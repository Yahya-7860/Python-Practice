fruitDetails = {
    'name': input('Enter Fruit name : '),
    'color': input('Enter color name : ')
}

if fruitDetails['name'] == 'banana' or 'mango':
    if fruitDetails['color'] == 'green':
        print('Unripe')
    elif fruitDetails['color'] == 'yellow':
        print('Ripe')
    elif fruitDetails['color'] == 'brown':
        print('Overripe')

elif fruitDetails['name'] == 'apple':
    if fruitDetails['color'] == 'green':
        print('Unripe')
    elif fruitDetails['color'] == 'red':
        print('Ripe')
    elif fruitDetails['color'] == 'brown':
        print('Overripe')
