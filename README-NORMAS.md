# Cómo aplicar las normas a todos los proyectos

Las normas viven en `/home/user` (el espacio de trabajo) y son **universales**: no pertenecen a
GLTools Reborn, se aplican a cualquier proyecto presente o futuro.

## Qué hay en el espacio de trabajo

| Ruta | Qué es |
|---|---|
| `NORMAS-DE-DISENO.md` | La norma completa: diagnóstico, 14 normas, método, lista de crítica y fuentes. |
| `habilidades/` | Ocho habilidades con procedimiento, reglas y errores ya cometidos. |
| `habilidades/kit-base/` | Código listo para copiar: tema, iconos, movimiento, plantilla `DESIGN.md` y el bloque de pruebas que vigila la ley. |
| `REGLAS.md` | La versión corta (la que se copia dentro de cada repositorio de app). |
| `SKILLS.md` | El proceso de ingeniería destilado (compilar, publicar, probar, honestidad, limpieza). |

## Cómo se aplica a un proyecto nuevo (30 minutos)

1. **Copia** `REGLAS.md` a la raíz del repo y `NORMAS-DE-DISENO.md` a `docs/`.
2. **Rellena** `habilidades/kit-base/diseno.md` como `DESIGN.md`: concepto + tres direcciones.
   Sin esto no se escribe ni una pantalla.
3. **Copia el kit**: `Tema.kt`, `Iconos.kt`, `Movimiento.kt` a `ui/`, y el bloque de
   `prueba-diseno.kt` a `Pruebas.kt`.
4. **Pasa las pruebas antes de la primera pantalla.** Si el proyecto no es Android, copia la
   lógica de las pruebas (leer fuentes y buscar glifos) a su equivalente.

## Cómo se aplica a un proyecto que ya existe

1. **Auditoría**: pasa la Parte IV de `NORMAS-DE-DISENO.md` sobre cada pantalla. Anota los
   fallos, no los arregles todavía.
2. **Arregla en este orden**: glifos → jerarquía → espaciado → superficies → color → movimiento →
   estados. El orden importa: arreglar el color antes de la jerarquía es pintar una casa sin
   plano.
3. **Añade el bloque de pruebas al mismo tiempo** que arreglas, para que no vuelva a entrar.
4. **Una iteración quita o fusiona**, no sólo añade.

## Estado por proyecto

| Proyecto | Norma aplicada | Pruebas de diseño |
|---|---|---|
| **GLTools Reborn** (Android) | Sí, 1.7.1 | 20 comprobaciones automáticas + sabotaje verificado |
| Cualquier proyecto nuevo | Obligatorio desde el primer commit | Copiar el bloque del kit |

## La regla, otra vez, porque es la que importa

> **Prohibido que parezca HTML, plantilla o panel genérico.** Y cuando no haya diseño propio a
> la altura: **se copia la estructura** de una app que sí funciona y **se refina** —arreglando
> sus errores, quitando lo que sobra, fusionando funciones—. Nunca se justifica con «es que es
> lo que hay».

## Reglas de operación y procedimientos

- **[REGLAS-OBLIGATORIAS.md](REGLAS-OBLIGATORIAS.md)** — las nueve reglas de cómo se trabaja:
  limpiar en cada turno, subir la versión en los tres sitios, publicar y verificar en el mismo
  turno, una incidencia por pendiente, ninguna afirmación sin prueba.
- **[procedimientos/](procedimientos/)** — los cinco scripts que hacen todo eso, ejecutables:
  1. `01-censar-catalogo-appteka.py` — censar las 42 categorías de Appteka con el filtro de
     código abierto (**36.540 apps**, ejecutado y verificado).
  2. `02-elegir-y-desmontar.sh` — bajar y desmontar las apps de las que aprender.
  3. `03-cerrar-tramo.sh` — probar, firmar, publicar, verificar y limpiar, en ese orden.
  4. `04-incidencias.sh` — abrir una incidencia por cada pendiente, sin duplicarlas.
  5. `05-diseno-imitar-y-mejorar.md` — de una pantalla fea a una que no lo es, fase por fase.
