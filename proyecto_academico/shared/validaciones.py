"""Funciones de validación reutilizables en modelos y controladores."""
import re


class ErrorValidacion(ValueError):
    """Error lanzado cuando un dato no cumple las reglas del sistema."""


def validar_texto(valor, campo, minimo=2):
    texto = str(valor).strip()
    if len(texto) < minimo:
        raise ErrorValidacion(f"El campo '{campo}' debe tener al menos {minimo} caracteres.")
    return texto


def validar_entero(valor, campo, minimo=None, maximo=None):
    try:
        numero = int(valor)
    except (TypeError, ValueError):
        raise ErrorValidacion(f"El campo '{campo}' debe ser un número entero.")
    if minimo is not None and numero < minimo:
        raise ErrorValidacion(f"El campo '{campo}' debe ser mayor o igual a {minimo}.")
    if maximo is not None and numero > maximo:
        raise ErrorValidacion(f"El campo '{campo}' debe ser menor o igual a {maximo}.")
    return numero


def validar_correo(valor):
    correo = str(valor).strip().lower()
    if not re.fullmatch(r"[\w.+-]+@[\w-]+(\.[\w-]+)+", correo):
        raise ErrorValidacion("El correo electrónico no tiene un formato válido.")
    return correo


def validar_cedula(valor):
    """Valida una cédula ecuatoriana con el algoritmo del módulo 10."""
    cedula = str(valor).strip()
    if not (cedula.isdigit() and len(cedula) == 10):
        raise ErrorValidacion("La cédula debe tener 10 dígitos numéricos.")
    provincia = int(cedula[:2])
    if not (1 <= provincia <= 24 or provincia == 30) or int(cedula[2]) > 5:
        raise ErrorValidacion("La cédula tiene un código de provincia o tercer dígito inválido.")
    suma = 0
    for i, digito in enumerate(cedula[:9]):
        valor_digito = int(digito) * (2 if i % 2 == 0 else 1)
        suma += valor_digito - 9 if valor_digito > 9 else valor_digito
    if (10 - suma % 10) % 10 != int(cedula[9]):
        raise ErrorValidacion("La cédula no es válida (dígito verificador incorrecto).")
    return cedula


def validar_nota(valor):
    try:
        nota = float(valor)
    except (TypeError, ValueError):
        raise ErrorValidacion("La nota debe ser un número.")
    if not 0 <= nota <= 10:
        raise ErrorValidacion("La nota debe estar entre 0 y 10.")
    return round(nota, 2)
