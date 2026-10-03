"""Curso hereda de Entidad (nivel 2): TAREA 3 resuelta. Relaciona asignatura, docente y estudiantes."""
from .entidad import Entidad
from shared import validar_texto, validar_entero, ErrorValidacion


class Curso(Entidad):

    def __init__(self, id, codigo, asignatura_id, docente_id, periodo, cupo_maximo=30,
                 estudiantes_ids=None, fecha_creacion=None):
        super().__init__(id, fecha_creacion)
        self._codigo = validar_texto(codigo, "código", 3).upper()
        self._asignatura_id = validar_entero(asignatura_id, "asignatura", 1)
        self._docente_id = validar_entero(docente_id, "docente", 1)
        self._periodo = validar_texto(periodo, "período")
        self._cupo_maximo = validar_entero(cupo_maximo, "cupo máximo", 1, 60)
        self.__estudiantes_ids = list(estudiantes_ids or [])    # PRIVADA

    @property
    def codigo(self):
        return self._codigo

    @property
    def asignatura_id(self):
        return self._asignatura_id

    @property
    def docente_id(self):
        return self._docente_id

    @property
    def periodo(self):
        return self._periodo

    @property
    def cupo_maximo(self):
        return self._cupo_maximo

    @cupo_maximo.setter
    def cupo_maximo(self, valor):
        nuevo = validar_entero(valor, "cupo máximo", 1, 60)
        if nuevo < len(self.__estudiantes_ids):
            raise ErrorValidacion("El cupo no puede ser menor a los estudiantes ya matriculados.")
        self._cupo_maximo = nuevo

    @property
    def estudiantes_ids(self):
        return list(self.__estudiantes_ids)

    @property
    def cupos_disponibles(self):
        return self._cupo_maximo - len(self.__estudiantes_ids)

    def matricular(self, estudiante_id):
        if estudiante_id in self.__estudiantes_ids:
            raise ErrorValidacion("El estudiante ya está matriculado en este curso.")
        if self.cupos_disponibles <= 0:
            raise ErrorValidacion("El curso no tiene cupos disponibles.")
        self.__estudiantes_ids.append(estudiante_id)

    def retirar(self, estudiante_id):
        if estudiante_id not in self.__estudiantes_ids:
            raise ErrorValidacion("El estudiante no está matriculado en este curso.")
        self.__estudiantes_ids.remove(estudiante_id)

    def describir(self):
        return (f"[Curso] {self._codigo} | Asig#{self._asignatura_id} Doc#{self._docente_id} | "
                f"{self._periodo} | Matriculados: {len(self.__estudiantes_ids)}/{self._cupo_maximo}")

    def to_dict(self):
        datos = super().to_dict()
        datos.update({"codigo": self._codigo, "asignatura_id": self._asignatura_id,
                      "docente_id": self._docente_id, "periodo": self._periodo,
                      "cupo_maximo": self._cupo_maximo, "estudiantes_ids": self.__estudiantes_ids})
        return datos

    @classmethod
    def from_dict(cls, d):
        return cls(d["id"], d["codigo"], d["asignatura_id"], d["docente_id"], d["periodo"],
                   d.get("cupo_maximo", 30), d.get("estudiantes_ids"), d.get("fecha_creacion"))
