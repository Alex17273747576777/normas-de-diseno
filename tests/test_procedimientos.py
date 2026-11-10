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

    def test_el_token_no_viaja_en_la_url_del_push(self):
        script = (ROOT / "procedimientos/03-cerrar-tramo.sh").read_text()
        self.assertNotRegex(script, r"https://[^\s\"]*\$TOKEN@")
        self.assertIn('http.extraheader="$AUTH"', script)

    def test_la_guarda_de_secretos_reconoce_lo_que_no_debe_subirse(self):
        script = (ROOT / "procedimientos/03-cerrar-tramo.sh").read_text()
        patron = re.search(r"grep -Ei '([^']+)'", script).group(1).replace("(^|/)", "(?:^|/)")
        for malo in ("llave.jks", "firma/reborn-release.keystore", ".pass", "x/.pass", ".tokens", "home/.gh-tokens", "clave.pem"):
            self.assertRegex(malo, re.compile(patron, re.I), malo)
        for bueno in ("app/build.gradle", "README.md", "app/src/main/java/Compas.kt", "notas/passo.md"):
            self.assertNotRegex(bueno, re.compile(patron, re.I), bueno)

    def test_el_censo_no_confunde_red_caida_con_categoria_vacia(self):
        import runpy, time, urllib.request
        def caida(*a, **k):
            raise OSError("sin red")
        real_sleep, real_open = time.sleep, urllib.request.urlopen
        time.sleep, urllib.request.urlopen = (lambda *_: None), caida
        try:
            m = runpy.run_path(str(ROOT / "procedimientos/01-censar-catalogo-appteka.py"), run_name="censo")
            self.assertEqual(m["pedir"]({"category_id": 3})["entries"], [])
            self.assertEqual(len(m["FALLOS"]), 1)
            self.assertIn("sin red", m["FALLOS"][0])
        finally:
            time.sleep, urllib.request.urlopen = real_sleep, real_open

if __name__ == "__main__":
    unittest.main()
