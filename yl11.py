text = input('tekst: ')

if len(text) < 7 or len(text) % 2 == 0:
    print('tekstis peaks olema vähemalt seitse sümboliid ja sümbolite arv paaris.')
else:
    middle_index = int(len(text) / 2)
    print(text[middle_index1] + text[middle_index] + text[middle_index+1])
