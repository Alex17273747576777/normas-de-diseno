# Habilidad · sistema de superficie y color

Sirve para cualquier app que tenga que verse hecha a mano y no generada.

## La paleta, en cinco decisiones

1. **Fondo neutro.** Tres tonos. Canales RGB casi iguales (diferencia ≤ 24). Un fondo con color
   vuelve ilegible todo lo que se apoye encima.
2. **Tres superficies** que se distinguen **sólo por tono** (por ejemplo `#14181E`, `#1B2028`,
   `#232A34`). Profundidad sin dibujar ni una caja.
3. **Un acento** para lo accionable. Uno. Si necesitas dos, es que sobra una acción.
4. **Color con significado**: verde = bien, ámbar = ojo, rojo = no se puede. Nunca decorativo.
5. **Bordes de luz** (`#14FFFFFF`, `#24FFFFFF`) en vez de sombras: funcionan en oscuro sin
   ensuciar.

## Los cinco errores que delatan una plantilla

| Error | Cómo se ve | Arreglo |
|---|---|---|
| Violeta de plantilla | `#7C4DFF`, `#6C5CE7` | un azul de marca, o nada |
| Cinco acentos | cada tarjeta de un color | un acento + color de estado |
| Degradado en cada caja | `linearGradient` de dos tonos | tono plano |
| Vidrio en el contenido | `backdrop blur` en tarjetas | superficie con tono |
| Todo mide lo mismo | títulos 16 sp, cuerpo 14 sp | dato principal ≥ 24 sp, etiquetas 11 sp versalitas |

## Regla de oro

El contenido se apoya en el fondo; las cajas sólo existen cuando el contenido **necesita** un
límite. Si dudas, quita la caja.
