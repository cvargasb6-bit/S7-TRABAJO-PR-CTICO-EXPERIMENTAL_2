"""Docente hereda de Persona (nivel 3): TAREA 1 resuelta."""
from .persona import Persona
from shared import validar_texto, validar_entero


class Docente(Persona):

    def __init__(self, id, cedula, nombres, apellidos, correo, titulo, especialidad,
                 anios_experiencia=0, fecha_creacion=None):
        super().__init__(id, cedula, nombres, apellidos, correo, fecha_creacion)
        self._titulo = validar_texto(titulo, "título")
        self._especialidad = validar_texto(especialidad, "especialidad")
        self.__anios = validar_entero(anios_experiencia, "años de experiencia", 0, 60)

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, valor):
        self._titulo = validar_texto(valor, "título")

    @property
    def especialidad(self):
        return self._especialidad

    @especialidad.setter
    def especialidad(self, valor):
        self._especialidad = validar_texto(valor, "especialidad")

    @property
    def anios_experiencia(self):
        return self.__anios

    @anios_experiencia.setter
    def anios_experiencia(self, valor):
        self.__anios = validar_entero(valor, "años de experiencia", 0, 60)

    def __nivel(self):                      # método PRIVADO
        if self.__anios >= 10:
            return "Senior"
        return "Semi-senior" if self.__anios >= 4 else "Junior"

    @property
    def nivel(self):
        return self.__nivel()

    # ---- REDEFINICIÓN ----
    def obtener_rol(self):
        return "Docente"

    def describir(self):
        base = super().describir()
        return f"{base} | {self._titulo} en {self._especialidad} | {self.__anios} años ({self.nivel})"

    def to_dict(self):
        datos = super().to_dict()
        datos.update({"tipo": "docente", "titulo": self._titulo,
                      "especialidad": self._especialidad, "anios_experiencia": self.__anios})
        return datos

    @classmethod
    def from_dict(cls, d):
        return cls(d["id"], d["cedula"], d["nombres"], d["apellidos"], d["correo"],
                   d["titulo"], d["especialidad"], d.get("anios_experiencia", 0),
                   d.get("fecha_creacion"))
