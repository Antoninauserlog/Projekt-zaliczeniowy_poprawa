
# User next action when one is completed:
def next_choice():
    """Funkcja umożliwiająca wybór kolejnego działania na słowniku. """
    while True:
        print("\nCo chcesz zrobić teraz?")
        print("1. Wyszukaj pojęcie")
        print("2. Dodaj nowe pojęcie")
        print("3. Edytuj istniejące pojęcie")
        print("4. Zgłoś pojęcie do usunięcia")
        print("5. Zarejestruj się")
        print("6. Zaloguj się")
        print("7. Wyjdź")
        choice = input("Wybierz opcję(dwukrotnie, aby zatwierdzić): ")
        if choice in ["1", "2", "3", "4", "5", "6", "7"]:
            return choice
        else:
            print("Nieprawidłowy wybór. Wybierz liczbę od 1 do 7 i spróbuj ponownie.")

