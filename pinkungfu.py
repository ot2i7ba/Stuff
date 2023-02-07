import itertools
import os

# Terminal löschen
os.system('cls' if os.name == 'nt' else 'clear')

def patternpinkungfu(length, include_digits, include_lowercase, include_uppercase, include_zero, allow_double_digits):

    # Zeichensatz definieren
    characters = ""
    if include_digits:
        characters += "0123456789"
    if include_lowercase:
        characters += "abcdefghijklmnopqrstuvwxyz"
    if include_uppercase:
        characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Ausschlußregelung
    combinations = itertools.product(characters, repeat=length)
    if not allow_double_digits and include_digits:
        combinations = [combination for combination in combinations if len(set(combination)) == length]
    if not include_zero:
        combinations = [combination for combination in combinations if "0" not in combination]
    return combinations

def write_combinations_to_file(combinations, filename):
    with open(filename, "w") as f:
        for combination in list(combinations):
            f.write("".join(combination) + "\n")

def main():
    # Benutzereingabe
    print("PIN-KungFu by ot2i7ba")
    print("-" * 80 + "\n")
    length = int(input("Eingabe der Zeichenlänge (3-16): "))
    include_digits = input("Berücksichtigung von Ziffern (0-9)? (y/n) ").lower() == "y"
    include_lowercase = input("Berücksichtigung von Kleinbuchstaben (a-z)? (y/n) ").lower() == "y"
    include_uppercase = input("Berücksichtigung von Großbuchstaben (A-Z)? (y/n) ").lower() == "y"
    include_zero = input("Kombinationen mit Nullen (0) erlauben? (y/n) ").lower() == "y"
    allow_double_digits = input("Kombinationen mit Duplikaten erlauben? (y/n) ").lower() == "y"

    # Kombinationen generieren
    combinations = list(patternpinkungfu(length, include_digits, include_lowercase, include_uppercase, include_zero, allow_double_digits))

    # Kombinationen Anzahl insgesamt
    print(f"Es wurden {len(combinations)} Kombinationen generiert.")

    # Benutzereingabe des Dateinamens
    filename = input("Dateiname eingeben: ")

    # Dateierweiterung anhängen
    if not filename.endswith(".txt"):
       filename += ".txt"

    # Kombinationen schreiben
    write_combinations_to_file(combinations, filename)
    print(f"Datei {filename} wurde erstellt.")

if __name__ == "__main__":
    main()
