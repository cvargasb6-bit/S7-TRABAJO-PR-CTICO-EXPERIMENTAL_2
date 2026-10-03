"""Persona hereda de Entidad (nivel 2). Es la clase padre de Estudiante y Docente."""
from .entidad import Entidad
from shared import validar_texto, validar_correo, validar_cedula


class Persona(Entidad):

    def __init__(self, id, cedula, nombres, apellidos, correo, fecha_creacion=None):
        super().__init__(id, fecha_creacion)            # constructor del padre
        self._cedula = validar_cedula(cedula)           # protected: las hijas lo ven
        self._nombres = validar_texto(nombres, "nombres")
        self._apellidos = validar_texto(apellidos, "apellidos")
        self._correo = validar_correo(correo)

    # ---- propiedades (getter / setter con validación) ----
    @property
    def cedula(self):
        return self._cedula

    @property
    def nombres(self):
        return self._nombres

    @nombres.setter
    def nombres(self, valor):
        self._nombres = validar_texto(valor, "nombres")

    @property
    def apellidos(self):
        return self._apellidos

    @apellidos.setter
    def apellidos(self, valor):
        self._apellidos = validar_texto(valor, "apellidos")

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, valor):
        self._correo = validar_correo(valor)

    @property
    def nombre_completo(self):
        return f"{self._nombres} {self._apellidos}"

    # ---- métodos que las hijas REDEFINEN ----
    def obtener_rol(self):
        return "Persona"

    def describir(self):
        return f"[{self.obtener_rol()}] {self.nombre_completo} | CI: {self._cedula} | {self._correo}"

    def to_dict(self):
        datos = super().to_dict()
        datos.update({"cedula": self._cedula, "nombres": self._nombres,
                      "apellidos": self._apellidos, "correo": self._correo})
        return datos
