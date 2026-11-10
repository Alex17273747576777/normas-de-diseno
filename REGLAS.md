# LEY DE DISEÑO · GLTools Reborn

> **Regla vigente desde la 1.7.1. No es una preferencia. Es una prohibición.**

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

Si el resultado se puede confundir con un `index.html` con Bootstrap, **está mal y se rehace**.

## OBLIGATORIO

Cuando el diseño propio no esté a la altura:

1. **Copiar la estructura** de una app que sí está bien hecha. Estructura, no recursos: ni
   iconos, ni fuentes, ni marca ajena.
2. **Refinar**: arreglar sus errores, quitar lo que sobra, adaptarlo a este producto.
3. **Mejorar cada vez**: fusionar funciones, no añadir pantallas nuevas al lado de las viejas.

## Referencias aceptadas

| App | Qué se toma |
|---|---|
| **ReDantotsu** | Barra inferior en píldora de cristal, muelle al seleccionar, jerarquía tipográfica |
| **Material 3 Expressive** | Escala de tipos, formas, color por rol, movimiento con física |
| **iOS 26 / Liquid Glass** | Superficies que flotan sobre contenido, no cajas sobre fondo |
| **GLTools original** | Estructura de pantallas: Home con estado arriba, tiles grandes, configuración por pestañas en mayúsculas |

## Cómo se comprueba (no es retórica)

La regla está **vigilada por una prueba automática** en `app/src/test/java/Pruebas.kt`,
bloque «ley de diseño». Si alguien vuelve a meter un icono de texto, la suite falla y el
APK no se publica. Eso es lo que la convierte en ley y no en un deseo.
