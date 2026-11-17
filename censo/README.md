# Censo de Appteka · sólo código abierto

> Foto del **8 de noviembre de 2026**, hecha con `procedimientos/01-censar-catalogo-appteka.py`
> recorriendo las 42 categorías por la API interna del sitio (`/api/proxy/list`) con el filtro
> `open_source=1`. El volcado completo, app por app con su repositorio de origen, está en
> `censo-2026-11-08.json.gz` (8,7 MB sin comprimir · 1,5 MB comprimido).
>
> **Lo que este censo no dice:** cuántas apps hay en total en Appteka. Dice cuántas son de
> código abierto, que es lo que se estaba buscando. Las cifras son de la fecha indicada y
> cambian: el catálogo recibe apps nuevas cada día.

- Categorías: **42**
- Apps: **36540**
- Con repositorio de origen declarado: **36540**

| Categoría | Apps |
|---|---|
| Tools | 17993 |
| Music & Audio | 2527 |
| Communication | 2165 |
| Entertainment | 1894 |
| Root & System | 1285 |
| Games | 1157 |
| Comics | 836 |
| Personalization | 823 |
| Web | 792 |
| Social | 772 |
| TV | 761 |
| Security & Privacy | 684 |
| Books & Reference | 628 |
| Productivity | 594 |
| Photography | 483 |
| Video Players & Editors | 477 |
| AI | 376 |
| Maps & Navigation | 298 |
| Health & Fitness | 289 |
| Other | 288 |
| Weather | 239 |
| Finance | 222 |
| Education | 193 |
| News & Magazines | 138 |
| Art & Design | 124 |
| Lifestyle | 105 |
| Food & Drink | 77 |
| Events | 67 |
| Medical | 52 |
| Wear OS | 51 |
| Auto & Vehicles | 39 |
| Travel & Local | 24 |
| Family | 19 |
| Shopping | 15 |
| Business | 14 |
| Sports | 12 |
| Parenting | 7 |
| Google Cast | 7 |
| House & Home | 4 |
| Dating | 4 |
| Dual Space | 4 |
| Beauty | 1 |

## CORRECCIÓN · 2026-11-17 · el titular de arriba cuenta listados, no apps

Las cifras de la tabla son **listados (categoría, app)**, no apps. Medidas sobre
`censo-2026-11-08.json.gz`:

| | |
|---|---|
| listados (lo que suma la columna «Apps») | **36.540** |
| **paquetes distintos, o sea apps de verdad** | **9.968** |
| listados por app | media **3,67** · máximo **352** |
| apps que salen en una sola categoría | 5.927 |
| apps que salen en más de siete | 983 |

Las cinco más repetidas: `app.morphe.manager` 352×, `com.leadaxe.lxbox` 175×, `sh.haven.app` 153×,
`com.nebula.karing` 152×, `online.novaproxy.nova_client` 138×.

Cómo se midió (reproducible, no estimado):

```bash
python3 -c "import gzip,json,collections as c; d=json.load(gzip.open('censo/censo-2026-11-08.json.gz','rt',encoding='utf-8')); p=[a.get('paquete') or i for x in d.values() for i,a in x['apps'].items()]; print(len(p),'listados ·',len(set(p)),'paquetes distintos'); print(c.Counter(p).most_common(5))"
```

Esta corrección **no reescribe** el censo del 8 de noviembre: los datos están bien, lo que estaba mal
era la lectura del titular. Desde hoy `07-diff-de-censos.py` informa las dos cifras juntas —apps
distintas y listados— para que el error no se pueda repetir, y el diff identifica las apps por
paquete en todo el censo, no por (categoría, id): con 26.572 entradas repetidas, un diff que
comparara categoría a categoría contaría una reclasificación como «una app nueva y una retirada».
