# Menu:
from search_function import find_keyword
from add_function import add_keyword
from edit_function import edit_keyword
from delete_function import delete_keyword
from login_function import login_panel
from next_choice_function import next_choice
from user_login_function import user_login

def interactive_dictionary_WT():
    """Funkcja mająca za zadanie spoić wszystkie funkcje w jeden program"""
    logged_in = False
    while True:
        print(" Witaj w interaktywnym słowniku architektoniczno - budowlanym!\n Zapraszamy do zgłębiania pojęć z zakresu architektury i budownictwa lub dodania własnych definicji.\n Uwaga! Aby dodać własne definicje musisz zarejestrować swój numer uprawnień.\n\n MENU UŻYTKOWNIKA\n 1. Wyszukaj pojęcie\n 2. Dodaj nowe pojęcie\n 3. Edytuj istniejące pojęcie\n 4. Zgłoś pojęcie do usunięcia\n 5. Zarejestruj się\n 6. Zaloguj się\n 7. Wyjdź")
        choice = input("Wybierz opcję: ")
        if choice == "1":
            while True:
                keyword = input("Podaj pojęcie: ")
                result = find_keyword(keyword)
                if result:
                    print(f'{result}\n')
                    break
                else:
                    print("Słowo nie zostało znalezione w słowniku. Spróbuj ponownie.")
        elif choice == "2":
            if logged_in:
                keyword = input("Podaj pojęcie: ")
                definition = input("Podaj definicję: ")
                print(add_keyword(keyword, definition))
            else:
                print("Musisz być zalogowany, aby dodać nową definicję.")
        elif choice == "3":
            if logged_in:
                keyword = input("Podaj pojęcie: ")
                new_definition = input("Podaj nową definicję: ")
                print(edit_keyword(keyword, new_definition))
            else:
                print("Musisz być zalogowany, aby edytować pojęcie.")
        elif choice == "4":
            if logged_in:
                keyword = input ("Podaj słowo, które chcesz usunąć:")
                print(delete_keyword(keyword))
            else:
                print("Musisz być zalogowany, aby zgłosić pojęcie do usunięcia.")
        elif choice == "5":
            print(login_panel())
        elif choice == "6":
            login_result = user_login()
            if login_result == True:
                logged_in = True
            if login_result == False:
                logged_in = False
        elif choice == "7":
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")
        input()
        next_choice()
