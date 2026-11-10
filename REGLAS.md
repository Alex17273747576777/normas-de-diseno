# LEY DE DISEÑO · GLTools Reborn

> **Regla vigente desde la 1.7.1, ampliada en la 1.8.1. No es una preferencia. Es una prohibición.**

## PROHIBIDO

Que la app que construimos parezca una **página HTML**, ya sea genérica o «moderna».

Esto incluye, y no es una lista cerrada:

- Iconos que son **caracteres de texto** (`◇ ◆ ✦ ▤ ? ↻ ✓ ×`) en vez de rutas dibujadas.
- **Tarjetas idénticas apiladas** sin jerarquía: todo el mismo radio, la misma opacidad, el
  mismo peso, la misma separación. Si al mirar la pantalla no sabes qué es lo importante en
  menos de un segundo, está mal.
- **Degradados por todas partes**. Un degradado es un acento, no un fondo de sistema.
- **Cristal/glass en todo**. El vidrio es para lo que flota (barra, píldoras), no para cada
  caja de contenido.
- Tipografía por defecto del sistema, sin escala: títulos y cuerpo casi del mismo tamaño.
- Listas de texto largas como única interfaz, cuando el dato pedía una tabla, un gráfico o
  un número grande.
- Estados vacíos que dicen «No hay datos» y nada más.
- **Cero movimiento**: nada responde al toque, nada entra ni sale, todo aparece de golpe.
- Botones con el mismo aspecto sea cual sea su importancia (primario / secundario / destructivo).
- Emojis como iconos de interfaz.
- **Cinco acentos compitiendo.** Si el violeta, el cian y el rosa hacen falta para que la
  pantalla «tenga vida», lo que falta es jerarquía, no colores. **Un** acento, y el resto
  neutro.
- **Violeta de plantilla** (`#7C4DFF`, `#6C5CE7`, `#A855F7` y parientes). Es la huella dactilar
  del tema por defecto de un framework. Se prohíbe.
- **Degradados decorativos**, incluido el `linearGradient` de dos tonos en un botón o una
  tarjeta para que «se vea moderno». El color sirve para decir algo, no para adornar.
- **Vidrio en el contenido.** Si la superficie no flota sobre nada, no es vidrio: es una caja.

Si el resultado se puede confundir con un `index.html` con Bootstrap, **está mal y se rehace**.

## OBLIGATORIO

Cuando el diseño propio no esté a la altura:

1. **Copiar la estructura** de una app que sí está bien hecha. Estructura, no recursos: ni
   iconos, ni fuentes, ni marca ajena.
2. **Refinar**: arreglar sus errores, quitar lo que sobra, adaptarlo a este producto.
3. **Mejorar cada vez**: fusionar funciones, no añadir pantallas nuevas al lado de las viejas.

## La superficie y el color, por escrito

1. **Fondo neutro**: tres tonos de gris con los canales RGB casi iguales (diferencia ≤ 24). Si el
   fondo tiene color, compite con el contenido.
2. **Tres niveles de superficie** que se distinguen **por tono**, no por borde ni por sombra:
   `superficie`, `superficieAlta`, `superficieMasAlta`. Eso da profundidad sin dibujar cajas.
3. **Un acento** para lo accionable y **color con significado** para el estado: verde = bien,
   ámbar = ojo, rojo = no se puede. Nada de color porque sí.
4. **El contenido se apoya en el fondo.** Filas separadas por un hueco o un hilo de 1 px, no
   cajas dentro de cajas. Una caja sólo cuando el contenido de verdad necesita un límite.
5. **Jerarquía tipográfica real**: el dato principal es grande (≥ 24 sp), lo secundario pequeño
   (11–12 sp), las etiquetas en versalitas. Si todo mide lo mismo, no hay diseño.

## Referencias aceptadas

| App | Qué se toma |
|---|---|
| **ReDantotsu** | Barra inferior en píldora de cristal, muelle al seleccionar, jerarquía tipográfica |
| **Material 3 Expressive** | Escala de tipos, formas, color por rol, movimiento con física |
| **iOS 26 / Liquid Glass** | Superficies que flotan sobre contenido, no cajas sobre fondo |
| **GLTools original** | Estructura de pantallas: Home con estado arriba, tiles grandes, configuración por pestañas en mayúsculas |

## Aprender de las apps que ya existen (1.9.0)

Antes de inventar una pantalla, **mirar cómo la resolvieron otros**. No de memoria ni de
impresiones: descargar el APK, desmontarlo con `aapt2` y `jadx`, mirar sus capturas.

Qué se copia y qué no:

| Se copia | No se copia |
|---|---|
| La estructura: cómo ordena la información | Iconos, fuentes, ilustraciones |
| El patrón de interacción que resuelve el problema | Colores y marca ajena |
| La jerarquía: qué es lo primero que se lee | El tema por defecto de su framework |

Un patrón que merece la pena tener a mano: **el carrusel de píldoras**. Cuando hay más de
cuatro grupos de datos y no caben a la vez, una fila de píldoras que se desplaza con una
encendida —y un solo panel debajo que cambia— resuelve el problema sin una lista que se
desplaza sin fin. Es de *Hardware Monitor* y está en GLTools Reborn desde la 1.9.0.

## Cómo se comprueba (no es retórica)

La regla está **vigilada por pruebas automáticas** (bloques «ley de diseño» y «sin disfraz de
plantilla»): cuentan los colores de la paleta por canales RGB para cazar violetas, cuentan los
`Brush.*Gradient(` en las pantallas, cuentan los usos de `.vidrio(` y exigen los tres niveles de
superficie. En la 1.8.1 estas pruebas encontraron 18 usos de vidrio y 4 pantallas con degradado
que llevaban tres versiones ahí, a la vista, sin que nadie las viera. **Eso es la prueba de que
la ley sirve.**

Además la regla está vigilada en `app/src/test/java/Pruebas.kt`,
bloque «ley de diseño». Si alguien vuelve a meter un icono de texto, la suite falla y el
APK no se publica. Eso es lo que la convierte en ley y no en un deseo.
