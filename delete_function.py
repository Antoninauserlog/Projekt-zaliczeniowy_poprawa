# Request to delete existing keyword:
from dictionary_WT import dictionary_WT
def delete_keyword(keyword):
    """Funkcja służąca do zgłoszenia pojęć do usunięcia w przypadku ich
zdezaktualizowania"""
    keyword = keyword.lower()
    if keyword in dictionary_WT:
        del dictionary_WT[keyword]
        return f"Definicja '{keyword}' została zgłoszona do usunięcia."
    else:
        return f"Definicja '{keyword}' nie istnieje w słowniku."
