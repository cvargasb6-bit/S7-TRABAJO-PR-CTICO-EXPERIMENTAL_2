"""Asignatura hereda de Entidad (nivel 2): TAREA 2 resuelta."""
from .entidad import Entidad
from shared import validar_texto, validar_entero


class Asignatura(Entidad):
    SEMANAS_PERIODO = 16

    def __init__(self, id, codigo, nombre, creditos, horas_semanales, fecha_creacion=None):
        super().__init__(id, fecha_creacion)
        self._codigo = validar_texto(codigo, "código", 3).upper()
        self._nombre = validar_texto(nombre, "nombre")
        self.__creditos = validar_entero(creditos, "créditos", 1, 12)
        self._horas_semanales = validar_entero(horas_semanales, "horas semanales", 1, 40)

    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = validar_texto(valor, "nombre")

    @property
    def creditos(self):
        return self.__creditos

    @creditos.setter
    def creditos(self, valor):
        self.__creditos = validar_entero(valor, "créditos", 1, 12)

    @property
    def horas_semanales(self):
        return self._horas_semanales

    @horas_semanales.setter
    def horas_semanales(self, valor):
        self._horas_semanales = validar_entero(valor, "horas semanales", 1, 40)

    def __calcular_horas_totales(self):     # método PRIVADO
        return self._horas_semanales * self.SEMANAS_PERIODO

    @property
    def horas_totales(self):
        return self.__calcular_horas_totales()

    # ---- REDEFINICIÓN ----
    def describir(self):
        return (f"[Asignatura] {self._codigo} - {self._nombre} | {self.__creditos} créditos | "
                f"{self.horas_totales} h/período")

    def to_dict(self):
        datos = super().to_dict()
        datos.update({"codigo": self._codigo, "nombre": self._nombre, "creditos": self.__creditos,
                      "horas_semanales": self._horas_semanales})
        return datos

    @classmethod
    def from_dict(cls, d):
        return cls(d["id"], d["codigo"], d["nombre"], d["creditos"], d["horas_semanales"],
                   d.get("fecha_creacion"))
