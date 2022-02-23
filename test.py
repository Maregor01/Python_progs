
a = input()
def search4vowels(word):
    """ Выводит символы переменной word, содержащиеся в переменной vowels"""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    return found
