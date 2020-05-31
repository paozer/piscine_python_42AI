

def print_recipe(name):
    if name not in cookbook:
        print('Recipe does not exist.')
        return
    print(f"Ingredients: {cookbook[name]['ingredients']}")
    print(f"TypeOfMeal: {cookbook[name]['meal']}")
    print(f"Time2Cook: {cookbook[name]['prep_time']}")


def print_recipe_names():
    for key in cookbook.keys():
        print(f'{key}')


def rm_recipe(name):
    if name not in cookbook:
        print('Recipe does not exist.')
        return
    cookbook.pop(name)


def add_recipe(name, ingredients, meal, prep_time):
    cookbook[name] = {
            'ingredients': ingredients,
            'meal': meal,
            'prep_time': prep_time,
            }


def handle_input(choice):
    if choice is '1':
        name = input('enter recipe name: ')
        print_recipe(name)
    elif choice is '2':
        print_recipe_names()
    elif choice is '3':
        name = input('enter recipe name: ')
        rm_recipe(name)
    elif choice is '4':
        name = input('enter recipe name: ')
        ingredients = input('enter ingredients sep by spaces: ')
        meal = input('enter meal type: ')
        prep_time = input('enter prep time: ')
        try:
            int(prep_time)
        except ValueError:
            prep_time = -1
        add_recipe(name, ingredients.split(), meal, int(prep_time))


cookbook = {
        'sandwich': {
            'ingredients': ['ham', 'bread', 'cheese'],
            'meal': 'lunch',
            'prep_time': 10,
            },
        'cake': {
            'ingredients': ['flour', 'sugar', 'eggs'],
            'meal': 'dessert',
            'prep_time': 60,
            },
        'salad': {
            'ingredients': ['avocado', 'aragula', 'tomatoes', 'spinach'],
            'meal': 'lunch',
            'prep_time': 15,
            },
        }

if __name__ == "__main__":
    choice = '1'
    while choice != '5':
        if choice not in '12345':
            print('unknown menu choice - retry')
        else:
            print('Menu')
            print('1 - print recipe')
            print('2 - print recipe names')
            print('3 - remove recipe')
            print('4 - add recipe')
            print('5 - quit')
        choice = input('')
        handle_input(choice)
