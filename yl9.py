name = input('Mis on sinu nimi: ')
print('tere', name.capitalize() + '!')
residence = input('Elukoht: ')
if 'saaremaa' in residence.lower():
    print('Cool!')
age = input('vanus: ')
age = int(age)
if age < 18:
    print('sa ei tohi veel autoga sõita')
elif age == 18:
    print('palju õnne täisealiseks saamiseks')
else:
    print('mis auto sul on')
