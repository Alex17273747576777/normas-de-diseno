# NORMAS DE DISEÑO · UNIVERSAL

**Versión 2.0 · 8 de noviembre de 2026**
**Se aplica a: todo proyecto presente y futuro. Sin excepciones.**

---

## 0. La regla, en una línea

> **Ninguna interfaz nuestra puede parecer una página HTML, una plantilla de Bootstrap ni un
> panel genérico.** Si se puede confundir con un `index.html` con tarjetas redondeadas, no se
> publica: se rehace.

Y la consecuencia operativa:

> **Cuando no sepamos diseñar mejor, se copia la estructura de una app que sí está bien
> hecha y se refina.** Copiar estructura no es plagiar: es partir de algo que funciona en vez
> de improvisar. Lo que no se copia nunca es la marca, los iconos, las fuentes ni los recursos
> de otro producto.

---

# PARTE I · EL DIAGNÓSTICO

## 1. Por qué una interfaz acaba pareciendo una plantilla

La investigación sobre interfaces generadas por IA coincide en una causa, y no es la falta de
talento: es la **falta de restricciones**. Cuando el encargo es «limpio y moderno», el modelo
—cualquier modelo— cae en su opción estadísticamente más segura, y esa opción es siempre la
misma: tarjetas redondeadas, degradado azul-violeta, tipografía por defecto, tres tarjetas en
fila, jerarquía débil, mucho relleno. El resultado no es feo: es **intercambiable**. Puesto al
lado de otros diez productos, no se distingue.

Las ocho causas concretas, que son las que hay que cazar:

| # | Síntoma | Por qué delata |
|---|---|---|
| 1 | **Iconos que son caracteres de texto** (`◇ ◆ ✦ ▤ ? ✓ × ↻`) | No están dibujados, están escritos. Trazos de distinto grosor, tamaños que no casan. Es el síntoma nº 1 de «esto es una web». |
| 2 | **Tarjetas idénticas apiladas** | Mismo radio, misma opacidad, mismo peso. Sin jerarquía no hay diseño, sólo una lista. |
| 3 | **Degradado en cada caja** | Un degradado es un acento. En todas partes es decoración, y la decoración sin función es ruido. |
| 4 | **Vidrio/cristal en todo** | El vidrio existe para lo que *flota* sobre el contenido. Sobre el contenido aplana la jerarquía. |
| 5 | **Tipografía sin escala** | Títulos y cuerpo casi del mismo tamaño. El ojo no sabe dónde empezar. |
| 6 | **Espaciado improvisado** | Sin rejilla: 13, 17, 22 px. El ojo detecta la falta de ritmo aunque no sepa nombrarla. |
| 7 | **Estados vacíos perezosos** | «No hay datos». Un estado vacío es una oportunidad de diseño, no un hueco. |
| 8 | **Cero movimiento, o movimiento decorativo** | Nada responde al toque (muerto), o todo late sin motivo (mareante). |

## 2. La evidencia de 2026: el vidrio mal usado rompe el producto

No es opinión nuestra, es lo que le pasó a Apple con **Liquid Glass** en iOS 26:

- **Nielsen Norman Group** (Raluca Budiu, octubre 2025) tituló su análisis *«Liquid Glass is
  cracked, and usability suffers in iOS 26»*: «texto encima de texto crea un desastre
  ilegible», y concluyó que Apple estaba **「priorizando el espectáculo sobre la usabilidad」**.
- Contrastes por debajo de **4,5:1** de forma sistemática; texto sobre fondos borrosos y en
  movimiento; botones sin etiqueta que dejan de parecer botones; animaciones que distraen en
  vez de guiar; fatiga visual en sesiones largas.
- Apple tuvo que responder con un ajuste **Clear/Tinted** en iOS 26.1 y un **deslizador de
  transparencia** en iOS 27.

**Lo que se aprende, y se convierte en norma de esta casa:**

1. El vidrio **sólo** en lo que flota: barra de navegación, píldoras, hojas. Nunca en el
   contenido.
2. **Nunca** vidrio sobre vidrio.
3. Texto sobre superficie **sólida o casi opaca**. Si hay que poner texto sobre algo
   transparente, hace falta una capa de oscurecimiento del ~35 % y aun así hay que medir.
4. Toda superficie debe responder a **reducir transparencia** y **aumentar contraste**.
5. Apple lo dijo de sí misma: limitar los efectos **a los elementos funcionales más
   importantes**. Lo decorativo, fuera.

## 3. Lo que sí funciona en 2026: Material 3 Expressive

Google hizo **46 estudios con más de 18.000 participantes** antes de publicar M3 Expressive
(mayo 2025). Los datos que importan aquí:

- **87 %** de preferencia en el grupo de 18–24 años.
- **4×** más rápido el reconocimiento de elementos.
- **+34 %** de percepción de modernidad.
- **Reduce** la brecha de usabilidad por edad en vez de ampliarla.

Sus tres pilares, que son los que usa esta casa:

**a) Tipografía con énfasis.** Escala ampliada y un juego de estilos «emphasized»: mismo
tamaño, más peso. La jerarquía se marca con peso y tamaño, no con colores distintos.

**b) Movimiento con física.** Dos esquemas: *standard* y *expressive*. El expresivo
**sobrepasa ligeramente** su destino y vuelve —un rebote de muelle— y se reserva para
**momentos protagonistas**: elegir una pestaña, cambiar de estado. No para todo.

**c) Forma como lenguaje.** Escala de radios de **10 pasos** (de 0 a completamente redondeado)
y **35 formas nuevas**. Y una instrucción explícita que rompe con lo anterior: **crear tensión
visual combinando formas rectas y redondeadas en el mismo diseño.** Se acabó lo de que todo
tenga el mismo radio.

> Esto último es la clave contra el aspecto de plantilla: **la uniformidad de radio era
> precisamente la firma visual de la plantilla.**

---

# PARTE II · LAS CATORCE NORMAS

## N1 · El concepto va antes que los componentes

Antes de escribir una línea de interfaz, se escribe en una frase **qué idea visual tiene este
producto**. No «moderno y limpio»: una idea. («Es una herramienta de precisión: densa, oscura,
con los datos a la vista».) Esa idea decide tipografía, color, densidad y movimiento. Sin ella,
la interfaz se rellena con lo primero que aparece.

Y antes de comprometerse con la primera idea, **se plantean tres direcciones distintas** y se
comparan. La primera respuesta casi nunca es la buena; es la más común.

## N2 · Jerarquía antes que decoración

En cada pantalla, **una sola cosa** es lo primero que el ojo debe ver. Todo lo demás baja un
escalón. Si dos elementos pesan igual, uno sobra. La jerarquía se marca en este orden: tamaño
→ peso → posición → espacio → color. El color es el último recurso, no el primero.

## N3 · Los iconos se dibujan, no se escriben

- Prohibido el glifo de texto como icono. Se acabó.
- Cada icono es una **ruta vectorial** con el mismo grosor de trazo, las mismas esquinas
  redondeadas y el mismo tamaño óptico que sus hermanos.
- Regla de trazo que usa esta casa: `width = minDimension × 0.085`, `StrokeCap.Round`,
  `StrokeJoin.Round`.
- Set mínimo obligatorio: navegación (4–5), acción primaria, visto, aspa, guion, refrescar.
- Icono de lanzador: **adaptativo y vectorial**, con capa `monochrome` para Android 13+.

## N4 · Escala tipográfica de verdad

Mínimo **seis pasos**, y todos en uso:

| Rol | Tamaño | Peso | Uso |
|---|---|---|---|
| Etiqueta | 8–11 sp | Bold, `letterSpacing` 0,6–3 sp, MAYÚSCULAS | Rótulos de sección |
| Micro | 9–10 sp | Normal | Aclaración al pie de un dato |
| Cuerpo | 12–13 sp | Normal, `lineHeight` 1,45× | Texto corriente |
| Cuerpo fuerte | 13 sp | Medium | Nombres, filas de datos |
| Título | 17–19 sp | Semibold o Light | Cabecera de pantalla |
| Cifra / titular | 22–26 sp | Bold o Light | El número que importa |

Regla: si un párrafo y un titular se parecen en tamaño, el titular no está haciendo su trabajo.

## N5 · Espaciado en rejilla de 4 (preferible 8)

Todo margen, relleno y separación es múltiplo de 4: 4 · 8 · 12 · 16 · 18 · 20 · 24 · 32. Nada
de 13, 17, 22, 27. El ritmo se percibe aunque no se vea.

Densidad: mejor **densa y clara** que aireada y vacía. El aire sin contenido es relleno.

## N6 · Color con significado

- Un color **sólo** existe si comunica: verde = se puede, ámbar = cuidado, rojo = no se puede, y
  los de marca para identidad.
- Máximo **un** acento de marca por pantalla; el resto, neutros.
- Contraste **WCAG 2.2 AA**: 4,5:1 en texto normal, 3:1 en texto grande y en elementos de
  interfaz. Se mide, no se estima. El texto gris bajo es el fallo nº 1 de accesibilidad
  (83,9 % de las webs más visitadas).
- Prohibida la paleta «azul-violeta de degradado» por defecto. Si el producto no tiene una
  razón para violeta, no lleva violeta.

## N7 · Superficies y profundidad

- Tres niveles y no más: **fondo**, **contenido**, **flotante**.
- El vidrio es exclusivo del nivel flotante.
- Nunca vidrio sobre vidrio.
- La elevación se expresa con **tono**, no sólo con sombra: una capa más clara es una capa más
  alta.
- Radios **variados** dentro de la misma pantalla (contenedor grande, elemento interno
  pequeño). La uniformidad de radio es la firma de la plantilla.

## N8 · Movimiento con física, no con adornos

- Curva por defecto: **muelle** (`spring(dampingRatio = MediumBouncy, stiffness = MediumLow)`),
  no `ease-in-out`.
- Duraciones: 50–150 ms para lo inmediato, 200–400 ms para lo espacial. Nada de 600 ms
  «elegante»: eso es lentitud.
- El movimiento **explica** algo (de dónde viene, qué cambió) o no existe.
- **Respetar «reducir animaciones»** del sistema. No es opcional.

## N9 · Estados, todos, y diseñados

Cada componente interactivo necesita **seis** estados pensados: normal, pulsado, enfocado,
seleccionado, deshabilitado **explicado** y cargando.

Y cada lista necesita **cuatro** pantallas: con datos, vacía, cargando y con error.

El estado vacío dice **qué es esto**, **por qué está vacío** y **qué botón lo saca del vacío**.
«No hay datos» está prohibido.

## N10 · Botones por importancia

Tres tratamientos, siempre distinguibles: **primario** (color pleno), **secundario** (vidrio o
borde) y **destructivo** (rojo, con confirmación). Nunca tres botones iguales seguidos. Si hay
tres acciones igual de importantes, no se ha decidido cuál es la importante.

## N11 · Accesibilidad desde el principio, no al final

Es exactamente el error de Liquid Glass: dejarlo para el final es dejarlo sin arreglo.

- Objetivo táctil: **48 dp en Android**, **44 pt en iOS**, **mínimo absoluto 24 px** (WCAG
  2.5.8 AA). Se consigue con relleno, sin agrandar el dibujo.
- Todo icono con **etiqueta accesible**. Todo control operable sin gesto.
- Nada importante depende sólo del color (daltonismo): se añade forma, icono o texto.
- El texto escala al 200 % sin romper la maqueta.
- Prohibido el movimiento que no se puede desactivar.

## N12 · Datos: tabla, cifra o gráfico. Nunca un párrafo

Si el contenido son números comparables, el diseño es una **tabla** o un **número grande**, no
una lista de frases. Si es una tendencia, un gráfico. La prosa es para lo que es prosa.

## N13 · Una pantalla, un trabajo

Si una pantalla hace dos cosas, son dos pantallas. Y cuando se añade una función, **se fusiona
con la que ya existe** en vez de abrir una pestaña nueva al lado. Cinco destinos como máximo en
una barra inferior; si hay más, van a un segundo nivel.

## N14 · Nada de marca ajena

Se copia **estructura**, jamás marca, logotipos, iconos, fuentes con licencia ni recursos de
otro producto. La referencia se cita en el README y en `PROCEDENCIA.md`.

---

# PARTE III · EL MÉTODO (obligatorio, en este orden)

```
CONCEPTO → 3 DIRECCIONES → ELEGIR → COMPONER → REVISAR EN CRÍTICA → REFINAR
```

**1. Concepto.** Una frase. Qué se siente al usarlo y por qué encaja con *este* producto.

**2. Tres direcciones.** Tres propuestas distintas de verdad (no tres colores del mismo
diseño). Se comparan y se elige una. Se documenta por qué se descartaron las otras dos.

**3. Componer.** Aplicar N1–N14. Primero la jerarquía, después la rejilla, y el color al final.

**4. Revisar en crítica.** Pasar la lista de la Parte IV. Si algo falla, no se publica.

**5. Refinar.** Cada iteración quita algo o fusiona algo. Una iteración que sólo añade es
sospechosa.

---

# PARTE IV · LISTA DE CRÍTICA (antes de entregar)

Si una casilla falla, **no se entrega**.

- [ ] ¿Se distingue en una captura de pantalla de otras diez apps del mismo tipo?
- [ ] ¿Se ve en 1 segundo qué es lo más importante de la pantalla?
- [ ] ¿Todos los iconos están dibujados? ¿Ninguno es un carácter de texto?
- [ ] ¿Hay al menos seis tamaños de letra en uso y cada uno tiene un rol?
- [ ] ¿Todo el espaciado es múltiplo de 4?
- [ ] ¿El vidrio está sólo donde flota? ¿Hay vidrio sobre vidrio? (no debe)
- [ ] ¿Los radios varían, o todo tiene el mismo?
- [ ] ¿Cada color comunica algo? ¿Cuántos acentos de marca hay? (uno)
- [ ] ¿Contraste ≥ 4,5:1 medido, o estimado a ojo? (medido)
- [ ] ¿Hay movimiento con muelle en lo que se toca?
- [ ] ¿Se respeta «reducir animaciones»?
- [ ] ¿Existen los estados vacío, cargando y error de cada lista?
- [ ] ¿Los estados vacíos dicen qué hacer?
- [ ] ¿Los botones se distinguen por importancia?
- [ ] ¿Objetivos táctiles ≥ 48 dp?
- [ ] ¿Funciona a 200 % de escala de texto?
- [ ] ¿Cero emojis haciendo de icono?
- [ ] ¿Cero marca ajena?

---

# PARTE V · REFERENCIAS ACEPTADAS

| Sistema | Qué se toma | Qué NO se toma |
|---|---|---|
| **Material 3 Expressive** | Escala tipográfica con énfasis, movimiento con física, radios variados, tensión entre formas | Sus componentes tal cual, su paleta por defecto |
| **iOS 26 / Liquid Glass** | Que las superficies floten; la jerarquía por capas | El exceso de transparencia: **está documentado que rompe la legibilidad** |
| **ReDantotsu** | Barra inferior en píldora de cristal, muelle al seleccionar | Sus recursos |
| **GLTools original** | Estructura de pantallas: estado arriba, tiles grandes, configuración por pestañas | Su estética de 2016 y su deshonestidad («mejor modo posible») |
| **NN/g · WCAG 2.2** | Los mínimos medibles: contraste, tamaño de objetivo, foco | — |

---

# PARTE VI · CÓMO SE HACE CUMPLIR

Una norma que sólo vive en un documento no es una norma: es un deseo. Por eso:

1. **Está escrita** aquí, y en la skill `habilidades/diseno-ui/`.
2. **Está probada.** En GLTools Reborn hay **16 comprobaciones automáticas** que leen el código
   fuente y fallan si aparece un glifo, si la tipografía pierde la escala, si no hay muelle o si
   un estado vacío es un «No hay datos». Se demostró por sabotaje: se metió un `◆` a propósito y
   la suite falló señalando la línea.
3. **Está en la lista de cierre** de cada entrega: sin pasar la Parte IV, no hay release.

---

## Fuentes

- **Material 3 Expressive**: tres pilares (tipografía, movimiento, forma), 46 estudios con
  18.000 participantes, escala de 10 radios y 35 formas, instrucción de crear tensión visual
  ([Material 3](https://zoewave.medium.com/material-3-design-system-e91a15d303a0),
  [Compose M3 Expressive](https://zoewave.medium.com/compose-material-3-expressive-89f4147df5b8),
  [Expressive Design](https://www.skillsdirectory.com/skills/neversight-expressive-design),
  [Material Expressive 2026](https://www.sabaoon.dev/blog/material-expressive)).
- **Liquid Glass**: crítica de usabilidad y accesibilidad
  ([NN/g vía Superapp](https://superapp.dev/blog/how-to-design-a-liquid-glass-app-for-ios),
  [Design Bootcamp](https://medium.com/design-bootcamp/apples-biggest-ux-mistake-since-ios-7-db43d664de6d),
  [OSNews](https://www.osnews.com/story/143522/liquid-glass-is-cracked-and-usability-suffers-in-ios-26/)).
- **WCAG 2.2**: 4,5:1, objetivo 24 px mínimo / 44–48 recomendado, criterios nuevos
  ([FNATechnology](https://fnatechnology.com/blog/designing-for-accessibility-ui),
  [Accessible Metrics](https://www.accessiblemetrics.com/blog/wcag-2-2-deep-dive-what-changed-what-is-new-and-how-to-comply/),
  [Website Spec](https://specification.website/spec/accessibility/touch-target-size/)).
- **Anti-plantilla en interfaces generadas por IA**
  ([Anti-Slop Framework](https://moelkholy1995.medium.com/beyond-make-it-beautiful-the-anti-slop-framework-for-ai-frontend-craftsmanship-c99bbee6c994),
  [15 Mistakes](https://gendesigns.ai/blog/ai-generated-ui-mistakes-how-to-fix),
  [daily.dev](https://daily.dev/posts/how-to-apply-professional-design-principles-in-ai-app-development-3vfymoswz),
  [DESIGN.md](https://martecks.com/blog/why-ai-built-apps-look-generic/)).
