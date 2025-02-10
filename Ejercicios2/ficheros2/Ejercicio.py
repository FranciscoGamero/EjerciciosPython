import csv

def leer_cotizaciones(fichero):
    datos = {
        "Nombre": [],
        "Final": [],
        "Máximo": [],
        "Mínimo": [],
        "Volumen": [],
        "Efectivo": []
    }

    with open(fichero, mode='r', encoding='utf-8') as archivo_csv:
        
        lector = csv.DictReader(archivo_csv, delimiter=';')
        
       
        print("Encabezados del archivo CSV:", lector.fieldnames)
        
        for fila in lector:
            
            print(fila)  

            datos["Nombre"].append(fila["Nombre"])
            datos["Final"].append(float(fila["Final"].replace(',', '.'))) 
            datos["Máximo"].append(float(fila["Máximo"].replace(',', '.')))
            datos["Mínimo"].append(float(fila["Mínimo"].replace(',', '.')))
            datos["Volumen"].append(int(fila["Volumen"].replace('.', '')))  
            datos["Efectivo"].append(float(fila["Efectivo"].replace(',', '.').replace('.', '')))

    return datos


def generar_estadisticas(datos, fichero_salida):
    estadisticas = []
    
    for columna in ['Final', 'Máximo', 'Mínimo', 'Volumen', 'Efectivo']:
        min_valor = min(datos[columna])
        max_valor = max(datos[columna])
        media_valor = sum(datos[columna]) / len(datos[columna])
        estadisticas.append({
            'Columna': columna,
            'Mínimo': min_valor,
            'Máximo': max_valor,
            'Media': media_valor
        })
    
    with open(fichero_salida, mode='w', newline='', encoding='utf-8') as f:
        escritor = csv.DictWriter(f, fieldnames=['Columna', 'Mínimo', 'Máximo', 'Media'])
        escritor.writeheader()
        escritor.writerows(estadisticas)

def main():
    datos = leer_cotizaciones('cotizacion.csv')
    generar_estadisticas(datos, 'estadisticas_cotizacion.csv')

if __name__ == "__main__":
    main()