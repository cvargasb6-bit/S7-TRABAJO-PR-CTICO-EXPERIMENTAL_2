"""Pruebas unitarias: ejecutar con  python -m unittest discover -s tests -v"""
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models import Entidad, Persona, Estudiante, Docente, Curso
from shared import ErrorValidacion, validar_cedula
from main import SistemaAcademico


class PruebasHerencia(unittest.TestCase):
    def test_cadena_de_herencia(self):
        self.assertTrue(issubclass(Estudiante, Persona))
        self.assertTrue(issubclass(Docente, Persona))
        self.assertTrue(issubclass(Persona, Entidad))

    def test_redefinicion_de_metodos(self):
        e = Estudiante(1, "0923456784", "Ana", "Pérez", "a@mail.com", "M-1", "Software")
        d = Docente(2, "0934567819", "Dan", "Vera", "d@mail.com", "Ing", "Datos", 12)
        self.assertEqual(e.obtener_rol(), "Estudiante")
        self.assertEqual(d.obtener_rol(), "Docente")
        self.assertIn("Senior", d.describir())

    def test_promedio_y_estado(self):
        e = Estudiante(1, "0923456784", "Ana", "Pérez", "a@mail.com", "M-1", "Software")
        e.registrar_nota(8)
        e.registrar_nota(6)
        self.assertEqual(e.promedio, 7.0)
        self.assertEqual(e.estado, "Aprobado")

    def test_notas_privadas_no_se_modifican_desde_fuera(self):
        e = Estudiante(1, "0923456784", "Ana", "Pérez", "a@mail.com", "M-1", "Software")
        e.notas.append(10)
        self.assertEqual(e.notas, [])

    def test_validaciones(self):
        with self.assertRaises(ErrorValidacion):
            validar_cedula("0923456780")

    def test_no_matricular_dos_veces(self):
        c = Curso(1, "ED-1", 1, 1, "2026", cupo_maximo=5, estudiantes_ids=[9])
        with self.assertRaises(ErrorValidacion):
            c.matricular(9)

    def test_cupo_lleno(self):
        c = Curso(1, "ED-1", 1, 1, "2026", cupo_maximo=1)
        c.matricular(5)
        with self.assertRaises(ErrorValidacion):
            c.matricular(6)

    def test_persistencia_json(self):
        with tempfile.TemporaryDirectory() as carpeta:
            s = SistemaAcademico(carpeta)
            s.estudiantes.crear(cedula="0923456784", nombres="Ana", apellidos="Pérez",
                                correo="a@mail.com", matricula="M-1", carrera="Software")
            otro = SistemaAcademico(carpeta)
            self.assertEqual(len(otro.estudiantes.listar()), 1)
            with self.assertRaises(ErrorValidacion):    # cédula duplicada
                otro.estudiantes.crear(cedula="0923456784", nombres="Dos", apellidos="Mas",
                                       correo="b@mail.com", matricula="M-2", carrera="Software")


if __name__ == "__main__":
    unittest.main()
