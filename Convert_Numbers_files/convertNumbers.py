"""
convertNumbers.py: Convierte números de un archivo a su representación
binaria y hexadecimal usando algoritmos básicos.

Uso:
    python convertNumbers.py fileWithData.txt

Los resultados se muestran en pantalla y se guardan en el archivo
ConvertionResults.txt.
"""

import sys
import time


def decimal_to_binary(n):
    """
    Convierte un entero a su representación en binario.
    """
    if n == 0:
        return "0"
    binary_digits = []
    is_negative = False
    if n < 0:
        is_negative = True
        n = -n
    while n > 0:
        remainder = n % 2
        binary_digits.append(str(remainder))
        n //= 2
    binary_digits.reverse()
    binary_str = ''.join(binary_digits)
    if is_negative:
        binary_str = "-" + binary_str
    return binary_str


def decimal_to_hex(n):
    """
    Convierte un entero a su representación en hexadecimal.
    """
    hex_digits = "0123456789ABCDEF"
    if n == 0:
        return "0"
    hex_result = []
    is_negative = False
    if n < 0:
        is_negative = True
        n = -n
    while n > 0:
        remainder = n % 16
        hex_result.append(hex_digits[remainder])
        n //= 16
    hex_result.reverse()
    hex_str = ''.join(hex_result)
    if is_negative:
        hex_str = "-" + hex_str
    return hex_str


def main():
    """
    Función principal.
    """
    if len(sys.argv) != 2:
        print("Uso: python convertNumbers.py fileWithData.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    results_lines = []
    start_time = time.time()

    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()
            items = content.split()
            for item in items:
                try:
                    number = int(item)
                    binary = decimal_to_binary(number)
                    hexadecimal = decimal_to_hex(number)
                    results_lines.append(
                        f"Número: {number}, Binario: {binary}, Hexadecimal: {hexadecimal}\n"
                    )
                except ValueError:
                    print(f"Error: '{item}' no es un entero válido. Se omite.")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{input_file}'.")
        sys.exit(1)
    except OSError as e:
        print(f"Error al leer el archivo '{input_file}': {e}")
        sys.exit(1)

    end_time = time.time()
    elapsed_time = end_time - start_time
    results_lines.append(f"Tiempo Transcurrido: {elapsed_time} segundos\n")

    results = "".join(results_lines)
    print(results)

    try:
        with open("ConvertionResults.txt", 'w', encoding='utf-8') as output_file:
            output_file.write(results)
    except OSError as e:
        print(f"Error al escribir en ConvertionResults.txt: {e}")


if __name__ == "__main__":
    main()
