// ══════════════════════════════════════════════════════════════════════════════
//  BLOQUE DE PRUEBAS: «LEY DE DISEÑO»
//
//  Pega esto dentro del `main()` de tu `Pruebas.kt`, antes del resumen final. Ajusta
//  `uiDir` a la carpeta de interfaz de tu proyecto.
//
//  Qué hace: lee el código fuente y comprueba que la interfaz no parece HTML. No es
//  instrumentación ni snapshot testing: es prueba estática, y funciona. Se verificó por
//  sabotaje — metiendo un `◆` a propósito, la suite falla señalando la línea.
//
//  Cada comprobación corresponde a una norma de NORMAS-DE-DISENO.md.
// ══════════════════════════════════════════════════════════════════════════════

println()
println("── ley de diseño: prohibido parecer HTML ──")

val uiDir = listOf(
    "app/src/main/java/io/github/labandita/glreborn/ui",
    "src/main/java/io/github/labandita/glreborn/ui",
).map { java.io.File(it) }.firstOrNull { it.isDirectory }

if (uiDir == null) {
    check("la carpeta de interfaz existe para poder vigilarla", false)
} else {
    val fuentes = uiDir.listFiles { f -> f.extension == "kt" }!!.sortedBy { it.name }
    check("hay ficheros de interfaz que revisar", fuentes.size >= 5, "${fuentes.size}")

    // ── N3. Ningún icono es un carácter de texto ───────────────────────────
    // Se busca SÓLO dentro de literales de cadena: un carácter suelto dibujado como
    // texto es lo que delata a una página web.
    val glifosProhibidos = listOf(
        "◇", "◆", "✦", "✧", "▣", "▤", "◉", "◈", "◐", "▲", "●", "■", "□",
        "↻", "✓", "✗", "×", "★", "☆", "➤", "≡", "⌂", "⚡",
    )
    val glifosEncontrados = mutableListOf<String>()
    fuentes.forEach { f ->
        f.readLines().forEachIndexed { n, linea ->
            val limpia = linea.substringBefore("//")   // en un comentario se puede hablar de glifos
            if (!limpia.contains('"')) return@forEachIndexed
            glifosProhibidos.forEach { g ->
                if (limpia.contains(g)) glifosEncontrados += "${f.name}:${n + 1} «$g»"
            }
        }
    }
    check(
        "ningún icono es un carácter de texto (eso es lo que parece HTML)",
        glifosEncontrados.isEmpty(),
        glifosEncontrados.joinToString(" | "),
    )

    // ── N3. Los iconos están dibujados ─────────────────────────────────────
    val iconos = fuentes.firstOrNull { it.name == "Iconos.kt" }
    check("existe Iconos.kt", iconos != null)
    if (iconos != null) {
        val txt = iconos.readText()
        val cuantos = Regex("fun [A-Z][A-Za-z]+\\(").findAll(txt).count()
        check("hay al menos 8 iconos dibujados", cuantos >= 8, "$cuantos")
        check("se dibujan con Path", txt.contains("Path()"))
        check("con trazo uniforme", txt.contains("Stroke("))
        check(
            "y esquinas redondeadas de verdad",
            txt.contains("StrokeCap.Round") && txt.contains("StrokeJoin.Round"),
        )
    }

    val todos = fuentes.joinToString("\n") { it.readText() }

    // ── N4. Jerarquía tipográfica ──────────────────────────────────────────
    val tamanos = Regex("fontSize\\s*=\\s*([0-9.]+)\\.sp")
        .findAll(todos).map { it.groupValues[1].toFloat() }.toSet()
    check("la tipografía tiene escala, no un solo tamaño", tamanos.size >= 6,
        tamanos.sorted().toString())
    check("hay titulares grandes (≥18sp)", tamanos.any { it >= 18f })
    check("y etiquetas pequeñas (≤11sp)", tamanos.any { it <= 11f })

    // ── N8. Movimiento con física ──────────────────────────────────────────
    check(
        "hay animación con física, no todo aparece de golpe",
        todos.contains("spring(") && todos.contains("animateFloatAsState"),
    )
    check("el muelle usa damping (no es linear disfrazado)", todos.contains("DampingRatio"))

    // ── N7. El vidrio es acento, no la única superficie ────────────────────
    val principal = fuentes.maxByOrNull { it.length() }
    if (principal != null) {
        val txt = principal.readText()
        val vidrios = Regex("\\.vidrio(Alto)?\\(").findAll(txt).count()
        val textos = Regex("\\bText\\(").findAll(txt).count()
        check("el cristal se usa como acento y no como única superficie",
            vidrios < textos, "vidrio=$vidrios texto=$textos")
    }

    // ── N9. Estados vacíos diseñados ───────────────────────────────────────
    val vacios = Regex("\"[^\"]{0,4}(No hay|Sin datos|Vacío|vacio)[^\"]{0,20}\"")
        .findAll(todos).count()
    check("ningún estado vacío es un «No hay datos» pelado", vacios == 0, "$vacios")

    // ── N10. Botones con importancia ───────────────────────────────────────
    check("existen al menos tres tratamientos de botón",
        todos.contains("Boton(") && todos.contains("BotonHome(") &&
            todos.contains("BotonPlano("))

    // ── Prohibición de emojis como iconos ──────────────────────────────────
    val emojis = Regex("[\\uD83C-\\uDBFF][\\uDC00-\\uDFFF]").findAll(todos).count()
    check("ningún emoji hace de icono", emojis == 0, "$emojis")
}
