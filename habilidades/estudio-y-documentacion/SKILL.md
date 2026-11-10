---
name: estudio-y-documentacion
description: Cómo estudiar documentación ajena antes de programar una app —qué se copia, qué no, cómo se cita y cómo se convierte en una decisión de diseño—. Se usa al empezar un tramo y al revisar por qué la app se comporta así.
---

# Habilidad · Estudiar antes de programar

> Nació de una petición literal: *«ponte a estudiar para cumplir las expectativas de mis futuros
> usuarios»*. Estudiar, aquí, no es juntar libros: es poder decir **por qué** esta app hace lo
> que hace y de dónde sale esa razón.

## Cuándo se usa

- Antes de escribir una pantalla o un algoritmo nuevo, si ya existe alguien que lo explicó.
- Cuando el usuario pide «aplicación real y profunda» y hay que justificar cada decisión.
- Al revisar un fallo: casi siempre hay un texto que dice qué no se debía haber hecho.

## Procedimiento (en orden)

1. **Buscar la fuente primaria.** Documentación oficial, especificación, RFC, guía del autor de la
   tecnología. Si no hay fuente primaria, se dice que sólo hay secundarias.
2. **Comprobar que se puede usar.** Licencia del texto (MIT, CC-BY, CC-BY-SA, GPL, Apache) y, si es
   código, su licencia. **GPL y CC-BY-SA se contagian**: leerlas y reescribir está bien; copiar
   trozos a un proyecto con otra licencia, no.
3. **Copiar sólo el texto** (`.md`, `.rst`, `.txt`, `.ipynb`, `.tex`), nunca imágenes, vídeo ni
   binarios, y guardar al lado **fuente, autor, licencia, commit y fecha** (`PROCEDENCIA.md`).
4. **Estudiar en tres pasadas:** (a) índice y glosario —qué vocabulario usa—; (b) el capítulo que
   responde a la pregunta de hoy; (c) los «errores comunes» y «anti-patrones».
5. **Escribir la conclusión en la app**, no en un cajón: una línea en `docs/`, una prueba que la
   fije y, si toca diseño, una entrada en `NORMAS-DE-DISENO.md`.
6. **Marcar lo que no se entendió.** «Leído y no aplicado» es un estado legítimo; «aplicado» sin
   relectura no lo es.

## Reglas que no se rompen

1. **Nada de texto ajeno dentro del APK** salvo citas cortas con su fuente; el conocimiento se
   convierte en decisiones y en pruebas, no en un anexo.
2. **Sin licencia clara, no se copia.** ¿Que el repositorio no declara licencia? Se lee desde el
   enlace y se anota «sin licencia: sólo consulta», no entra en el espacio de trabajo.
3. **Copiar estructura, no recursos.** Vale aprender cómo organiza Google su guía de estilo; no
   vale llevarse sus iconos, sus capturas ni sus ficheros de diseño.
4. **Una fuente no es una verdad.** Dos fuentes que se contradicen se anotan las dos, con la
   discrepancia escrita.

## Diseño gráfico: lo que se estudia y lo que se decide

De las guías de diseño (Material, Apple HIG, guías de tipografía y color, sistemas de diseño
abiertos) se aprende **método**, y el método se traduce a decisiones ya tomadas en
`NORMAS-DE-DISENO.md` y `sistema-de-superficie.md`:

- **Jerarquía antes que decoración**: un solo elemento manda por pantalla; el resto se subordina
  por tamaño, color y espacio, no por sombras.
- **Escala tipográfica fija** (una razón, no tamaños sueltos) y como mucho **dos familias**.
- **Contraste mínimo 4,5:1** para texto normal y **3:1** para texto grande: es medida, no opinión.
- **Espacio en múltiplos de 4**; la densidad se ajusta con el espacio, no bajando el tamaño.
- **Color con significado estable**: un color no cambia de sentido entre pantallas.
- **Estados, no adornos**: pulsado, deshabilitado, cargando y error se diseñan antes que el estado
  bonito.
- **Nada de degradados «porque sí»**. En esta app hay un único acento y el degradado tiene
  funciones contadas (profundidad de superficie, no llamar la atención).

## Multi-idioma: lo que se estudia y lo que se decide

- **El texto no se concatena**: se usan plantillas con huecos (`%1$s`), porque el orden de las
  palabras cambia entre idiomas y concatenar produce frases rotas.
- **Plurales con reglas del idioma**, no con `if (n == 1)`.
- **Fechas, números y unidades** por configuración regional; los GB no se escriben igual en todas
  partes.
- **Longitud elástica**: el alemán ocupa ~30 % más que el inglés; ningún botón se dimensiona por el
  texto en un idioma concreto.
- **Nada de traducir identificadores**: las claves de recurso no llevan texto visible.

## Errores ya cometidos (no repetir)

- **Clonar repositorios enteros en `/tmp`.** En este entorno `/tmp` es una RAM de 992 MB: el clon
  la llenó, tumbó la importación de datos que corría a la vez y dejó 12 repositorios sin bajar. Se
  clona en el disco grande, en modo disperso y filtrando por extensión.
- **Dar por hecho que un índice de enlaces contiene los libros.** No los contiene: enlaza a
  repositorios, y lo que se puede copiar es el texto de esos repositorios.
- **Confundir «descargado» con «estudiado».** Un gigabyte de Markdown sin una sola decisión escrita
  no es conocimiento; es peso.

## Cómo se comprueba que se hizo bien

- Cada repositorio copiado tiene su `PROCEDENCIA.md` con commit, licencia y fecha.
- `_registro.json` dice cuántos ficheros y cuántos bytes, y **qué falló y por qué**.
- Cada tramo de trabajo cita al menos un documento estudiado y la decisión que provocó.
- Si una norma de diseño se cambió, se cambió con la razón escrita al lado.
