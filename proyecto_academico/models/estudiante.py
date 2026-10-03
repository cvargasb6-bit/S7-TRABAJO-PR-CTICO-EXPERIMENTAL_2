"""Estudiante hereda de Persona (nivel 3): COMPLETO."""
from .persona import Persona
from shared import validar_texto, validar_entero, validar_nota


class Estudiante(Persona):
    NOTA_APROBACION = 7.0

    def __init__(self, id, cedula, nombres, apellidos, correo, matricula, carrera,
                 semestre=1, notas=None, fecha_creacion=None):
        super().__init__(id, cedula, nombres, apellidos, correo, fecha_creacion)
        self._matricula = validar_texto(matricula, "matrícula", 3)
        self._carrera = validar_texto(carrera, "carrera")
        self._semestre = validar_entero(semestre, "semestre", 1, 12)
        self.__notas = [validar_nota(n) for n in (notas or [])]   # variable PRIVADA

    @property
    def matricula(self):
        return self._matricula

    @property
    def carrera(self):
        return self._carrera

    @carrera.setter
    def carrera(self, valor):
        self._carrera = validar_texto(valor, "carrera")

    @property
    def semestre(self):
        return self._semestre

    @semestre.setter
    def semestre(self, valor):
        self._semestre = validar_entero(valor, "semestre", 1, 12)

    @property
    def notas(self):
        return list(self.__notas)           # copia: no se expone la lista privada

    def registrar_nota(self, valor):
        """Método PÚBLICO: agrega una nota validada."""
        self.__notas.append(validar_nota(valor))

    def __calcular_promedio(self):          # método PRIVADO
        return round(sum(self.__notas) / len(self.__notas), 2) if self.__notas else 0.0

    @property
    def promedio(self):
        return self.__calcular_promedio()

    @property
    def estado(self):
        if not self.__notas:
            return "Sin notas"
        return "Aprobado" if self.promedio >= self.NOTA_APROBACION else "Reprobado"

    # ---- REDEFINICIÓN de métodos del padre ----
    def obtener_rol(self):
        return "Estudiante"

    def describir(self):
        base = super().describir()
        return f"{base} | {self._carrera} S{self._semestre} | Prom: {self.promedio} ({self.estado})"

    def to_dict(self):
        datos = super().to_dict()
        datos.update({"tipo": "estudiante", "matricula": self._matricula, "carrera": self._carrera,
                      "semestre": self._semestre, "notas": self.__notas})
        return datos

    @classmethod
    def from_dict(cls, d):
        return cls(d["id"], d["cedula"], d["nombres"], d["apellidos"], d["correo"],
                   d["matricula"], d["carrera"], d.get("semestre", 1), d.get("notas"),
                   d.get("fecha_creacion"))
