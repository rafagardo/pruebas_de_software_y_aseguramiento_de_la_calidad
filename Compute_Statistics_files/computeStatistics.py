"""
computeStatistics.py: Calcula estadísticas descriptivas (media, mediana, moda,
varianza y desviación estándar) a partir de un archivo que contiene números.

Uso:
    python computeStatistics.py fileWithData.txt

Los resultados se muestran en pantalla y se guardan en el archivo
StatisticsResults.txt.
"""

import sys
import time


def my_sqrt(number, tolerance=1e-10):
    """
    Calcula la raíz cuadrada de 'number' usando el método de Newton.
    """
    if number < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
    if number == 0:
        return 0.0
    guess = number / 2.0
    while True:
        new_guess = (guess + number / guess) / 2.0
        if abs(new_guess - guess) < tolerance:
            return new_guess
        guess = new_guess


def insertion_sort(data):
    """
    Ordena una lista de números usando el algoritmo de inserción.
    """
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data


def compute_statistics(numbers):
    """
    Calcula las estadísticas descriptivas: media, mediana, moda, varianza y
    desviación estándar.
    """
    n = 0
    total = 0.0
    for num in numbers:
        total += num
        n += 1
    if n == 0:
        raise ValueError("No se han proporcionado números válidos.")
    mean = total / n

    # Calcular la mediana ordenando la lista (se hace una copia para no alterar la original)
    sorted_numbers = numbers.copy()
    insertion_sort(sorted_numbers)
    if n % 2 == 1:
        median = sorted_numbers[n // 2]
    else:
        median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2.0

    # Calcular la moda
    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    max_count = 0
    mode = None
    for num, count in frequency.items():
        if count > max_count:
            max_count = count
            mode = num

    # Calcular varianza y desviación estándar
    sum_sq_diff = 0.0
    for num in numbers:
        diff = num - mean
        sum_sq_diff += diff * diff
    variance = sum_sq_diff / n
    try:
        std_dev = my_sqrt(variance)
    except ValueError:
        std_dev = 0.0

    return mean, median, mode, variance, std_dev


def main():
    """
    Función principal.
    """
    if len(sys.argv) != 2:
        print("Uso: python computeStatistics.py fileWithData.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    numbers = []
    start_time = time.time()

    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()
            items = content.split()
            for item in items:
                try:
                    number = float(item)
                    numbers.append(number)
                except ValueError:
                    print(f"Error: '{item}' no es un número válido. Se omite.")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{input_file}'.")
        sys.exit(1)
    except IOError as e:
        print(f"Error al leer el archivo '{input_file}': {e}")
        sys.exit(1)

    if not numbers:
        print("No se encontraron números válidos en el archivo.")
        sys.exit(1)

    try:
        mean, median, mode, variance, std_dev = compute_statistics(numbers)
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error al calcular las estadísticas: {e}")
        sys.exit(1)

    end_time = time.time()
    elapsed_time = end_time - start_time

    results = (
        f"Estadísticas Descriptivas:\n"
        f"Cantidad: {len(numbers)}\n"
        f"Media: {mean}\n"
        f"Mediana: {median}\n"
        f"Moda: {mode}\n"
        f"Varianza: {variance}\n"
        f"Desviación Estándar: {std_dev}\n"
        f"Tiempo Transcurrido: {elapsed_time} segundos\n"
    )

    print(results)

    try:
        with open("StatisticsResults.txt", 'w', encoding='utf-8') as output_file:
            output_file.write(results)
    except IOError as e:
        print(f"Error al escribir en StatisticsResults.txt: {e}")


if __name__ == "__main__":
    main()
