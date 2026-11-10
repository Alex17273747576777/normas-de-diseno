# Habilidades · GLTools Reborn

El proceso de estos 37 tramos, destilado. No es un diario: es lo que hay que hacer otra vez,
en orden, con los errores que ya se cometieron y no hay que repetir.

Índice:

1. [Construir y publicar un APK firmado](#1-construir-y-publicar-un-apk-firmado)
2. [Diseñar interfaz que no parezca HTML](#2-diseñar-interfaz-que-no-parezca-html)
3. [Navegación y arquitectura de pantallas](#3-navegación-y-arquitectura-de-pantallas)
4. [Probar sin teléfono](#4-probar-sin-teléfono)
5. [Reglas de honestidad](#5-reglas-de-honestidad)
6. [Conseguir datos reales sin relleno](#6-conseguir-datos-reales-sin-relleno)
7. [Android sin root: qué se puede de verdad](#7-android-sin-root-qué-se-puede-de-verdad)
8. [Errores que YA se cometieron](#8-errores-que-ya-se-cometieron)
9. [Checklist de cierre de tramo](#9-checklist-de-cierre-de-tramo)

---

## 1. Construir y publicar un APK firmado

**Entorno.** `ANDROID_HOME=/opt/android-sdk`, `GRADLE_USER_HOME=/opt/gradle-home`,
clave en `/home/user/.firma/reborn-release.jks` (alias `reborn`), contraseña en `.pass`,
token de GitHub en la **primera línea** de `/home/user/.gh-tokens`.

```bash
git clone https://github.com/Alex17273747576777/gltools-reborn.git /tmp/proy
echo "sdk.dir=/opt/android-sdk" > /tmp/proy/local.properties
export ANDROID_HOME=/opt/android-sdk GRADLE_USER_HOME=/opt/gradle-home \
  REBORN_KEYSTORE=/home/user/.firma/reborn-release.jks \
  REBORN_STORE_PASS=$(cat /home/user/.firma/.pass) \
  REBORN_KEY_PASS=$(cat /home/user/.firma/.pass) REBORN_KEY_ALIAS=reborn
./gradlew :app:pruebasNucleo :app:lintDebug :app:assembleRelease --no-daemon
```

**Orden obligatorio:** pruebas → lint → APK normal → APK `-PrebornDatos=crudo` → copiar a
`apk/` → `sha256sum`/`md5sum` → crear release → subir 4 assets → **descargar de nuevo y
verificar**. Si un paso falla, no se publica.

**Trampa del orden de compilación:** Gradle reutiliza la salida. Tras compilar con
`-PrebornDatos=crudo` hay que **volver a compilar sin el flag** o el APK «normal» sale de
15 MB. Compilar siempre el normal **después** del crudo, y comprobar el tamaño de cada uno.

**Verificación de verdad** (sin sesión, como lo haría cualquiera):

```bash
curl -sL -O .../releases/download/vX/GLTools-Reborn-X.apk
sha256sum -c SHA256SUMS.txt
apksigner verify --print-certs *.apk      # debe dar 1ff4c6ee…c6c9e803
aapt2 dump badging *.apk | grep -E "versionCode|versionName"
aapt2 dump badging *.apk | grep uses-permission
```

**Comprobar que el código nuevo va dentro** (esto faltaba y es lo que evita publicar un APK
de la versión anterior):

```bash
unzip -qo app.apk -d /tmp/x && strings -a /tmp/x/classes*.dex | grep "un texto nuevo tuyo"
```

---

## 2. Diseñar interfaz que no parezca HTML

**Diagnóstico.** Una pantalla parece una página web cuando: los iconos son caracteres, todas
las tarjetas pesan lo mismo, hay degradado en cada caja, y nada se mueve.

**Cómo se arregla, en este orden:**

1. **Jerarquía antes que decoración.** Decide qué es lo primero que el ojo debe ver. En Home
   es el cartel de estado; todo lo demás baja un escalón. Si dos cosas pesan igual, una sobra.
2. **Iconos dibujados.** `Canvas` + `Path` + `Stroke(width = size.minDimension * 0.085f)`,
   con `StrokeCap.Round` y `StrokeJoin.Round`. Un solo grosor para todos. Nunca un glifo.
   Implementación de referencia: `ui/Iconos.kt`.
3. **Escala tipográfica de verdad.** 10–11 sp etiquetas en mayúsculas con `letterSpacing`
   1–3 sp, 13 sp cuerpo, 19–22 sp títulos, 22 sp cifras. Light para titulares grandes,
   Bold sólo en etiquetas y cifras.
4. **El cristal es para lo que flota.** Barra de navegación, píldoras, chips. El contenido va
   sobre superficies casi opacas. Si todo es vidrio, no hay profundidad.
5. **Color con significado, no de adorno.** Verde = se puede, ámbar = ojo, rojo = no se puede.
   Un color que no comunica nada, fuera.
6. **Estados vacíos diseñados.** No «No hay datos»: qué es esto, por qué está vacío, y un
   botón para salir del estado vacío.
7. **Movimiento con física.** `spring(dampingRatio = MediumBouncy, stiffness = MediumLow)` al
   seleccionar; el resto, transiciones cortas. Nada de `animateFloatAsState` con linear por
   defecto.
8. **Botones por importancia.** Primario (color pleno), secundario (vidrio), destructivo
   (rojo). Nunca tres botones iguales en una fila.

**Regla de la casa:** si el diseño propio no está a la altura, **se copia la estructura** de
una app buena (ReDantotsu, Material 3 Expressive, iOS 26) y se refina. Nunca se justifica
«es que es lo que hay».

Detalle completo y lista de prohibiciones: `REGLAS.md`.

---

## 3. Navegación y arquitectura de pantallas

**El fallo:** diez secciones planas en una píldora. Caben de milagro, sin jerarquía, y la
primera pantalla era un catálogo en vez de un resumen.

**La forma que funciona:** **5 destinos** en la barra, cada uno con sus **subpestañas**.

```
HOME        (sin subpestañas: es un resumen)
PERFILES    Catálogo · Aplicar · Generar
HERRAMIENTAS Configurar · Rendimiento · Apps · Pantalla · Red
DATOS       TOP500 · Aplicado · Dispositivos
AYUDA       Compat. · Diagnóstico · Límites · Fuentes
```

**Cómo hacer el cambio sin perder nada** (esto es lo que costó):

1. Define destinos y pestañas **como datos puros** en un fichero aparte
   (`ui/Arquitectura.kt`), con un mapa `sección antigua → pestaña nueva`.
2. Escribe la prueba que comprueba que **todas** las secciones antiguas siguen teniendo
   sitio, **antes** de tocar la UI.
3. Cambia el `when` de la pantalla de `seccion` a `pestana`.
4. Sólo entonces borra el enum viejo y las funciones de navegación viejas.
5. Compila entre cada paso. Un `when` mal cerrado se arregla en un minuto; cinco a la vez,
   en una hora.

**Aviso de refactor con llaves:** al sustituir bloques grandes con Python, cuenta llaves
(`depth += l.count('{') - l.count('}')`) y verifica que las etiquetas del `when` están todas
a la misma profundidad **antes** de compilar. Es más rápido que leer el error del compilador.

---

## 4. Probar sin teléfono

Aquí no hay `/dev/kvm` ni dispositivo conectado. Todo lo que se pueda comprobar en JVM, se
comprueba.

- `./gradlew :app:pruebasNucleo` — `JavaExec` sobre la lógica pura. Hoy: **267 comprobaciones**.
- La lógica que se quiere probar **tiene que ser pura**: por eso la navegación, el banner de
  estado y la configuración son `object` con funciones que devuelven datos, no `@Composable`.
- Las pruebas pueden **leer el código fuente** y comprobar reglas de estilo: que no haya
  `LazyColumn` anidado, que los iconos usen `Path`, que no queden glifos. Parece trampa y no
  lo es: es la única forma de vigilar una regla de diseño sin instrumentación.
- `org.json` no existe en JVM: hay una configuración aparte `pruebasJson` con su dependencia.
  No meter `org.json` como `implementation`.
- Una prueba que **nunca ha fallado** no vale nada: saboréala (rompe a propósito, comprueba
  que falla, restaura). Ya se hizo y se documentó.

---

## 5. Reglas de honestidad

Estas no se negocian nunca.

- **Lo no probado se dice.** No «compatible» a secas: `VERIFICADO` / `PARCIAL` /
  `SIN_VERIFICAR`.
- **Nunca fingir identificadores únicos** (IMEI, serie, MAC, Android ID). Están bloqueados en
  el filtro y hay prueba de que se bloquean.
- **Shizuku no es root.** Trae permisos de `adb shell`. El cartel de estado lo dice en su
  propio texto, y una prueba falla si alguien escribe «el mejor modo posible».
- **Sin vía = rojo.** Si no hay Shizuku ni `su`, la app abre, lee y dice que no puede
  escribir. Un botón que responde «aplicado» sin haber aplicado nada es una mentira, y es el
  peor fallo posible en esta app.
- **Lo que no se ha ejecutado en un teléfono físico, se declara.** En cada entrega.

---

## 6. Conseguir datos reales sin relleno

- **Antes de rastrear, lee `robots.txt`.** `versus.com` responde 202 vacío con Cloudflare:
  no se rastrea. Eso se documenta en `FUENTES-DE-DATOS.md` con el motivo.
- **Los datos van dentro del APK** (`assets/datos/`) y hay un `manifiesto.json` que declara
  cada bloque, su origen, su licencia y cuándo se descargó.
- **14,33 MB de datos comprimen a ~3 MB de APK.** El ZIP comprime. Por eso hay dos
  variantes: la normal (3 MB) y `-PrebornDatos=crudo` (15,5 MB). Es la única forma honesta de
  que el peso sea contenido real y no relleno.
- **No guardes caché de HTML en `/tmp`**: es tmpfs de 992 MB y se llena
  (`No space left on device`). Rastrea sin caché y guarda sólo el JSON final. Y **no borres la
  caché antes de tener el JSON** o hay que rastrear otra vez.
- Los campos ausentes se quedan **vacíos**, no se inventan.

---

## 7. Android sin root: qué se puede de verdad

Lo verificado por shell (`adb shell` vía Shizuku) y lo que no:

| Se puede | No se puede |
|---|---|
| Escribir `ro.*` de identidad (modelo, marca, device, hardware, `ro.opengles.version`) | Escribir `/system`, montar particiones, tocar el kernel |
| Escala de animaciones, densidad, tasa de refresco | Sustituir el driver OpenGL ES |
| DNS privado, congelar/descongelar apps, limpiar caché | Forzar Vulkan real en una app |
| Leer propiedades, SoC, GPU, apps, pantalla | Falsificar IMEI/serie/MAC |
| Doze, gobernadores que expone el sistema | Cualquier cosa que exija SELinux permisivo |

Regla: **una casilla gris explicada es mejor que una casilla que miente.** Las que necesitan
root salen en gris con la etiqueta «Necesita root» y su motivo.

---

## 8. Errores que YA se cometieron

No repetir:

1. **`by lazy` no protege del orden de inicialización.** Lo que arregló el NPE fue declarar
   la propiedad **antes** y envolver en `try/catch`. No reescribir la prueba afirmando lo
   contrario.
2. **`LazyColumn` dentro de `LazyColumn`** cierra la app al medir. Si un composable se pinta
   dentro del scroll principal, usa `Column`. Hay prueba que lo vigila.
3. **Iconos como glifos de texto** → parece HTML. Prohibido y vigilado.
4. **Compilar el APK normal justo después del crudo** sin recompilar → el «normal» sale de
   15 MB.
5. **Refactor de bloques con llaves a mano** → estructura desalineada. Usa conteo de llaves.
6. **Copiar strings de recursos** en vez de recursos → hay que versionar los `.xml` del icono
   adaptativo en `mipmap-anydpi-v26` y el `roundIcon` en el manifiesto.
7. **Prometer lo que el sitio no expone** (el listado de AxManager no está en el HTML
   estático): no prometer «las 280 fichas».
8. **Borrar `/tmp/proy` antes de terminar** las comprobaciones: hay que limpiar al cerrar,
   no antes.

---

## 9. Checklist de cierre de tramo

- [ ] `pruebasNucleo` en verde, y **el número de comprobaciones sube o se mantiene**.
- [ ] `lintDebug` con 0 errores.
- [ ] `versionCode` incrementado, `versionName` actualizado.
- [ ] APK normal y crudo compilados **en ese orden**, con tamaños medidos.
- [ ] Firmados con la misma clave (`apksigner --print-certs`).
- [ ] `README.md` y `PROBADO.md` actualizados, con lo probado y **lo no probado**.
- [ ] Commit y push; `git ls-remote` confirma el HEAD.
- [ ] Release con 4 assets; descarga de nuevo y verificación `sha256sum -c` + `apksigner`.
- [ ] `strings` sobre los `.dex` confirma que el código nuevo está dentro.
- [ ] Página `GLTools-X.html` en `/home/user` y presentada.
- [ ] `/tmp/proy` y temporales borrados; `/home/user` sin ficheros viejos.

---

## Anexo · Dónde está cada cosa

| Pieza | Ruta |
|---|---|
| Navegación y estado (puro, probable) | `ui/Arquitectura.kt` |
| Home | `ui/Home.kt` |
| Barra de destinos y pestañas | `ui/Navegacion.kt` |
| Iconos vectoriales | `ui/Iconos.kt` |
| Pantalla Configurar + modelo de filas | `ui/Configurar.kt` |
| Pantalla principal y secciones | `ui/Pantalla.kt` |
| Tema (colores `Cristal`, tipografía) | `ui/Tema.kt` |
| Motor | `core/*.kt` |
| Pruebas | `app/src/test/java/Pruebas.kt` |
| Datos | `app/src/main/assets/datos/` |
| Icono de lanzador | `res/mipmap-anydpi-v26/`, `res/drawable/ic_launcher_*.xml` |
