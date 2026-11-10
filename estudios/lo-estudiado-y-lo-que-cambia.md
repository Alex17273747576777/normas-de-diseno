# Lo estudiado, y qué cambia en nuestras apps

> No es una bibliografía. Es la lista de cosas que **ya se leyeron** y la decisión concreta que
> cada una provocó. Si algo de aquí no está aplicado, se dice: «leído y no aplicado».
>
> De dónde sale el material: `conocimiento/INDICE.md` (72 repositorios, cada uno con su commit y su
> licencia). Las fuentes se citan por repositorio, no por página: el texto está en el espacio de
> trabajo y se puede volver a él.

## 1. Diseño de software: lo que manda cuando hay prisa

**Fuentes:** `ashishps1/awesome-low-level-design` (GPL-3.0),
`donnemartin/system-design-primer` (CC-BY-4.0),
`kamranahmedse/design-patterns-for-humans` (CC-BY-4.0),
`charlax/professional-programming` (MIT).

> **Licencias, comprobadas fichero a fichero** (no con el campo de la API, que aquí devolvía
> `NOASSERTION`): `awesome-low-level-design` es **GPL-3.0**,
> `system-design-primer` y `design-patterns-for-humans` son **CC-BY-4.0**
> y `professional-programming` es **MIT**. Consecuencia: de la
> primera no se reescribe código ni texto dentro de la app; de las demás se puede reescribir el
> criterio citando al autor.

Lo que se extrae, en orden de utilidad para nosotros:

1. **DRY, KISS y YAGNI aparecen antes que SOLID**, y en ese orden. YAGNI es el que más nos toca:
   no construir «el modo que un día hará falta». Un botón que no hace nada hoy es deuda, no futuro.
2. **Los axiomas de Urbit** que recoge `professional-programming` y que suscribo uno a uno:
   - *«Data is better than code»* → preferir un JSON con su fuente y su fecha antes que código que
     calcule el dato. Es exactamente lo que hacemos con `mobolist.json` y `manifiesto.json`.
   - *«Correctness is more important than performance»* → primero que diga la verdad, después que
     vaya rápido. Un dato vacío es correcto; un dato inventado es rápido y falso.
   - *«Deterministic beats heuristic»* → si se puede leer el estado real (`/proc`, `dumpsys`), no se
     estima.
   - *«One hundred lines of simplicity is better than twenty lines of complexity»* → el lector de
     JSON propio (`MiniJson.kt`) es más largo que una librería y aun así se justifica: no hay
     dependencia y se prueba entero.
   - *«If you don't understand a system you're using, you don't control it»* → de aquí sale la
     manía de releer lo escrito en vez de suponerlo.
3. **Condiciones de carrera y secciones críticas** (`awesome-low-level-design`: mutex, semáforos,
   CAS, deadlock, productor-consumidor). En una app de diagnóstico hay estado compartido por
   hilos: el hilo que mide y el que pinta. La regla que se adopta: **la medición escribe en un
   único sitio y la pantalla sólo lee**; nada de dos hilos tocando la misma lista.
4. **Código que se puede revisar**: `professional-programming` insiste en *code reviews*,
   *refactoring* y *documentation* como disciplina, no como ceremonia. Traducido: cada tramo
   termina con el «por qué» escrito en `docs/` y con la prueba que lo fija.

## 2. Rendimiento: números, no intuiciones

**Fuente:** `donnemartin/system-design-primer` (CC-BY-4.0), tabla
*«Latency numbers every programmer should know»*. Los números se citan porque son medidas; el resto
del repositorio se leyó como criterio.

| Operación | Coste | Lo que implica en Android |
|---|---|---|
| Referencia a L1 / L2 | 0,5 ns / 7 ns | Recorrer una lista en memoria es gratis comparado con tocar disco. |
| Bloqueo de mutex | 25 ns | Sincronizar no es el problema; abusar de ello, sí. |
| Memoria principal | 100 ns | Un `Map` de 54.434 entradas vive bien en RAM. |
| Leer 4 KB al azar de SSD | 150 µs | **Un fichero pequeño leído mil veces cuesta más que uno grande leído una vez.** |
| Leer 1 MB secuencial de SSD | 1 ms | Leer `mobolist.json` (2 MB) una vez ≈ 2 ms: aceptable **fuera del hilo de pintado**. |
| Ida y vuelta en el mismo centro de datos | 0,5 ms | Una llamada a red local es más lenta que leer el catálogo entero. |

Decisiones que ya están tomadas por esto:

- Los datos del APK se leen **una vez** y en `Dispatchers.IO` (está en `MainActivity`), nunca en el
  hilo de pintado: 15 MB en el hilo principal son un ANR, no una lentitud.
- **Una lectura por sesión**, no una por búsqueda. Buscar es recorrer una lista en memoria (100 ns
  por elemento), no volver a abrir el fichero (milisegundos).
- Cuando el catálogo crezca (3.500 fichas), **filtrar en memoria** sigue siendo más barato que
  cualquier caché intermedia.

## 3. Que la app diga la verdad: lo que ya estaba y ahora está fundado

**Fuentes:** `bregman-arie/devops-exercises` (CC-BY-NC-ND) y
`MichaelCade/90DaysOfDevOps` (CC-BY-NC-SA). Las dos son **no comerciales**, y la
primera además **sin obras derivadas**:
se estudia el método de autoevaluación, no se copian sus preguntas.

- El sistema operativo **expone su estado** (procesos, memoria, ficheros): si algo se puede leer,
  se lee; no se estima. De ahí la regla de que un umbral se lea **después** de aplicarlo.
- **Observabilidad**: registro y manejo de excepciones no son extras. Nuestro `RegistroFallos` y el
  informe `.md` al cerrar son exactamente eso; el estudio confirma el criterio: **un fallo sin
  contexto (dispositivo, versión, comando, salida) no es un informe, es una queja.**
- **Autoevaluación**: los «self assessment» de `devops-exercises` son preguntas con respuesta. La
  versión para nosotros son las pruebas de `Pruebas.kt`: cada ley es una pregunta con respuesta
  comprobable.

## 4. Lenguaje y estilo: Kotlin con criterio

**Fuentes:** `isocpp/CppCoreGuidelines` (sin identificar),
`realpython/python-guide` (CC-BY-NC-SA),
`inancgumus/learngo` (CC-BY-NC-SA), `getify/You-Dont-Know-JS`
(CC-BY-NC-ND — **NC-ND**, sólo criterio).

> Aquí se vio el error: `You-Dont-Know-JS` es **CC-BY-NC-ND** (no comercial y sin
> obras derivadas) y `python-guide` es **CC-BY-NC-SA**. Citarlas como «MIT» habría
> sido falso, y una licencia mal citada en un documento de normas es peor que no citarla.

- **Los valores nulos y los tipos son el primer control de calidad.** Kotlin ya obliga; la regla
  que se adopta es no usar `!!` fuera de código de arranque probado.
- **`CppCoreGuidelines` dice algo que sirve en cualquier lenguaje**: una regla que no se puede
  comprobar automáticamente es un deseo. De ahí que toda norma nuestra acabe en el auditor o en una
  prueba.
- **Un fallo silencioso es peor que una excepción**: `runCatching { }.getOrDefault(emptyList())`
  convierte un JSON roto en «no hay datos», y eso se ve como app vacía en vez de como error. Donde
  ya está, se acompaña de un aviso en pantalla; donde se pueda, se propaga.

## 5. Diseño gráfico: la lista corta que de verdad se aplica

**Fuentes:** `sadanandpai/frontend-learning-kit` (MIT),
`charlax/professional-programming` (MIT, sección de *frontend*) y
`kamranahmedse/developer-roadmap` (sin identificar).

Reglas adoptadas (y ya escritas en `habilidades/estudio-y-documentacion/SKILL.md`):

- **Jerarquía antes que decoración**; un solo elemento manda por pantalla.
- **Escala tipográfica con una razón fija**; dos familias como máximo.
- **Contraste mínimo 4,5:1** para texto normal, 3:1 para texto grande: se mide, no se opina.
- **Espacio en múltiplos de 4**; la densidad se ajusta con espacio, no bajando el tamaño.
- **Estados diseñados antes que el estado bonito**: pulsado, deshabilitado, cargando, error.
- **El color no cambia de significado** entre pantallas.

Lo que **no** se copia, dicho claro: ni paletas, ni iconos, ni capturas, ni «inspiración» que acabe
siendo la misma pantalla con otro nombre.

## 6. Multi-idioma: cuatro reglas que evitan frases rotas

- Plantillas con huecos (`%1$s`), **nunca concatenar**.
- Plurales con la regla del idioma, no con `if (n == 1)`.
- Fechas, números y unidades según la configuración regional.
- Ningún control se dimensiona por el texto del idioma más corto (el alemán ocupa ~30 % más).

## 7. Lo leído y **no** aplicado (para no fingir)

- **Diseño de sistemas a gran escala** (colas, cachés distribuidas, *sharding*): leído; esta app es
  un proceso en un teléfono, no un servicio. Se aplica el criterio, no la infraestructura.
- **Concurrencia avanzada** (bloom filters concurrentes, HashMap concurrente): leído; no hay caso de
  uso todavía. YAGNI manda.
- **El curso de LLM y los cuadernos de ML**: material disponible; hoy no hay ninguna función de la
  app que lo necesite.

## Cómo se comprueba que esto no es palabrería

1. Cada decisión de arriba tiene su reflejo en código o en una prueba concreta (`Pruebas.kt`,
   `RegistroFallos`, la carga en `Dispatchers.IO`).
2. La habilidad `estudio-y-documentacion` recoge el procedimiento y los errores ya cometidos.
3. `conocimiento/INDICE.md` dice qué hay, de quién es y con qué licencia; `_registro.json` dice el
   commit exacto de cada copia.
4. Si una afirmación de este documento deja de ser cierta, **se borra** en vez de maquillarse.

## 8. El error que este documento tuvo, y cómo se corrigió

Al escribirlo la primera vez puse licencias «de memoria» para siete repositorios. Al comprobar los
ficheros reales, **varias atribuciones eran falsas**. Y en el primer intento de corrección volví a
fallar de otra forma: un programa que buscaba la palabra «MIT» en cualquier parte del README
encontraba la licencia de un proyecto **enlazado**, no la del repositorio, y atribuyó MIT a sitios
que en realidad son **CC-BY-NC-ND**.

La corrección definitiva tiene tres reglas:

1. Se lee el fichero `LICENSE`/`COPYING`/`UNLICENSE` copiado; sólo si no existe se mira el README, y
   **sólo en su apartado de licencia**, no en todo el texto.
2. Cada licencia guarda **la prueba**: el fichero y el fragmento de texto que la identifica
   (`licencia_prueba` en `conocimiento/_registro.json`). Si no hay prueba, es `sin identificar`.
3. Las que no se identifican (**19 de 72**) quedan en **sólo consulta**: se leen,
   no se copian.

Resultado comprobado hoy: **25 MIT · 7 CC-BY-NC-SA · 5 CC-BY-NC-ND · 5 CC0 · 3 CC-BY-4.0 · 3 CC-BY-SA · 3 GPL-3.0 · 2 Apache-2.0**.

**Lección, que va a `honestidad-tecnica`:** una licencia es un dato, y los datos se leen del
original y se citan con su prueba. «Creo que era CC-BY» no es una licencia: es una suposición con
consecuencias legales. Y si un programa automático decide licencias, hay que poder enseñar **por
qué** decidió cada una.
