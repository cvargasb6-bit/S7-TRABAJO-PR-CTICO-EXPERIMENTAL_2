"""ControladorAsignatura: TAREA 2 resuelta."""
from .controlador_base import ControladorBase
from models import Asignatura
from shared import ErrorValidacion


class ControladorAsignatura(ControladorBase):
    CAMPO_UNICO = "codigo"

    def __init__(self, ruta_json):
        super().__init__(ruta_json, Asignatura)

    def buscar_por_codigo(self, codigo):
        for a in self._items:
            if a.codigo == str(codigo).strip().upper():
                return a
        raise ErrorValidacion(f"No existe una asignatura con código {codigo}.")

    def total_creditos(self):
        return sum(a.creditos for a in self._items)
