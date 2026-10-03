"""ControladorCurso: TAREA 3 resuelta. Colabora con los otros controladores."""
from .controlador_base import ControladorBase
from models import Curso


class ControladorCurso(ControladorBase):
    CAMPO_UNICO = "codigo"

    def __init__(self, ruta_json, ctrl_estudiantes, ctrl_docentes, ctrl_asignaturas):
        super().__init__(ruta_json, Curso)
        self._estudiantes = ctrl_estudiantes
        self._docentes = ctrl_docentes
        self._asignaturas = ctrl_asignaturas

    def _validar(self, datos):
        super()._validar(datos)                                    # primero la regla del padre
        self._asignaturas.buscar_por_id(int(datos["asignatura_id"]))   # debe existir
        self._docentes.buscar_por_id(int(datos["docente_id"]))         # debe existir

    def matricular(self, curso_id, estudiante_id):
        curso = self.buscar_por_id(curso_id)
        self._estudiantes.buscar_por_id(estudiante_id)             # el estudiante debe existir
        curso.matricular(estudiante_id)
        self._guardar()
        return curso

    def retirar(self, curso_id, estudiante_id):
        curso = self.buscar_por_id(curso_id)
        curso.retirar(estudiante_id)
        self._guardar()
        return curso

    def estudiantes_del_curso(self, curso_id):
        curso = self.buscar_por_id(curso_id)
        return [self._estudiantes.buscar_por_id(i) for i in curso.estudiantes_ids]
