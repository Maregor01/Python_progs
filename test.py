vowels = set('aeiou')
a = input()
def search4vowels(word):
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)
b = search4vowels(a)
