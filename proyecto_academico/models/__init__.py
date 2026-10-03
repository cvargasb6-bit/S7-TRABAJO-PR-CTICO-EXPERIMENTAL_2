"""Paquete models: clases que representan los datos del sistema (jerarquía de herencia)."""
from .entidad import Entidad
from .persona import Persona
from .estudiante import Estudiante
from .docente import Docente
from .asignatura import Asignatura
from .curso import Curso

__all__ = ["Entidad", "Persona", "Estudiante", "Docente", "Asignatura", "Curso"]
