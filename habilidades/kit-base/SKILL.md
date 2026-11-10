---
name: kit-base
description: El código de partida de una app nueva —paleta, superficies, tipografía— ya conforme a las normas, para no volver a decidirlo cada vez.
---

# Kit base

## Cuándo se usa

Al empezar una app nueva, o al rehacer una pantalla que quedó con el lenguaje viejo. No es una
librería que se instala: es **código de referencia** que se copia y se adapta.

## Qué hay dentro

| Fichero | Qué es |
|---|---|
| `Tema.kt` | La paleta: fondo, tres niveles de superficie, un solo acento, un solo semáforo. |

## Procedimiento

1. Copiar `Tema.kt` al paquete `ui/` del producto nuevo.
2. No renombrar los colores: se llaman por su función (`superficie`, `superficieAlta`,
   `marca`, `verde`, `ambar`, `rojo`), no por su aspecto.
3. Comprobar con `tests/test_kit_diseno.py` que la paleta sigue sin alias ni degradados.

## Reglas que no se rompen

- **Un solo acento.** Si aparece un segundo color de marca, está mal.
- **Tres niveles de superficie**, ni dos ni cinco: `fondoArriba`, `superficie`, `superficieAlta`.
- Prohibidos los degradados de adorno y el vidrio dentro del contenido.
- Nada de violeta: es el color de plantilla por excelencia.

## Errores ya cometidos (no repetir)

- La ley de diseño de la 1.7.1 no tenía prueba para los degradados ni para el violeta, y en la
  1.8.1 aparecieron 18 usos de vidrio y 4 pantallas con degradado que llevaban tres versiones ahí.
  Por eso el kit tiene test propio.
- Se declararon alias de color (`violeta`, `cian`, `rosa`) «por compatibilidad»: era una puerta
  trasera a la paleta vieja. Se quitaron en `8f6e840` y el test ahora lo impide.

## Cómo se comprueba que se hizo bien

```bash
python3 -m unittest discover -s tests -p 'test_kit_diseno.py' -v
```
