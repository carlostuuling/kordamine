fruits = ['õun', 'pirn', 'banaan']
print(fruits[0])
fruits.append('ploom')
print(fruits[-1])
print(fruits[len(fruits)-1])
fruits[-2] = 'kirss'
print(fruits)
if 'pirn' in fruits:
    print('pirn on listis')

print(len(fruits))
fruits.remove('pirn')
print(fruits)
fruits.reverse()
print(fruits)
fruits.sort()
print(fruits)
