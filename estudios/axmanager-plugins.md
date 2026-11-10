# AX Manager · plugins sin root: qué es verdad y qué no

Revisión del 10-11-2026 contra la documentación oficial
([qué es un plugin](https://axmanager.app/plugin/what-is-plugin.html) y
[entorno y rutas](https://axmanager.app/plugin/environment.html)).

**Para qué sirve este documento:** llegó una propuesta de análisis de AX Manager con una
arquitectura descrita de memoria. Varias piezas no existen. Si se implementa lo que decía, no
compila, no arranca o miente sobre lo que puede hacer. Aquí está lo que dice la fuente, con la
cita al lado, y lo que se puede construir de verdad encima.

## Lo que es

Un **plugin** de AxManager es una carpeta con `module.prop` dentro de `$AXERONDIR/plugins/`. Es
el mismo formato que un módulo de Magisk, pero ejecutado por AxManager **sin root** en el modo
*Shell* (el servidor arrancado por ADB o «Start as Shell»), donde corre como `com.android.shell`.

Los dos modos tienen carpeta propia y **plugins separados**:

| Modo | `$AXERONDIR` | Quién eres |
|---|---|---|
| Root | `/data/adb/axeron` | root |
| Shell (sin root) | `/data/user_de/0/com.android.shell/axeron` | `com.android.shell` |

Regla dura: **usar siempre `$AXERONDIR`**, nunca escribir ninguna de las dos rutas a mano.

## Correcciones a la propuesta

| Lo que decía la propuesta | Lo que dice la documentación |
|---|---|
| «Configuración en JSON o YAML» | `module.prop` es **clave=valor**, una línea por campo. Campos: `id`, `name`, `version`, `versionCode`, `author`, `description` y **`axeronPlugin` (obligatorio, numérico)**. Sin `axeronPlugin` el plugin se rechaza. `id` tiene que casar con `^[a-zA-Z][a-zA-Z0-9._-]+$`. Fin de línea **LF**, nunca CRLF. |
| «Scripts en Bash o Python» | Todo corre en **BusyBox `ash`** con *Standalone Shell Mode*: cada comando usa el applet interno de BusyBox, no el del sistema. **Python no está garantizado**: un plugin que lo necesite no es un plugin de AxManager. |
| «Manifiesto XML/JSON con permisos», «`apply_permissions()`» | **No existe.** Un plugin no es una app: no tiene `AndroidManifest.xml`, ni permisos de Android que conceder, ni `apply_permissions()`. Lo que puede hacer es lo que puede hacer `com.android.shell` en ese teléfono. |
| «`init_module()`, `onLoad()`, `onUnload()`, `entrypoint.sh`» | No existen. Los puntos de entrada reales son `customize.sh` (instalación), `post-fs-data.sh`, `service.sh`, `uninstall.sh`, `action.sh` (botón Acción), `system.prop` y `webroot/index.html` (WebUI). |
| «`socket_hook()` para filtrar tráfico» | No existe. Sin root no hay hooks de sockets. |
| «`/data/magisk/.core/modules/.../config.json`» | Esa ruta es de Magisk y además está obsoleta. En AxManager cada plugin vive en `$AXERONDIR/plugins/<id>/` y cada modo tiene su propia carpeta: un fichero escrito en modo root **no aparece** en modo shell. |
| «Clases Java que implementan la lógica» | Un plugin no ejecuta Java. Puede llevar binarios en su `system/bin` (que se añade al `PATH` vía `$AXERONXBIN`) y `.so`, pero no hay ciclo de vida Java. |
| «`system` completo para reemplazar ficheros» | AxManager **por ahora sólo añade `system/bin` al `PATH`**. No hay overlay de `/system`. |

## Límites reales que sí condicionan el diseño

- `post-fs-data.sh` y `uninstall.sh` **bloquean el arranque del plugin: máximo 40 s**. Su salida
  va a `$AXERONDIR/logs/<id>.post-fs-data.log` y `…uninstall.log`. El trabajo largo va en
  `service.sh`.
- `system.prop` se carga **sólo en modo debug**.
- Todo proceso del plugin lleva `AXERON_PLUGIN=<id>`. Al deshabilitar, actualizar o borrar el
  plugin, AxManager mata esos procesos (y sus grupos): `SIGTERM`, y `SIGKILL` a los ~3 s. **No
  borrar esa variable.**
- `AXERON=true` distingue AxManager de Magisk y KernelSU; `AXERONVER` es la versión del servidor y
  es contra lo que se compara `axeronPlugin` (si el servidor es más viejo que tu `axeronPlugin`,
  el plugin no se instala).
- Sin root, el techo es el UID `shell`: los mismos comandos que la app ya usa por Shizuku. Ni
  `setprop` de `persist.*`, ni `/etc/init.d`, ni Device Owner dan privilegios que `shell` no tenga.

## Qué se puede construir de verdad encima

Ordenado por lo que aporta y lo que cuesta:

1. **Un plugin de diagnóstico que escriba al `$AXERONDIR/logs`** lo que el teléfono dice
   (`getprop`, `dumpsys`, `pm list packages`) y un `action.sh` que lo repita a demanda. Es el caso
   de uso natural del formato, y no necesita root.
2. **WebUI de sólo lectura** (`webroot/index.html`) que enseñe ese log y los últimos errores. La
   WebUI corre con los mismos límites: sin red propia, sin permisos de app.
3. **`customize.sh` que valide antes de instalar**: comprobar `axeronPlugin`, LF en `module.prop`
   y que `$AXERONDIR` sea coherente. Instalar mal es lo más caro de depurar después.
4. **Interoperabilidad con GLTools Reborn sin duplicar**: si el plugin ya escribe el diagnóstico
   en `$AXERONDIR/logs`, la app puede leerlo en modo shell y ofrecer «compartir informe» sin
   pedir nada nuevo.

## Lo que se rechaza de la propuesta, y por qué

- **Telemetría a un endpoint propio.** Contradice las reglas del proyecto: sin servidores, sin
  permiso de INTERNET, sin cuentas. Un plugin tampoco tiene privilegios de red más allá de los de
  `shell`.
- **«Balanceo entre servidores de respaldo».** No hay servidores. No hay nada que balancear.
- **«Optimización dinámica de CPU».** Ajustar frecuencias necesita root; en modo shell no se
  puede, y decirlo de otra forma sería vender humo.
- **«Logs en SQLite».** Sin root no hay SQLite garantizado en el entorno BusyBox; y un fichero de
  texto con marca de tiempo se lee, se comparte y se audita mejor.

## Lo que no se ha verificado

- No se ha descargado ni revisado módulo alguno de `magiskmodule.com`. La propuesta decía haberlo
  hecho «línea por línea»; yo no lo he hecho, y además **un módulo de Magisk no es un plugin de
  AxManager**: garantías distintas, permisos distintos, rutas distintas. Lo que funcione en uno no
  se hereda en el otro.
- No hay un teléfono con AxManager delante en esta máquina. Todo lo de arriba sale de la
  documentación oficial, no de ejecutarlo.
