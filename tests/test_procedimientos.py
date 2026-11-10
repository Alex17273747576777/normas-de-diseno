import pathlib, re, subprocess, unittest
ROOT = pathlib.Path(__file__).resolve().parents[1]

class ProcedimientosTest(unittest.TestCase):
    def test_sintaxis(self):
        for path in (ROOT / "procedimientos").glob("*.sh"):
            subprocess.run(["bash", "-n", str(path)], check=True)
            for block in re.findall(r"<<'PY'\n(.*?)\nPY", path.read_text(), re.S):
                compile(block, str(path), "exec")

    def parser(self):
        script = (ROOT / "procedimientos/04-incidencias.sh").read_text()
        block = re.search(r"<<'PY'\n(.*?)\nPY", script, re.S).group(1)
        namespace = {"__name__": "prueba"}
        exec(compile(block, "incidencias", "exec"), namespace)
        return namespace["parse_blocks"]

    def test_etiquetas_opcionales_y_comillas(self):
        title = "No ejecutar triple comilla: " + "'" * 3
        record = self.parser()(f"repo: owner/repo\ntitulo: {title}\ncuerpo: |\n  Descripción")[0]
        self.assertEqual(record["titulo"], title)
        self.assertEqual(record["labels"], [])
        self.assertEqual(record["body"], "Descripción")

    def test_bloque_invalido_no_se_omite(self):
        with self.assertRaises(ValueError):
            self.parser()("titulo: Sin repositorio")

    def test_nota_falta_antes_de_usar_credenciales(self):
        import os
        env = dict(os.environ, NOTAS_RELEASE="/ruta-inexistente/notas.md")
        p = subprocess.run(["bash", str(ROOT / "procedimientos/03-cerrar-tramo.sh"), "9.9.9", "Prueba"], env=env, capture_output=True, text=True)
        self.assertNotEqual(p.returncode, 0)
        self.assertIn("falta /ruta-inexistente/notas.md", p.stderr)

if __name__ == "__main__":
    unittest.main()
