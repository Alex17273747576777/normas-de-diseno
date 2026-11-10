---
name: limpieza-y-cierre
description: Cerrar un tramo de trabajo sin dejar temporales, clones ni versiones viejas en el espacio de trabajo.
---

# Habilidad · Limpieza y cierre

## Cuándo se usa

Al terminar cada entrega. **Después** de verificar, nunca antes.

## Procedimiento

1. Verificar todo (release descargada, sumas, firma, código nuevo dentro).
2. Borrar el clon y los temporales:

```bash
rm -rf /tmp/proy /tmp/verif /tmp/scrape /tmp/t5 /tmp/w_*.html /tmp/top500.* /tmp/devices* \
       /tmp/mob_* /tmp/ax_*.html /tmp/sitemap-*.xml /tmp/s.txt /tmp/b*.txt
```

3. Dejar en `/home/user` **sólo** lo que sirve: claves (`.firma`, `.gh-tokens`), `uploads/`,
   `bd/`, `trabajo/`, las normas y habilidades, y **la página de la versión vigente**.
4. Borrar las páginas de versiones anteriores: sólo se conserva la última.
5. Comprobar el peso de `/tmp` (`du -sh /tmp`) y que no queden ficheros huérfanos.

## Reglas que no se rompen

- **No se borra antes de verificar.** Borrar el clon antes de terminar las comprobaciones obliga
  a clonar otra vez.
- **No se borran** `.firma/`, `.gh-tokens`, `uploads/`, `bd/`, `trabajo/`, `NORMAS-DE-DISENO.md`,
  `habilidades/`.
- Lo que se borra de `/tmp` **no se recupera**: si algo hay que conservar, va a `/home/user`
  antes.

## Errores ya cometidos

- Borrar la caché de rastreo antes de tener el JSON reconstruido → hubo que rastrear de nuevo
  (623 MB de HTML perdidos).
- Acumular cuatro páginas HTML de versiones viejas en `/home/user`. Se limpian.

## Cómo se comprueba

`ls -la /home/user` no muestra nada que no esté en la lista permitida, y `/tmp` vuelve a su
peso de reposo (~310 MB).
