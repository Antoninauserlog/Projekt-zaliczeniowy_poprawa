# Editing existing keyword:
from dictionary_WT import dictionary_WT
def edit_keyword(keyword, new_definition):
    """Funkcja służąca do edycji istniejących pojęć w słowniku"""
    keyword = keyword.lower()
    if keyword in dictionary_WT:
        dictionary_WT[keyword] = new_definition
        return f"Definicja '{keyword}' została zaktualizowana."
    else:
        return f"Definicja '{keyword}' nie istnieje w słowniku."
