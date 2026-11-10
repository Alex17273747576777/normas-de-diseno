---
name: datos-reales-sin-relleno
description: Conseguir datos legítimos, verificables y con licencia para meter dentro de una app, sin inflar el peso.
---

# Habilidad · Datos reales sin relleno

## Cuándo se usa

Cuando el producto necesita un catálogo (dispositivos, fichas, puntuaciones) dentro del APK.

## Procedimiento

1. **Comprobar `robots.txt` antes de rastrear.** Si dice que no, o si responde vacío por
   Cloudflare, **no se rastrea** y se documenta el motivo.
2. **Preferir fuente con licencia clara**: Google Play Supported Devices (CSV público),
   Wikipedia, listados abiertos de fabricantes.
3. **Un `manifiesto.json`** que declare, por bloque: origen, URL, licencia, fecha de descarga y
   número de registros. Sin eso, el dato no entra.
4. **Rastrear sin caché de HTML.** `/tmp` es tmpfs de 992 MB y se llena. Guarda sólo el JSON
   final. Y **no borres la caché antes de tener el JSON**, o hay que rastrear otra vez.
5. **Los campos ausentes se quedan vacíos.** Nunca se inventa el valor que falta.
6. **Comprimir es comprimir, no engañar.** 14 MB de datos ocupan 3 MB de APK porque el ZIP
   comprime. Si se pide un APK de más peso, la variante honesta es `-PrebornDatos=crudo`
   (sin comprimir), no rellenar con basura.

## Reglas que no se rompen

- **Nada de relleno.** Ni imágenes de relleno, ni texto repetido, ni ficheros que no se usan.
- **Cada bloque de datos tiene una prueba** que comprueba que está dentro del APK y que tiene
  un mínimo de registros (p. ej. «más de mil fichas», «más del 90 % con GPU»).
- El APK funciona **en modo avión**: los datos viajan dentro.
- No se promete cobertura que la fuente no da.

## Errores ya cometidos

- Rastrear con caché de HTML → `No space left on device` y perder el trabajo.
- Borrar la caché antes de reconstruir el JSON → hubo que volver a rastrear.
- Intentar llegar a 10 MB comprimidos con relleno. **No**: se entregan dos variantes y se
  explica por qué el ZIP comprime.

## Cómo se comprueba

Pruebas sobre `assets/datos/`: existen los ficheros, tienen el mínimo de registros, el
manifiesto declara los bloques y explica qué se descartó y por qué.
