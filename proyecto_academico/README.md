# Sistema Académico MVC - Práctica 2 (Herencia)

Universidad Estatal de Milagro - Estructura de Datos.

## Ejecutar
```
python main.py          # menú interactivo
python main.py --demo   # demostración automática
python -m unittest discover -s tests -v   # pruebas
```
Requiere Python 3.8 o superior (solo librería estándar).

## Estructura
```
proyecto_academico/
├── main.py                 # SistemaAcademico (integración y menú)
├── shared/                 # código reutilizable
│   ├── archivo_json.py     # ArchivoJSON
│   └── validaciones.py     # cédula, correo, nota, texto, entero
├── models/                 # jerarquía de herencia
│   ├── entidad.py          # Entidad (base)
│   ├── persona.py          # Persona(Entidad)
│   ├── estudiante.py       # Estudiante(Persona)
│   ├── docente.py          # Docente(Persona)
│   ├── asignatura.py       # Asignatura(Entidad)
│   └── curso.py            # Curso(Entidad)
├── controllers/            # CRUD (ControladorBase y sus hijos)
├── views/                  # InterfazConsola
├── data/                   # archivos .json (colecciones)
└── tests/                  # pruebas unitarias
```
