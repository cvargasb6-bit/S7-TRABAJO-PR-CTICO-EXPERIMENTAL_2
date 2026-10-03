"""Clase base de toda la jerarquía: Entidad (nivel 1 de herencia)."""
from datetime import datetime


class Entidad:
    """Toda cosa que se guarda en el sistema tiene un id y una fecha de creación."""

    def __init__(self, id, fecha_creacion=None):
        self._id = id                                   # atributo PROTECTED
        self._fecha_creacion = fecha_creacion or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @property
    def id(self):
        return self._id

    @property
    def fecha_creacion(self):
        return self._fecha_creacion

    def to_dict(self):
        return {"id": self._id, "fecha_creacion": self._fecha_creacion}

    def describir(self):
        return f"Entidad #{self._id}"

    def __str__(self):
        return self.describir()
