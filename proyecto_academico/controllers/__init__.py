"""Paquete controllers: lógica CRUD y reglas de negocio."""
from .controlador_base import ControladorBase
from .controlador_estudiante import ControladorEstudiante
from .controlador_docente import ControladorDocente
from .controlador_asignatura import ControladorAsignatura
from .controlador_curso import ControladorCurso

__all__ = ["ControladorBase", "ControladorEstudiante", "ControladorDocente",
           "ControladorAsignatura", "ControladorCurso"]
