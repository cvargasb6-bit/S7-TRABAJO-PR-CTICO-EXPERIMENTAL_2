"""InterfazConsola: COMPLETO. Solo muestra y pide datos; no contiene reglas de negocio."""


class InterfazConsola:

    # ---------- mensajes ----------
    def mostrar_titulo(self, texto):
        print("\n" + "=" * 60)
        print(texto.center(60))
        print("=" * 60)

    def mostrar_mensaje(self, texto):
        print(f"  [OK] {texto}")

    def mostrar_error(self, texto):
        print(f"  [ERROR] {texto}")

    def mostrar_lista(self, items):
        if not items:
            print("  (sin registros)")
        for item in items:
            print(f"  {item.id:>3} | {item.describir()}")

    # ---------- entradas ----------
    def leer(self, pregunta):
        return input(f"  {pregunta}: ").strip()

    def elegir_opcion(self, opciones):
        for clave, texto in opciones:
            print(f"  {clave}. {texto}")
        return self.leer("Opción")

    # ---------- formularios ----------
    def pedir_datos_persona(self):
        return {"cedula": self.leer("Cédula"), "nombres": self.leer("Nombres"),
                "apellidos": self.leer("Apellidos"), "correo": self.leer("Correo")}

    def pedir_datos_estudiante(self):
        datos = self.pedir_datos_persona()
        datos.update({"matricula": self.leer("Matrícula"), "carrera": self.leer("Carrera"),
                      "semestre": self.leer("Semestre")})
        return datos

    def pedir_datos_docente(self):
        datos = self.pedir_datos_persona()
        datos.update({"titulo": self.leer("Título"), "especialidad": self.leer("Especialidad"),
                      "anios_experiencia": self.leer("Años de experiencia")})
        return datos

    def pedir_datos_asignatura(self):
        return {"codigo": self.leer("Código"), "nombre": self.leer("Nombre"),
                "creditos": self.leer("Créditos"), "horas_semanales": self.leer("Horas semanales")}

    def pedir_datos_curso(self):
        return {"codigo": self.leer("Código del curso"), "asignatura_id": self.leer("ID asignatura"),
                "docente_id": self.leer("ID docente"), "periodo": self.leer("Período"),
                "cupo_maximo": self.leer("Cupo máximo")}
