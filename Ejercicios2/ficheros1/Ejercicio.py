import csv

def leer_datos(fichero):
    alumnos = []
    with open(fichero, newline='', encoding='utf-8') as f:
        lector = csv.DictReader(f)
        for fila in lector:
            notas = {materia: int(fila[materia]) for materia in fila.keys() if materia not in ['Nombre', 'Apellidos', 'Curso']}
            alumno = {
                "nombre": fila["Nombre"],
                "apellidos": fila["Apellidos"],
                "curso": fila["Curso"],
                "notas": notas
            }
            alumnos.append(alumno)
    return alumnos

def calcular_nota_media(notas):
    return sum(notas.values()) / len(notas) if notas else 0

def mostrar_alumnos_con_media(alumnos):
    for alumno in alumnos:
        media = calcular_nota_media(alumno["notas"])
        print(f"{alumno['nombre']} {alumno['apellidos']}: Nota media = {media:.2f}")

def mostrar_notas_por_asignatura(alumnos, curso, asignatura):
    print(f"Notas de {asignatura} en el curso {curso}:")
    for alumno in alumnos:
        if alumno['curso'] == curso and asignatura in alumno['notas']:
            print(f"{alumno['nombre']} {alumno['apellidos']}: {alumno['notas'][asignatura]}")

def calcular_porcentaje_aprobados(alumnos, curso):
    asignaturas = set()
    aprobados = {}
    total = {}
    
    for alumno in alumnos:
        if alumno['curso'] == curso:
            for asignatura, nota in alumno['notas'].items():
                asignaturas.add(asignatura)
                total[asignatura] = total.get(asignatura, 0) + 1
                if nota >= 5:
                    aprobados[asignatura] = aprobados.get(asignatura, 0) + 1
    
    print(f"Porcentaje de aprobados en el curso {curso}:")
    for asignatura in asignaturas:
        porcentaje = (aprobados.get(asignatura, 0) / total[asignatura]) * 100
        print(f"{asignatura}: {porcentaje:.2f}%")

def generar_fichero_curso(alumnos, curso):
    with open(f"{curso}.txt", "w", encoding="utf-8") as f:
        for alumno in alumnos:
            if alumno['curso'] == curso:
                media = calcular_nota_media(alumno["notas"])
                f.write(f"{alumno['nombre']} {alumno['apellidos']}: {media:.2f}\n")
    print(f"Fichero {curso}.txt generado correctamente.")

def menu():
    fichero = "notas.txt"
    alumnos = leer_datos(fichero)
    
    while True:
        print("\nMenú de opciones:")
        print("1. Mostrar listado de alumnos con nota media")
        print("2. Mostrar notas de una asignatura en un curso")
        print("3. Mostrar porcentaje de aprobados por asignatura en un curso")
        print("4. Generar fichero de curso con notas medias")
        print("5. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            mostrar_alumnos_con_media(alumnos)
        elif opcion == "2":
            curso = input("Introduce el curso: ")
            asignatura = input("Introduce la asignatura: ")
            mostrar_notas_por_asignatura(alumnos, curso, asignatura)
        elif opcion == "3":
            curso = input("Introduce el curso: ")
            calcular_porcentaje_aprobados(alumnos, curso)
        elif opcion == "4":
            curso = input("Introduce el curso: ")
            generar_fichero_curso(alumnos, curso)
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    menu()