# User log-in:

def user_login():
    """Funkcja pozyskująca dane do logowania użytkownika. """

    while True:
        license_number = input("Podaj numer uprawnień: ")
        if len(license_number) > 0 and license_number.isalnum() is True:
            print("Wartość właściwa.")
            break
        else:
            print("Wartość niewłaściwa. Podaj ponownie")

    while True:
        login = input("Podaj login (max. 8 znaków): ")
        if 8 >= len(login) > 0:
            print("Login właściwy.")
            break
        else:
            print("Login niewłaściwy.")

    while True:
        password = input("Podaj hasło (max. 6 znaków): ")
        if  6 >= len(password) > 0:
            print("Hasło właściwe.")
            break
        else:
            print("Hasło niewłaściwe.")

    if 8 >= len(login) > 0 and 6 >= len(password) > 0:
        print("Zalogowano.")
        return True
    else:
        print("Nie udało się zalogować. Spróbuj ponownie.")
        return False

