text = 'kuresaare Ametikool'

vowels = ['a', 'e', 'i', 'o', 'u', 'õ', 'ä', 'ö', 'ü']

for c in text:
    if c.lower() in vowels:
        i += 1
        print(c)

print(i)
