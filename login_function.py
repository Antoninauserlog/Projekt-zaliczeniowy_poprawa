# Log-in panel:

def login_panel():
    """: Funkcja pozyskująca dane do rejestracji nowego użytkownika."""

    while True:
        name = input("Podaj imię: ")
        if len(name) > 0:
            print("Wartość właściwa.")
            break
        else:
            print("Wartość niewłaściwa. Podaj ponownie")

    while True:
        surname = input("Podaj nazwisko: ")
        if len(surname) > 0:
            print("Wartość właściwa.")
            break
        else:
            print("Wartość niewłaściwa. Podaj ponownie")

    while True:
        license_number = input("Podaj numer uprawnień: ")
        if len(license_number) > 0 and license_number.isalnum() is True:
            print("Wartość właściwa.")
            break
        else:
            print("Wartość niewłaściwa. Podaj ponownie")

    while True:
        email = input("Podaj email: ")
        endings = ('.com', '.pl')
        if email.find('@') > (-1) and email.endswith(endings):
            print("Email właściwy.")
            break
        else:
            print("Email niewłaściwy. Podaj ponownie.")

    while True:
        login = input("Podaj login (max. 8 znaków): ")
        if 8 >= len(login) > 0:
            print("Login właściwy.")
            break
        else:
            print("Login niewłaściwy. Spróbuj ponownie")

    while True:
        password = input("Podaj hasło (max. 6 znaków): ")
        if 6 >= len(password) > 0:
            print("Hasło właściwe.")
            break
        else:
            print("Hasło niewłaściwe. Spróbuj ponownie")

    while True:
        card_number = (input("Podaj numer karty (15 znaków):"))
        if len(card_number) == 15 and card_number.isdigit() is True:
            print("Numer właściwy.")
            break
        else:
            print("Numer niewłaściwy. Wprowadź ponownie.")

    while True:
        payment = input("Wprowadź kwotę, którą chcesz opłacić dostęp do konta premium.: ")
        try:
            payment = int(payment)
        except ValueError:
            print('Wprowadź wartość liczbową.')
            continue
        if payment <= 0:
            print('Wprowadź wartość dodatnią.')
            continue
        else:
            print("Płatność zaakceptowana.")
            break

    print("Dziękujemy za wpłatę. Każda kwota będzie przekazana jako darowizna na rzecz dofinansowania studentów architektury "
    "i budownictwa w krajach rozwijających się.")

    return "Twoje konto zostało utworzone."