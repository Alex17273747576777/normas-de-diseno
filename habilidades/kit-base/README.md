# Kit base · diseño universal

Código de referencia listo para copiar en **cualquier** proyecto nuevo, Android o no. La idea:
dentro de dos horas de empezar, el proyecto ya tiene escala tipográfica, rejilla, iconos
dibujados, estados y movimiento — es decir, ya no puede parecer HTML.

## Qué hay aquí

| Fichero | Qué es |
|---|---|
| `diseno.md` | Plantilla de `DESIGN.md`: concepto, 3 direcciones, tipografía, color, densidad, prohibiciones. Se rellena **antes** de escribir código. |
| `Iconos.kt` | Set de iconos dibujados con `Path`, trazo uniforme. Copiar a `ui/`. |
| `Tema.kt` | Colores con rol, tres niveles de superficie, escala tipográfica. Copiar a `ui/`. |
| `Movimiento.kt` | Muelles y duraciones con nombre, para no inventarse curvas cada vez. |
| `prueba-diseno.kt` | El bloque de pruebas «ley de diseño» que se añade a `Pruebas.kt`. |

## Cómo se usa en un proyecto nuevo

1. Copia `diseno.md` como `DESIGN.md` en la raíz y **rellénalo** (concepto + 3 direcciones).
2. Copia `Tema.kt`, `Iconos.kt` y `Movimiento.kt` a `app/src/main/java/.../ui/`.
3. Pega el bloque de `prueba-diseno.kt` en `Pruebas.kt` y ajusta la ruta del paquete.
4. Ejecuta las pruebas **antes** de escribir la primera pantalla. Si fallan por falta de
   pantallas, es que aún no hay nada que romper: sigue y vuelve a pasarlas al final.

## Regla del kit

El kit **no crece por acumulación**. Cada elemento nuevo entra porque una pantalla real lo
necesitaba, y cada elemento que deja de usarse se borra. Un kit que crece solo es un
almacén, y los almacenes no diseñan.
