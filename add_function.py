# Adding new keyword:
from dictionary_WT import dictionary_WT
def add_keyword(keyword, definition):
    """Funkcja służąca do dodawania pojęć do słownika"""
    keyword = keyword.lower()
    if keyword not in dictionary_WT:
        dictionary_WT[keyword] = definition
        return f"Definicja '{keyword}' została dodana do słownika."
    else:
        return f"Definicja '{keyword}' już istnieje w słowniku."