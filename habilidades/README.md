# Habilidades · índice

Cada carpeta es una habilidad: un procedimiento que se puede repetir, con sus reglas, su
código de referencia y los errores que ya se cometieron para no repetirlos.

**Todas las habilidades heredan de `NORMAS-DE-DISENO.md`.** Ninguna puede contradecirlo: si
una habilidad dice «haz una tarjeta con degradado», la norma manda y la habilidad está mal.

| Habilidad | Para qué |
|---|---|
| [`diseno-ui/`](diseno-ui/SKILL.md) | Diseñar pantallas que no parezcan HTML. La más importante. |
| [`android-compose/`](android-compose/SKILL.md) | Construir la interfaz en Jetpack Compose sin romper la app. |
| [`android-shell-shizuku/`](android-shell-shizuku/SKILL.md) | Qué se puede hacer en Android sin root, y qué no. |
| [`empaquetar-y-publicar-apk/`](empaquetar-y-publicar-apk/SKILL.md) | Compilar, firmar, publicar y **verificar** un APK. |
| [`pruebas-sin-dispositivo/`](pruebas-sin-dispositivo/SKILL.md) | Probar sin teléfono conectado, y probar reglas de diseño. |
| [`datos-reales-sin-relleno/`](datos-reales-sin-relleno/SKILL.md) | Conseguir datos legítimos y meterlos en el APK. |
| [`honestidad-tecnica/`](honestidad-tecnica/SKILL.md) | Decir lo que está probado y lo que no. Transversal. |
| [`limpieza-y-cierre/`](limpieza-y-cierre/SKILL.md) | Cerrar un tramo sin dejar basura ni cabos sueltos. |

## Formato de una habilidad

```markdown
---
name: nombre-de-la-habilidad
description: una línea, qué hace y cuándo usarla
---

# Título
## Cuándo se usa
## Procedimiento (en orden)
## Reglas que no se rompen
## Errores ya cometidos (no repetir)
## Cómo se comprueba que se hizo bien
```
