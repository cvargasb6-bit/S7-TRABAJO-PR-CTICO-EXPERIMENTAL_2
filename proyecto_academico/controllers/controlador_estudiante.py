"""ControladorEstudiante: COMPLETO."""
from .controlador_base import ControladorBase
from models import Estudiante
from shared import ErrorValidacion


class ControladorEstudiante(ControladorBase):
    CAMPO_UNICO = "cedula"

    def __init__(self, ruta_json):
        super().__init__(ruta_json, Estudiante)

    def buscar_por_cedula(self, cedula):
        for e in self._items:
            if e.cedula == str(cedula).strip():
                return e
        raise ErrorValidacion(f"No existe un estudiante con cédula {cedula}.")

    def registrar_nota(self, id, nota):
        estudiante = self.buscar_por_id(id)
        estudiante.registrar_nota(nota)
        self._guardar()
        return estudiante

    def aprobados(self):
        return [e for e in self._items if e.estado == "Aprobado"]
