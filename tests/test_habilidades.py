"""El índice de habilidades no puede prometer lo que no existe, ni callar lo que sí.

Nació de un fallo real: el 10-11-2026 el índice listaba ocho habilidades y había nueve carpetas
—`kit-base` no aparecía— y `sistema-de-superficie.md` estaba suelto sin entrada. Una habilidad que
no está en el índice no la encuentra nadie, y entonces no es una habilidad: es un fichero.
"""
import pathlib
import re
import unittest

RAIZ = pathlib.Path(__file__).resolve().parents[1]
HABILIDADES = RAIZ / "habilidades"
INDICE = HABILIDADES / "README.md"


class IndiceHabilidadesTest(unittest.TestCase):

    def setUp(self):
        self.texto = INDICE.read_text(encoding="utf-8")
        # Sólo la tabla del principio: las rutas enlazadas dentro de otras secciones no cuentan.
        self.enlazadas = set(re.findall(r"\]\(([^)]+)\)", self.texto))

    def test_cada_enlace_existe(self):
        rotos = [r for r in self.enlazadas if not (HABILIDADES / r).exists()]
        self.assertEqual(rotos, [], f"el índice enlaza rutas que no existen: {rotos}")

    def test_no_hay_habilidad_fuera_del_indice(self):
        carpetas = {f"{p.name}/SKILL.md" for p in HABILIDADES.iterdir() if p.is_dir()}
        sueltos = {p.name for p in HABILIDADES.glob("*.md")} - {"README.md"}
        fuera = sorted((carpetas | sueltos) - self.enlazadas)
        self.assertEqual(fuera, [], f"habilidades que no están en el índice: {fuera}")

    def test_cada_ficha_tiene_cabecera(self):
        malas = []
        # Sólo carpetas: las fichas sueltas (`sistema-de-superficie.md`) y el propio índice no
        # son habilidades con carpeta. Se comprueba lo que dicen ser, no lo que no son.
        for carpeta in (p for p in HABILIDADES.iterdir() if p.is_dir()):
            ficha = carpeta / "SKILL.md"
            if not ficha.is_file():
                malas.append(f"{carpeta.name}: sin SKILL.md")
                continue
            primera = ficha.read_text(encoding="utf-8").lstrip().splitlines()[:1]
            if primera != ["---"]:
                malas.append(f"{carpeta.name}: sin cabecera ---")
        self.assertEqual(malas, [], malas)


if __name__ == "__main__":
    unittest.main()
