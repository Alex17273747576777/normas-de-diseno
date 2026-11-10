# Reglas obligatorias de operación

Estas no son de diseño: son de **cómo se trabaja**. Se aplican a todos los repositorios y a
todos los tramos. Cada una nació de un fallo real, y eso está escrito al lado.

## 1. Limpiar el entorno local en cada turno

Al cerrar un tramo, antes de decir «hecho»:

```bash
rm -rf /tmp/proy /tmp/estudio /tmp/fuentes /tmp/apk-*.apk /tmp/*.log /tmp/chk* /tmp/verif*
```

**Por qué:** un clon olvidado y una descompilación de 200 MB hacen que el siguiente tramo
empiece con el disco lleno y sin saber qué fichero es de fiar. El script `03-cerrar-tramo.sh`
lo hace solo, y es el último paso por algo.

## 2. Subir la versión en los tres sitios donde vive

`app/build.gradle` (`versionCode` **y** `versionName`), `MainActivity.kt` (`version = …`) y
`RegistroFallos.kt` (`VERSION_REBORN`). Si no coinciden, el APK miente sobre sí mismo.

**Por qué:** el `versionCode` se quedó en 9 una vez y el APK publicado se instaló encima del
anterior sin actualizarse. Se detectó comparando el `badging` del APK descargado con el
`build.gradle`, y por eso ese paso es ahora una comprobación automática, no una promesa.

## 3. Commit, push y release en el mismo turno

Nunca se deja trabajo en el disco sin subir. Y la release se **verifica anónimamente**: se
descarga el asset publicado sin sesión, se comprueba el SHA-256 y la firma, y se mira el
`versionCode` del APK descargado —no el del fichero local—.

**Por qué:** el objeto que importa es el que se descarga el usuario, no el que se compiló.

## 4. Una incidencia por cada cosa pendiente

Lo pendiente que vive en el chat se pierde. Al cerrar un tramo se recorren los pendientes y cada
uno se abre en el repositorio que le corresponde, con **criterio de cierre** explícito.
`04-incidencias.sh` lo hace desde un fichero de texto.

**Por qué:** el `LazyColumn` anidado estuvo tres versiones cerrando la app. Como incidencia
habría tenido número, dueño y estado, en vez de ser un rumor.

## 5. Ninguna afirmación sin prueba, y ninguna prueba sin decir qué no cubre

Cada vez que se dice «está arreglado», va con **cómo se comprobó**. Y cada entrega añade a
`PROBADO.md` una sección con lo que **no** se ha podido probar y por qué.

**Por qué:** la app se cerró tres versiones seguidas porque se dijo «arreglado» sin haberlo
reproducido nunca en un teléfono.

## 6. Los procedimientos se ejecutan antes de entregarse

Un script que no se ha corrido no es un script: es un borrador. Antes de dar por hecho un
procedimiento, se ejecuta con datos reales y se corrige lo que salga.

**Por qué:** `01-censar-catalogo-appteka.py` daba `total` como el número de apps cuando en
realidad era un identificador interno (338127); se descubrió al correrlo, no al escribirlo.

## 7. No copiar recursos ajenos, sólo estructura

De una app de la que se aprende se copia **cómo ordena la información**, nunca sus iconos,
fuentes, colores ni marca. Se anota en `APRENDIDO-DE-APPS.md` qué se tomó y qué se descartó.

**Por qué:** copiar el tema de otra app es exactamente lo que hace que una app parezca una
plantilla de otra.

## 8. Diseño: la ley se vigila con pruebas, no con buenas intenciones

Toda regla de diseño que se escriba tiene que tener su comprobación en `Pruebas.kt`. Una regla
sin prueba se pierde en el tramo siguiente.

**Por qué:** la ley de diseño de la 1.7.1 no tenía prueba para los degradados ni para el
violeta, y en la 1.8.1 aparecieron 18 usos de vidrio y 4 pantallas con degradado que llevaban
tres versiones ahí sin que nadie los viera.

## 9. El idioma y el tono

Se responde en español y **en pocas palabras**; el detalle va en los ficheros del repositorio.
Nada de adornos en el chat. Lo que no se ha podido hacer se dice en la primera frase, no en la
última.

## 10. La compilación ocurre en la nube, nunca en local

Desde el 10-11-2026 no se compila ni se firma en la máquina de trabajo. Se hace en GitHub Actions
(`.github/workflows/version.yml`), que compila, prueba, firma, verifica el certificado y publica.
En local no hay SDK de Android ni Gradle, y eso es a propósito: así no puede volver a pasar que
el APK que se prueba no sea el que se publica.

**Consecuencia práctica:** un cambio no está terminado hasta que el workflow está en verde. Un
`./gradlew` local que «compila» ya no prueba nada, porque aquí no existe.

**Por qué:** la 1.12.1 se quedó bloqueada diciendo «no hay clave» cuando la clave existía. El
problema estaba en el CI —un secreto mal formado y un verificador que no entendía el formato de
huella de `apksigner` 35— y sólo se vio lanzándolo.

## 11. En el espacio de trabajo no se guarda nada que no sea un token

Ni capturas, ni APK, ni clones, ni descompilaciones, ni copias de catálogos.

| Dónde vive | Qué puede vivir ahí |
|---|---|
| Espacio de trabajo | **Sólo credenciales**: token de GitHub y keystore. Nada más. |
| `/tmp` | Temporal de un turno. Se borra al cerrarlo. |
| Repositorio | Todo lo demás: código, documentos, capturas, datos, kit de publicación. |

Si un turno necesita un fichero para trabajar, se clona en `/tmp`, se usa, se sube al repositorio
y se borra antes de decir «hecho». **El repositorio es la fuente de verdad; el disco, una
servilleta.** Lo que llega adjunto en un mensaje (capturas, documentos) también se sube al
repositorio y se borra del espacio de trabajo.

**Por qué:** al empezar el turno del 10-11-2026 había 48 MB de basura de tramos anteriores
—capturas de dos días antes, un APK de la 1.11.0 dentro del kit de publicación, clones sueltos—
y ni un solo sitio donde mirar qué era de fiar.

## 12. El disco y el repositorio están sincronizados

No hay dos versiones de nada. Si una regla está en el disco y no en el repositorio, la regla no
existe. `normas/` se compara con su remoto y se sube en el mismo turno en que se toca; si hay
cambios locales sin subir, o commits en el remoto que aquí no están, el turno no está cerrado.

**Cómo se comprueba:** `procedimientos/06-auditar-reglas.sh` cuenta las reglas, comprueba que la
numeración no tiene saltos, verifica qué reglas tienen quien las vigile y falla si hay cambios
sin subir o el remoto va por delante. Se ejecuta antes de cerrar, y en el CI de `normas`.

**Por qué:** el 10-11-2026 el `git status` mostraba cambios de permisos en cuatro
procedimientos que nadie había revisado, `normas/` no tenía remoto configurado y al disco le
faltaban cuatro commits del repositorio. Tres formas silenciosas de que el disco y el
repositorio digan cosas distintas.

---

Estas doce reglas están resumidas en `REGLAS.md` (diseño) y `SKILLS.md` (habilidades). Si alguna
deja de tener sentido, se cambia **y se anota por qué**, no se borra sin más.
