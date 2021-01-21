year = int(input('aasta: '))

if year % 4 and year % 100 !=0 or year % 400 == 0:
    print(year, 'pole liigaasta')
else:
    print(year, ' on liigaasta')
