---
name: empaquetar-y-publicar-apk
description: Compila, firma, publica y VERIFICA un APK. Con el orden correcto y las trampas conocidas.
---

# Habilidad · Empaquetar y publicar un APK

## Cuándo se usa

Cada entrega de una app Android.

## Procedimiento (el orden importa)

```bash
# 1. Entorno
export ANDROID_HOME=/opt/android-sdk GRADLE_USER_HOME=/opt/gradle-home
export REBORN_KEYSTORE=/home/user/.firma/reborn-release.jks
export REBORN_STORE_PASS=$(cat /home/user/.firma/.pass)
export REBORN_KEY_PASS=$(cat /home/user/.firma/.pass) REBORN_KEY_ALIAS=reborn

# 2. Clon limpio
git clone https://github.com/Alex17273747576777/gltools-reborn.git /tmp/proy
echo "sdk.dir=/opt/android-sdk" > /tmp/proy/local.properties

# 3. Pruebas → lint → APK normal
./gradlew :app:pruebasNucleo :app:lintDebug :app:assembleRelease --no-daemon
cp app/build/outputs/apk/release/app-release.apk apk/GLTools-Reborn-X.apk

# 4. APK crudo (SIEMPRE DESPUÉS del normal)
./gradlew :app:assembleRelease --no-daemon -PrebornDatos=crudo
cp app/build/outputs/apk/release/app-release.apk apk/GLTools-Reborn-X-sin-comprimir.apk

# 5. Sumas
(cd apk && sha256sum *.apk > SHA256SUMS.txt && md5sum *.apk > MD5SUMS.txt)

# 6. Publicar (4 assets) y luego VERIFICAR descargando otra vez
```

## Trampas conocidas

1. **Gradle reutiliza la salida.** Si compilas el crudo y luego no recompilas el normal, el
   «normal» sale de 15 MB. **Compilar el normal después del crudo** y comprobar el tamaño.
2. **`apk/` no se sube al repo** pero sí se usa para preparar los assets: crear la carpeta
   vacía antigua puede quedarse con APK viejos dentro. Limpiar antes de medir.
3. **El commit va antes de la release**, y `git ls-remote` confirma el HEAD: si no, estás
   publicando un APK que no corresponde a ningún commit visible.
4. **Un tag nuevo necesita release nuevo**: no se reutiliza el de la versión anterior.

## Reglas que no se rompen

- Sin `pruebasNucleo` en verde y `lintDebug` en 0 errores, **no se publica**.
- Se firma **siempre** con la misma clave (`1ff4c6ee…c6c9e803`). Cambiarla rompe las
  actualizaciones de quien ya tiene instalada la app.
- **Se verifica descargando de nuevo, sin sesión**, como lo haría cualquiera:

```bash
curl -sL -O .../releases/download/vX/GLTools-Reborn-X.apk
sha256sum -c SHA256SUMS.txt
apksigner verify --print-certs *.apk
aapt2 dump badging *.apk | grep -E "versionCode|versionName"
```

- **Se comprueba que el código nuevo va dentro** (esto evita publicar el APK de la versión
  anterior sin darse cuenta):

```bash
unzip -qo app.apk -d /tmp/x && strings -a /tmp/x/classes*.dex | grep "un texto nuevo tuyo"
```

## Errores ya cometidos

- Publicar el APK normal de 15 MB por compilar en el orden equivocado. Detectado midiendo.
- Dar por buena una release sin descargarla. Ahora siempre se descarga y se verifica.
- Sabotear una prueba para verificar que falla es **obligatorio**: una prueba que nunca ha
  fallado no demuestra nada.

## Cómo se comprueba

Todo lo anterior, en la lista de cierre de `SKILLS.md` del proyecto.
