---
name: android-shell-shizuku
description: Qué se puede cambiar de verdad en Android sin root, con Shizuku o adb shell, y qué no se puede fingir.
---

# Habilidad · Android sin root (Shizuku / adb shell)

## Cuándo se usa

Cuando el producto promete «cambiar cosas del sistema» en un teléfono sin root.

## Lo que se puede, verificado

| Se puede | Cómo |
|---|---|
| Escribir propiedades `ro.*` de identidad (`ro.product.model`, `ro.product.brand`, `ro.product.device`, `ro.hardware`, `ro.opengles.version`) | `setprop` / `settings` vía shell |
| Escala de animaciones (3 escalas) | `settings put global window_animation_scale 0.5` |
| Densidad de pantalla | `wm density` |
| Tamaño de pantalla | `wm size` |
| Tasa de refresco | `settings put system peak_refresh_rate` |
| DNS privado | `settings put global private_dns_mode` |
| Congelar / descongelar apps | `pm disable-user` / `pm enable` |
| Limpiar caché de una app | `pm trim-caches` |
| Doze, gobernadores que exponga el sistema | `settings` / `cmd deviceidle` |
| Leer SoC, GPU, apps, pantalla | `getprop`, `dumpsys`, `pm list packages` |

## Lo que NO se puede sin root, y hay que decirlo

- Escribir en `/system`, montar particiones, tocar el kernel o SELinux.
- Sustituir el driver de OpenGL ES.
- Forzar Vulkan **de verdad** en una app que no lo pide.
- Falsificar IMEI, número de serie, MAC o Android ID. **Prohibido además por principio.**
- Cualquier cosa que exija `su`.

## Reglas que no se rompen

1. **Shizuku no es root.** Da permisos de `adb shell`. El texto de la interfaz no puede decir
   «root» cuando sólo hay Shizuku, y no puede decir «el mejor modo posible» nunca.
2. **Sin vía = decir que no hay vía**, en rojo, y no aplicar nada. Un botón que responde
   «aplicado» sin haber aplicado es el peor fallo posible.
3. **Una casilla gris explicada es mejor que una casilla que miente.** Lo que necesita root sale
   en gris, con la etiqueta «Necesita root» y su motivo.
4. **Cada escritura se anota antes de hacerse** y se deshace si la app muere a mitad.
5. **Alcance real de Shizuku**: permisos de `adb shell`. Nada más. Documentarlo así.

## Errores ya cometidos

- Se prometió cobertura de módulos que el sitio no expone (el listado de AxManager no está en
  el HTML estático). **No prometer «las 280»**: sólo lo que se puede leer.
- Se dio por hecho que HarmonyOS NEXT ejecuta APKs de Android. **No las ejecuta.**

## Cómo se comprueba

- Prueba en JVM con un **ejecutor falso**: que escriba, que omita valores vacíos, que confirme,
  que **no declare éxito si no cambió** y que restaure.
- El filtro de identidad (IMEI, serie, MAC, meid…) se prueba con 8 claves: 8 de 8 bloqueadas.
