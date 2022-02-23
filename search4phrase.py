
a = input("Введите символы, которые нужно отыскать: ")
b = input("Введите фразу, в которой нужно найти символы: ")
          
def search4letters(search_letters: str, input_phrase: str) -> set:
    """ Output symbols input_phrase variable, contained in search_phrase variable"""
    found = set(search_letters).intersection(set(input_phrase))
    return found
print(search4letters(a, b))
