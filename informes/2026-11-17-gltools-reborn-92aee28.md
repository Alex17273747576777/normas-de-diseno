# Auditoría de diseño · gltools-reborn

| | |
|---|---|
| Fecha (UTC) | `2026-11-17T11:22:04Z` |
| Repositorio | `/var/tmp/propios/gltools-reborn` |
| Remoto | `https://github.com/Alex17273747576777/gltools-reborn.git` |
| Rama | `main` |
| Commit auditado | `92aee286527116ff8c8e9fb17855d39095e7bf9e` |
| Cambios sin commitear | `0` |
| Auditor | `auditar_diseno_generico.py` sha256:`6625334b39e5193a` |
| Modo | `normal` |
| Código de salida | `0` |

## Salida íntegra del auditor

```
AUDITORÍA DE DISEÑO · gltools-reborn
  59 ficheros Kotlin de producto · 15 colores declarados con Color(0xAARRGGBB)
  rango de matiz prohibido 246-341°, derivado de REGLAS.md: #7C4DFF=255.8°, #6C5CE7=246.9°, #A855F7=270.7°

AVISOS (1) — no cortan, salvo con --estricto:
  ! R14b superficie sobre el lienzo: `superficie` sobre `fondoMedio` se queda en 1.06:1, por debajo del paso más sutil que Material 3 acepta entre niveles (1.08:1). Si `fondoMedio` es el contenedor de una hoja, un diálogo o una barra que flota, las cajas `superficie` de dentro pueden perder su límite. Hace falta verlo en pantalla para saber si se pierde: incidencia #6.

NO SE PUEDE MEDIR (6) — declarado, no escondido:
  · R9/R10 alcance: sólo se juzgan los 14 ficheros de interfaz (importan androidx.compose o llevan @Composable). Un ⛔ o un ✓ en un informe de texto que se guarda en un fichero o se registra no es un icono de interfaz y la ley no lo prohíbe: en GLTools hay seis, en core/, y están bien donde están.
  · El tacto y el ritmo: si la interfaz se siente bien exige pantalla encendida.
  · Si un elemento pequeño se ve de verdad (un chevrón de 14 dp, un rótulo de 9,5 sp): exige captura real, no texto.
  · Si una fila se corta en un ancho concreto: exige medir el texto renderizado.
  · El número exacto de cajas visibles por pantalla: aquí se cuentan usos en el texto, no la composición real. Un `if` puede no ejecutarse nunca.
  · Si los botones primario/secundario/destructivo se distinguen: se puede medir el color, no la percepción de peso.

RESULTADO: SIN INCUMPLIMIENTOS
```

## Cómo repetir esta auditoría

```bash
git -C "/var/tmp/propios/gltools-reborn" checkout 92aee286527116ff8c8e9fb17855d39095e7bf9e
python3 procedimientos/auditar_diseno_generico.py "/var/tmp/propios/gltools-reborn"
```

Si el commit ya no está (reescritura de historia, clon superficial), este informe no se puede
reproducir: ésa es la razón de anotar el SHA y no sólo la fecha.
