# conversor.py

### 1. Funciones de Conversión de Temperatura ###

def celsius_a_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_a_kelvin(c):
    return c + 273.15

def fahrenheit_a_celsius(f):
    return (f - 32) * 5/9

### 2. Funciones de Conversión de Distancia ###

def km_a_millas(km):
    return km / 1.60934

def metros_a_pies(m):
    return m * 3.28084

def pies_a_centimetros(pies):
    return pies * 30.48

### 3. Funciones de Conversión de Masa ###

def kg_a_libras(kg):
    return kg * 2.20462

def gramos_a_onzas(g):
    return g / 28.3495

### 4. Funciones de Conversión de Almacenamiento Digital ###

def mb_a_gb(mb):
    return mb / 1024

def gb_a_tb(gb):
    return gb / 1024

# --- Lógica principal del programa ---

def manejar_conversion(titulo, unidad_entrada, unidad_salida, funcion_conversion):
    """Maneja la entrada del usuario y muestra la salida para una conversión específica."""
    print(f"\n--- {titulo} ---")
    try:
        # Entrada de datos: Pedir al usuario el valor
        valor = float(input(f"Ingrese el valor en {unidad_entrada}: "))
        
        # Proceso: Aplicar la función de conversión
        resultado = funcion_conversion(valor)
        
        # Salida: Mostrar el resultado con formato
        print(f"\nResultado: {valor} {unidad_entrada} son {resultado:.2f} {unidad_salida}.")
    except ValueError:
        print("Error: Por favor, ingrese un número válido.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def principal():
    while True:
        print("\n=============================================")
        print("         Conversor Universal")
        print("=============================================")
        print("1.  Temperatura: Celsius a Fahrenheit")
        print("2.  Temperatura: Celsius a Kelvin")
        print("3.  Temperatura: Fahrenheit a Celsius")
        print("4.  Distancia: Kilómetros a Millas")
        print("5.  Distancia: Metros a Pies")
        print("6.  Distancia: Pies a Centímetros")
        print("7.  Masa: Kilogramos a Libras")
        print("8.  Masa: Gramos a Onzas")
        print("9.  Digital: Megabytes a Gigabytes")
        print("10. Digital: Gigabytes a Terabytes")
        print("11. Salir del programa")
        print("---------------------------------------------")

        opcion = input("Elige una opción (1-11): ")

        if opcion == '1':
            manejar_conversion("Celsius a Fahrenheit", "Celsius", "Fahrenheit", celsius_a_fahrenheit)
        elif opcion == '2':
            manejar_conversion("Celsius a Kelvin", "Celsius", "Kelvin", celsius_a_kelvin)
        elif opcion == '3':
            manejar_conversion("Fahrenheit a Celsius", "Fahrenheit", "Celsius", fahrenheit_a_celsius)
        elif opcion == '4':
            manejar_conversion("Kilómetros a Millas", "Kilómetros", "Millas", km_a_millas)
        elif opcion == '5':
            manejar_conversion("Metros a Pies", "Metros", "Pies", metros_a_pies)
        elif opcion == '6':
            manejar_conversion("Pies a Centímetros", "Pies", "Centímetros", pies_a_centimetros)
        elif opcion == '7':
            manejar_conversion("Kilogramos a Libras", "Kilogramos", "Libras", kg_a_libras)
        elif opcion == '8':
            manejar_conversion("Gramos a Onzas", "Gramos", "Onzas", gramos_a_onzas)
        elif opcion == '9':
            manejar_conversion("Megabytes a Gigabytes", "Megabytes", "Gigabytes", mb_a_gb)
        elif opcion == '10':
            manejar_conversion("Gigabytes a Terabytes", "Gigabytes", "Terabytes", gb_a_tb)
        elif opcion == '11':
            print("\nGracias por usar el Conversor Universal. Saliendo...")
            break
        else:
            print("\nOpción no válida. Por favor, selecciona un número del 1 al 11.")
            
# Ejecución del programa
if __name__ == "__main__":
    principal()
