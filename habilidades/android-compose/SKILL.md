---
name: android-compose
description: Construye pantallas en Jetpack Compose sin cerrar la app ni romper el rendimiento.
---

# Habilidad · Android con Jetpack Compose

## Cuándo se usa

Cualquier interfaz Android nativa de esta casa.

## Procedimiento

1. **Theme primero.** Color por rol + tipografía con escala + formas. Sin theme no hay
   consistencia, y sin consistencia todo parece plantilla.
2. **Una pantalla = un composable de nivel superior** que recibe **datos y callbacks**, nunca
   dependencias ocultas. Eso lo hace probable en JVM.
3. **La lógica va fuera del composable.** Navegación, estado del banner, filas de
   configuración: todo `object`/`data class` puros en un fichero aparte (`ui/Arquitectura.kt`).
   Motivo: aquí no hay teléfono para probar, así que lo que se pueda probar en JVM, se prueba.
4. **Estado con `remember` en el nivel correcto.** `remember` dentro de la lambda de contenido
   de un `LazyColumn` **no compila** (no es `@Composable`). Por eso el estado de pantalla vive
   en el composable de arriba.
5. **Listas:** un solo `LazyColumn` por pantalla. Dentro, `items(...)`, nunca otro `LazyColumn`.
6. **Iconos:** `Canvas` + `Path` + `Stroke`. Ver `ui/Iconos.kt`.
7. **Animación:** `animateFloatAsState` + `spring(dampingRatio = MediumBouncy,
   stiffness = MediumLow)`.
8. **Icono de lanzador:** `mipmap-anydpi-v26/ic_launcher.xml` adaptativo con
   `<monochrome>` (Android 13+), más `android:roundIcon` en el manifiesto.

## Reglas que no se rompen

- **Nunca `LazyColumn` anidado.** Cierra la app al medir. Si el composable se pinta dentro del
  scroll principal, usa `Column`.
- **Nunca `by lazy` para arreglar un orden de inicialización.** Lo que arregla un NPE de
  inicialización es declarar la propiedad **antes** y envolver en `try/catch`.
- **Nunca un `catch` que se trague el fallo en silencio**: se convierte en un resultado visible
  con el motivo (`proteger { }` en `MainActivity.kt`).
- `org.json` no existe en JVM: configuración aparte (`pruebasJson`), no `implementation`.
- Todo lo que pueda lanzar (shell, ficheros) va envuelto: una excepción no puede dejar la app
  en negro.

## Errores ya cometidos

1. **NPE al arrancar** por `prefs` inicializado después de `modo`. La app no abría. Se arregló
   con orden + `try/catch` y una prueba que lee el fichero real.
2. **`LazyColumn` dentro de `LazyColumn`** en la pantalla Configurar de la 1.7.0. Detectado
   antes de publicar; arreglado y **vigilado por prueba**.
3. **Refactor de bloques con llaves a mano** → estructura desalineada y media hora perdida.
   Ahora: contar llaves con `depth += l.count('{') - l.count('}')` antes de compilar.

## Cómo se comprueba

- `./gradlew :app:compileDebugKotlin` tras **cada** cambio estructural, no al final.
- `lintDebug` con 0 errores.
- Prueba sobre el fuente que prohíbe `LazyColumn(` en los composables que se pintan dentro de
  otro scroll.
