import pathlib, re, unittest

class KitDisenoTest(unittest.TestCase):
    def test_paleta_sin_alias_ni_degradados(self):
        root = pathlib.Path(__file__).resolve().parents[1]
        text = (root / "habilidades/kit-base/Tema.kt").read_text()
        self.assertNotRegex(text, r"val\s+(violeta|cian|rosa|degradado\w*)\s*=")
        self.assertNotIn("Brush.linearGradient", text)
        self.assertNotIn("Brush.verticalGradient", text)
