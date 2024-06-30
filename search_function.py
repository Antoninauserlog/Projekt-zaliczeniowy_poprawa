#Keyword searching:
from dictionary_WT import dictionary_WT
def find_keyword(keyword):
    """ Funkcja do wyszukiwania pojęć w słowniku"""
    keyword = keyword.lower()
    if keyword in dictionary_WT:
        return f"{dictionary_WT[keyword]}"
    else:
        return None