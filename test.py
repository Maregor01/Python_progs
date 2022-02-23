
a = input()
def search4vowels(word: str) -> set:
    """ Выводит символы переменной word, содержащиеся в переменной vowels"""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    return found
b = search4vowels(a)
