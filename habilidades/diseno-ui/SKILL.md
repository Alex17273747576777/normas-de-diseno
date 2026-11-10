---
name: diseno-ui
description: Diseña y critica interfaces para que no parezcan una página HTML. Obligatoria antes de escribir cualquier pantalla.
---

# Habilidad · Diseño de interfaz

> **Prohibido que una interfaz nuestra parezca HTML, plantilla o panel genérico.**
> Norma completa: [`../../NORMAS-DE-DISENO.md`](../../NORMAS-DE-DISENO.md)

## Cuándo se usa

- Antes de crear una pantalla nueva.
- Antes de dar por buena una pantalla existente.
- Cuando el usuario dice «parece HTML», «parece plantilla», «está feo» o similar. **No se
  discute: se rehace.**

## Procedimiento

**1. Concepto.** Una frase que describa la idea visual del producto. Ejemplo real de GLTools
Reborn: *«Herramienta de precisión: oscura, densa, con los datos del teléfono a la vista y el
estado siempre arriba»*. Esa frase decide todo lo demás.

**2. Tres direcciones.** Tres propuestas **distintas de verdad** (no tres colores del mismo
diseño). Se comparan y se elige una. Documenta por qué se descartaron las otras dos.

**3. Jerarquía.** Escribe, en una lista ordenada, qué debe ver el ojo en la pantalla, del 1 al
5. El elemento 1 se lleva el tamaño grande; el resto baja. Si dos empatan, uno sobra.

**4. Rejilla.** Espaciado múltiplo de 4 (preferible 8). Densidad decidida de antemano.

**5. Tipografía.** Seis pasos como mínimo, cada uno con su rol. Título ≥ 18 sp, etiqueta ≤
11 sp, cuerpo 12–13 sp.

**6. Iconos.** Dibujados con `Path`. Mismo grosor y mismo tamaño óptico. Ver
`Iconos.kt` de GLTools Reborn como implementación de referencia.

**7. Superficies.** Fondo / contenido / flotante. Vidrio sólo en flotante. Radios variados.

**8. Color al final.** Un acento de marca. Verde/ámbar/rojo con significado. Contraste
4,5:1 **medido**.

**9. Movimiento.** Muelle en lo que se toca. Nada decorativo.

**10. Estados.** Vacío, cargando, error, deshabilitado-explicado. Cada uno diseñado.

**11. Crítica.** Pasa la Parte IV de `NORMAS-DE-DISENO.md`. Si falla una casilla, vuelve al
paso 3.

## Reglas que no se rompen

- Ningún icono es un carácter de texto. Jamás.
- Ningún estado vacío dice sólo «No hay datos».
- Ningún degradado sin función.
- Nunca vidrio sobre vidrio.
- Nunca todos los radios iguales.
- Nunca tres botones iguales seguidos.
- Nunca tres tarjetas idénticas en fila como única estructura.

## Errores ya cometidos

1. **Glifos como iconos** (`◇ ◆ ✦ ▤ ? ✓ × ↻`) → es EL síntoma de HTML. Costó un tramo entero
   arreglarlo. Ahora hay prueba que lo bloquea.
2. **Degradado en cada tarjeta y vidrio en cada caja** → todo pesa igual, nada destaca.
3. **Diez secciones planas en una barra** → sin jerarquía. Cinco destinos y subpestañas.
4. **Cristal como superficie por defecto** en vez de acento. La crítica de NN/g a Liquid Glass
   es exactamente esto: legibilidad por debajo de 4,5:1.
5. **Confundir «moderno» con «tarjetas redondeadas»**. Moderno en 2026 es tipografía con
   énfasis, movimiento con física y **radios variados**.

## Cómo se comprueba

En GLTools Reborn, `pruebasNucleo` ejecuta el bloque **«ley de diseño»**: 16 comprobaciones que
leen el código fuente. Vigila glifos, número de tamaños de letra, existencia de muelle,
proporción vidrio/texto, estados vacíos y emojis. **Se verificó por sabotaje**: se metió un `◆`
a propósito y la suite falló señalando `Home.kt:81`.

En un proyecto nuevo: copia ese bloque de pruebas antes de escribir la primera pantalla.
