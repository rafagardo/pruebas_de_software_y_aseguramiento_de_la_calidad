"""
wordCount.py: Cuenta las palabras distintas y su frecuencia en un archivo.

Uso:
    python wordCount.py fileWithData.txt

Los resultados se muestran en pantalla y se guardan en el archivo
WordCountResults.txt.
"""

import sys
import time


def count_words(word_list):
    """
    Cuenta las palabras en una lista y devuelve un diccionario con la frecuencia.
    """
    frequency = {}
    for word in word_list:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency


def main():
    """
    Función principal.
    """
    if len(sys.argv) != 2:
        print("Uso: python wordCount.py fileWithData.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    start_time = time.time()
    words = []

    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()
            items = content.split()
            # Se realiza una limpieza básica: se eliminan caracteres no alfanuméricos
            for item in items:
                cleaned_word = ""
                for char in item:
                    if char.isalnum():
                        cleaned_word += char
                if cleaned_word:
                    words.append(cleaned_word.lower())
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{input_file}'.")
        sys.exit(1)
    except IOError as e:
        print(f"Error de E/S al leer el archivo '{input_file}': {e}")
        sys.exit(1)
    except UnicodeDecodeError as e:
        print(f"Error de decodificación al leer el archivo '{input_file}': {e}")
        sys.exit(1)

    if not words:
        print("No se encontraron palabras válidas en el archivo.")
        sys.exit(1)

    frequency = count_words(words)

    end_time = time.time()
    elapsed_time = end_time - start_time

    results_lines = []
    results_lines.append("Conteo de Palabras:\n")
    for word, count in frequency.items():
        results_lines.append(f"{word}: {count}\n")
    results_lines.append(f"Tiempo Transcurrido: {elapsed_time} segundos\n")
    results = "".join(results_lines)
    print(results)

    try:
        with open("WordCountResults.txt", 'w', encoding='utf-8') as output_file:
            output_file.write(results)
    except IOError as e:
        print(f"Error de E/S al escribir en WordCountResults.txt: {e}")


if __name__ == "__main__":
    main()
