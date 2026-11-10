---
name: pruebas-sin-dispositivo
description: Probar una app Android cuando no hay teléfono ni emulador, incluida la vigilancia de reglas de diseño.
---

# Habilidad · Probar sin dispositivo

## Cuándo se usa

Siempre que no haya dispositivo conectado ni `/dev/kvm` (el caso normal en este entorno).

## Procedimiento

1. **Separa lo puro.** Toda decisión (navegación, estado, configuración, cálculos) va a
   ficheros sin `@Composable` ni `Context`. Se convierte en `object` con funciones que devuelven
   datos.
2. **Tarea `JavaExec` propia** en `build.gradle`, para no depender de emulador:

```groovy
configurations { pruebasJson }
dependencies { pruebasJson 'org.json:json:20240303' }
tasks.register('pruebasNucleo', JavaExec) {
    classpath = sourceSets.test.runtimeClasspath +
        configurations.debugRuntimeClasspath + configurations.pruebasJson
    mainClass = 'PruebasKt'
}
```

3. **`check(nombre, condición, detalle)`** con salida legible y código de salida ≠ 0 si falla.
   Formato `[ok] / [FALLO]` con el detalle para depurar.
4. **Pruebas que leen el código fuente.** Es la única forma de vigilar una regla de diseño sin
   instrumentación: prohibir `LazyColumn` anidado, exigir iconos con `Path`, prohibir glifos.
   No es trampa: es prueba estática y funciona.
5. **Sabotea.** Rompe algo a propósito, comprueba que la prueba **falla**, restaura. Si nunca
   falla, no prueba nada.

## Reglas que no se rompen

- El número de comprobaciones **nunca baja** entre tramos.
- Toda prueba nueva trae su mensaje de fallo con el dato concreto.
- Nada de `org.json` como `implementation`: sólo en la configuración de pruebas.
- Una prueba que mide el resultado **no** puede leer la caché de la propia función: tiene que
  leer el fichero real (así se detectó el NPE).

## Errores ya cometidos

- **Afirmar que `by lazy` arregla un NPE.** No lo arregla: lo que lo arregla es el orden de
  declaración + `try/catch`. La prueba se reescribió para decir la verdad.
- Meter `org.json` en `implementation` y romper las pruebas en JVM.
- Tener pruebas que sólo comprobaban el caso feliz: el fallo real (no aplicar y decir
  «aplicado») no estaba cubierto hasta que se añadió.

## Cómo se comprueba

`./gradlew :app:pruebasNucleo` → todas `[ok]`. Estado actual de GLTools Reborn: **283**.
