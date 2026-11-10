# normas-de-diseno

**Base universal de diseño e ingeniería para todos nuestros proyectos. Presentes y futuros.**

> **Regla 0 — Prohibido que una interfaz nuestra parezca una página HTML, una plantilla o un
> panel genérico.** Si se puede confundir con un `index.html`, se rehace.
>
> Y cuando no haya diseño propio a la altura: **se copia la estructura de una app que sí
> funciona y se refina** —arreglando sus errores, quitando lo que sobra, fusionando funciones—.
> Nunca se justifica con «es que es lo que hay».

## Qué hay aquí

| Fichero | Qué es |
|---|---|
| [`NORMAS-DE-DISENO.md`](NORMAS-DE-DISENO.md) | La norma completa: diagnóstico con evidencia de 2026, 14 normas, método obligatorio, lista de crítica de 18 puntos y fuentes. |
| [`REGLAS.md`](REGLAS.md) | La versión corta. Se copia dentro de cada repositorio de app. |
| [`README-NORMAS.md`](README-NORMAS.md) | Cómo se aplica a un proyecto nuevo y a uno que ya existe. |
| [`habilidades/`](habilidades/) | Ocho habilidades: diseño de interfaz, Compose, Android sin root, empaquetar y publicar, probar sin dispositivo, datos reales, honestidad, limpieza. |
| [`habilidades/kit-base/`](habilidades/kit-base/) | Código listo para copiar: tema, iconos dibujados, movimiento, plantilla `DESIGN.md` y el bloque de pruebas que vigila la ley. |

## Las 14 normas, en titulares

1. El concepto va antes que los componentes.
2. Jerarquía antes que decoración.
3. **Los iconos se dibujan, no se escriben.**
4. Escala tipográfica de verdad (mínimo 6 pasos).
5. Espaciado en rejilla de 4/8.
6. Color con significado; contraste 4,5:1 medido.
7. Superficies: fondo / contenido / flotante. Vidrio sólo en flotante, nunca sobre vidrio.
8. Movimiento con física de muelle, no adornos.
9. Todos los estados, y diseñados (vacío, cargando, error, deshabilitado explicado).
10. Botones por importancia.
11. Accesibilidad desde el principio (48 dp, etiquetas, escala al 200 %).
12. Datos: tabla, cifra o gráfico. Nunca un párrafo.
13. Una pantalla, un trabajo. Las funciones nuevas se **fusionan**, no se añaden al lado.
14. Nada de marca ajena: se copia estructura, jamás marca ni recursos.

## Por qué estas normas y no otras

No son gustos. Cada una sale de evidencia:

- **Material 3 Expressive** (Google, mayo 2025): 46 estudios, 18.000 participantes; 4× más
  rápido el reconocimiento de elementos, +34 % de percepción de modernidad. Sus tres pilares
  —tipografía con énfasis, movimiento con física, radios variados para **crear tensión**— son
  la base de N2, N4, N7 y N8.
- **El fracaso de Liquid Glass** en iOS 26 tal como lo documentó Nielsen Norman Group:
  «texto encima de texto crea un desastre ilegible», contrastes por debajo de 4,5:1, y Apple
  «priorizando el espectáculo sobre la usabilidad». De ahí N7 (vidrio sólo donde flota) y N6.
- **WCAG 2.2** (recomendación de la W3C): 4,5:1, objetivos de 24 px mínimo y 44–48
  recomendados. De ahí N11.
- **La literatura sobre interfaces generadas por IA**: el aspecto de plantilla viene de la
  falta de restricciones, no de la falta de talento. De ahí N1 (concepto y tres direcciones) y
  toda la Parte I.

## Cómo se hace cumplir

Una norma que sólo vive en un documento es un deseo. Por eso:

1. Escrita aquí.
2. **Probada**: en GLTools Reborn hay 20 comprobaciones que leen el código fuente y fallan si
   aparece un glifo, si la tipografía pierde la escala o si un estado vacío es «No hay datos».
   Se verificó por sabotaje.
3. En la lista de cierre de cada entrega: sin pasar la lista de crítica, no hay release.

## Estado

Aplicada y verificada en **GLTools Reborn 1.7.1**. Obligatoria desde el primer commit en
cualquier proyecto nuevo.
