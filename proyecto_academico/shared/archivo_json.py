"""Clase reutilizable para guardar y leer colecciones de datos en archivos JSON."""
import json
import os


class ArchivoJSON:
    """Encapsula la lectura y escritura de una lista de diccionarios en un .json."""

    def __init__(self, ruta):
        self.__ruta = ruta          # variable privada: nadie fuera de la clase la toca
        self._asegurar_archivo()    # método protegido: uso interno y de las subclases

    @property
    def ruta(self):
        return self.__ruta

    def _asegurar_archivo(self):
        carpeta = os.path.dirname(self.__ruta)
        if carpeta:
            os.makedirs(carpeta, exist_ok=True)
        if not os.path.exists(self.__ruta):
            self.guardar([])

    def leer(self):
        """Devuelve la lista guardada; si el archivo está dañado devuelve []."""
        try:
            with open(self.__ruta, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            return []

    def guardar(self, datos):
        """Guarda la lista completa (sobrescribe) con formato legible."""
        with open(self.__ruta, "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=4)
