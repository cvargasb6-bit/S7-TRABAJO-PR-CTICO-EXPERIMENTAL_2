"""ControladorDocente: TAREA 1 resuelta."""
from .controlador_base import ControladorBase
from models import Docente
from shared import ErrorValidacion


class ControladorDocente(ControladorBase):
    CAMPO_UNICO = "cedula"

    def __init__(self, ruta_json):
        super().__init__(ruta_json, Docente)

    def buscar_por_cedula(self, cedula):
        for d in self._items:
            if d.cedula == str(cedula).strip():
                return d
        raise ErrorValidacion(f"No existe un docente con cédula {cedula}.")

    def buscar_por_especialidad(self, texto):
        texto = texto.strip().lower()
        return [d for d in self._items if texto in d.especialidad.lower()]
