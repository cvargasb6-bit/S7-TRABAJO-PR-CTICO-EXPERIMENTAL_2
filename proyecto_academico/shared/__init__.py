"""Paquete shared: código reutilizable (archivos JSON y validaciones)."""
from .archivo_json import ArchivoJSON
from .validaciones import (ErrorValidacion, validar_texto, validar_entero,
                           validar_correo, validar_cedula, validar_nota)

__all__ = ["ArchivoJSON", "ErrorValidacion", "validar_texto", "validar_entero",
           "validar_correo", "validar_cedula", "validar_nota"]
