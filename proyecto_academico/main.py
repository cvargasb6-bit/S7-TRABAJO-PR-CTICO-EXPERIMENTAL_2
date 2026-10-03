"""Punto de entrada: integra modelos, controladores y vistas.

Uso:
    python main.py          -> menú interactivo
    python main.py --demo   -> demostración automática de herencia, validaciones y CRUD
"""
import os
import sys

from controllers import (ControladorEstudiante, ControladorDocente,
                         ControladorAsignatura, ControladorCurso)
from models import Entidad, Persona, Estudiante, Docente
from shared import ErrorValidacion
from views import InterfazConsola

CARPETA_DATOS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")


class SistemaAcademico:

    def __init__(self, carpeta_datos=CARPETA_DATOS):
        self.vista = InterfazConsola()
        ruta = lambda nombre: os.path.join(carpeta_datos, nombre)
        self.estudiantes = ControladorEstudiante(ruta("estudiantes.json"))
        self.docentes = ControladorDocente(ruta("docentes.json"))
        self.asignaturas = ControladorAsignatura(ruta("asignaturas.json"))
        self.cursos = ControladorCurso(ruta("cursos.json"), self.estudiantes,
                                       self.docentes, self.asignaturas)

    # ---------- menú genérico CRUD ----------
    def _menu_crud(self, titulo, ctrl, pedir_datos, extras=()):
        opciones = [("1", "Crear"), ("2", "Listar"), ("3", "Eliminar")]
        opciones += [(str(4 + i), nombre) for i, (nombre, _) in enumerate(extras)]
        opciones.append(("0", "Volver"))
        while True:
            self.vista.mostrar_titulo(titulo)
            op = self.vista.elegir_opcion(opciones)
            try:
                if op == "0":
                    return
                elif op == "1":
                    self.vista.mostrar_mensaje(f"Creado: {ctrl.crear(**pedir_datos())}")
                elif op == "2":
                    self.vista.mostrar_lista(ctrl.listar())
                elif op == "3":
                    ctrl.eliminar(int(self.vista.leer("ID a eliminar")))
                    self.vista.mostrar_mensaje("Registro eliminado.")
                elif op.isdigit() and 4 <= int(op) < 4 + len(extras):
                    extras[int(op) - 4][1]()
                else:
                    self.vista.mostrar_error("Opción no válida.")
            except (ErrorValidacion, ValueError) as error:
                self.vista.mostrar_error(str(error))

    def _registrar_nota(self):
        est = self.estudiantes.registrar_nota(int(self.vista.leer("ID estudiante")),
                                              self.vista.leer("Nota (0-10)"))
        self.vista.mostrar_mensaje(f"Nota registrada. {est}")

    def _matricular(self):
        curso = self.cursos.matricular(int(self.vista.leer("ID curso")),
                                       int(self.vista.leer("ID estudiante")))
        self.vista.mostrar_mensaje(f"Matriculado. {curso}")

    def _retirar(self):
        curso = self.cursos.retirar(int(self.vista.leer("ID curso")),
                                    int(self.vista.leer("ID estudiante")))
        self.vista.mostrar_mensaje(f"Retirado. {curso}")

    def ejecutar(self):
        while True:
            self.vista.mostrar_titulo("SISTEMA ACADÉMICO - UNEMI")
            op = self.vista.elegir_opcion([("1", "Estudiantes"), ("2", "Docentes"),
                                           ("3", "Asignaturas"), ("4", "Cursos"), ("0", "Salir")])
            if op == "1":
                self._menu_crud("ESTUDIANTES", self.estudiantes, self.vista.pedir_datos_estudiante,
                                [("Registrar nota", self._registrar_nota)])
            elif op == "2":
                self._menu_crud("DOCENTES", self.docentes, self.vista.pedir_datos_docente)
            elif op == "3":
                self._menu_crud("ASIGNATURAS", self.asignaturas, self.vista.pedir_datos_asignatura)
            elif op == "4":
                self._menu_crud("CURSOS", self.cursos, self.vista.pedir_datos_curso,
                                [("Matricular estudiante", self._matricular),
                                 ("Retirar estudiante", self._retirar)])
            elif op == "0":
                print("  Hasta pronto.")
                return
            else:
                self.vista.mostrar_error("Opción no válida.")


def demo(carpeta_datos):
    """Ejecuta una demostración automática que evidencia cada tema de la práctica."""
    s = SistemaAcademico(carpeta_datos)
    v = s.vista

    v.mostrar_titulo("1. HERENCIA: cadena de clases")
    for clase in (Estudiante, Docente):
        print("  " + " -> ".join(c.__name__ for c in clase.__mro__ if c is not object))
    print(f"  Estudiante es Persona: {issubclass(Estudiante, Persona)} | "
          f"Persona es Entidad: {issubclass(Persona, Entidad)}")

    v.mostrar_titulo("2. CRUD: crear registros (se guardan en data/*.json)")
    est1 = s.estudiantes.crear(cedula="0923456784", nombres="Ana María", apellidos="Pérez Loor",
                               correo="ana.perez@unemi.edu.ec", matricula="M-001",
                               carrera="Software", semestre=3)
    est2 = s.estudiantes.crear(cedula="0912345675", nombres="Luis Andrés", apellidos="Mora Vera",
                               correo="luis.mora@unemi.edu.ec", matricula="M-002",
                               carrera="Software", semestre=3)
    doc = s.docentes.crear(cedula="0934567819", nombres="Daniel Alexander", apellidos="Vera Paredes",
                           correo="dvera@unemi.edu.ec", titulo="Ingeniero",
                           especialidad="Estructura de Datos", anios_experiencia=8)
    asig = s.asignaturas.crear(codigo="est-201", nombre="Estructura de Datos", creditos=4,
                               horas_semanales=5)
    curso = s.cursos.crear(codigo="ED-A1", asignatura_id=asig.id, docente_id=doc.id,
                           periodo="Agosto 2026 - Diciembre 2026", cupo_maximo=2)
    v.mostrar_lista([est1, est2, doc, asig, curso])

    v.mostrar_titulo("3. REDEFINICIÓN: el mismo método describir() se comporta distinto")
    for obj in (Persona(0, "0922222211", "Persona", "Genérica", "p@mail.com"), est1, doc):
        print(f"  {type(obj).__name__:<10} -> rol: {obj.obtener_rol():<10} | {obj.describir()}")

    v.mostrar_titulo("4. NOTAS y promedio (método privado + propiedad)")
    for nota in (9, 8.5, 7):
        s.estudiantes.registrar_nota(est1.id, nota)
    s.estudiantes.registrar_nota(est2.id, 5)
    v.mostrar_lista(s.estudiantes.listar())

    v.mostrar_titulo("5. MATRÍCULA y control de cupos")
    s.cursos.matricular(curso.id, est1.id)
    s.cursos.matricular(curso.id, est2.id)
    print(f"  {curso}")
    for intento in (lambda: s.cursos.matricular(curso.id, est1.id),
                    lambda: s.estudiantes.crear(cedula="0923456784", nombres="Repetida",
                                                apellidos="Cedula", correo="r@mail.com",
                                                matricula="M-009", carrera="Software")):
        try:
            intento()
        except ErrorValidacion as error:
            v.mostrar_error(str(error))

    v.mostrar_titulo("6. VALIDACIONES (cédula, correo, nota)")
    for texto, accion in (
        ("cédula inválida", lambda: s.estudiantes.crear(cedula="0923456780", nombres="Xx",
            apellidos="Yy", correo="x@y.com", matricula="M-010", carrera="Software")),
        ("correo inválido", lambda: setattr(est1, "correo", "esto-no-es-correo")),
        ("nota fuera de rango", lambda: s.estudiantes.registrar_nota(est1.id, 11)),
    ):
        try:
            accion()
        except ErrorValidacion as error:
            print(f"  {texto}: {error}")

    v.mostrar_titulo("7. PERSISTENCIA: se vuelve a cargar desde los JSON")
    s2 = SistemaAcademico(carpeta_datos)
    v.mostrar_lista(s2.estudiantes.listar() + s2.docentes.listar() + s2.cursos.listar())


if __name__ == "__main__":
    if "--demo" in sys.argv:
        demo(os.path.join(CARPETA_DATOS))
    else:
        SistemaAcademico().ejecutar()
