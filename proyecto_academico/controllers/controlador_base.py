"""Controlador genérico: el CRUD se escribe UNA vez y los demás controladores lo heredan."""
from shared import ArchivoJSON, ErrorValidacion


class ControladorBase:
    CAMPO_UNICO = None      # nombre del campo que no puede repetirse (cedula, codigo...)

    def __init__(self, ruta_json, modelo):
        self._archivo = ArchivoJSON(ruta_json)
        self._modelo = modelo
        self._items = [modelo.from_dict(d) for d in self._archivo.leer()]

    # ---------- métodos protegidos (apoyo interno) ----------
    def _guardar(self):
        self._archivo.guardar([item.to_dict() for item in self._items])

    def _siguiente_id(self):
        return max((item.id for item in self._items), default=0) + 1

    def _validar(self, datos):
        """Gancho que las hijas REDEFINEN; aquí solo se revisa el campo único."""
        campo = self.CAMPO_UNICO
        if campo and campo in datos:
            nuevo = str(datos[campo]).strip().upper()
            for item in self._items:
                if str(getattr(item, campo)).upper() == nuevo:
                    raise ErrorValidacion(f"Ya existe un registro con {campo} = {datos[campo]}.")

    # ---------- CRUD público ----------
    def crear(self, **datos):
        self._validar(datos)
        objeto = self._modelo(id=self._siguiente_id(), **datos)
        self._items.append(objeto)
        self._guardar()
        return objeto

    def listar(self):
        return list(self._items)

    def buscar_por_id(self, id):
        for item in self._items:
            if item.id == id:
                return item
        raise ErrorValidacion(f"No existe un registro con id {id}.")

    def actualizar(self, id, **cambios):
        objeto = self.buscar_por_id(id)
        for campo, valor in cambios.items():
            setattr(objeto, campo, valor)       # usa los setters validados del modelo
        self._guardar()
        return objeto

    def eliminar(self, id):
        objeto = self.buscar_por_id(id)
        self._items.remove(objeto)
        self._guardar()
        return objeto
