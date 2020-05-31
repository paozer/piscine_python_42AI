class Recipe:
    def __init__(self, name, cooking_level, cooking_time, ingredients,
                 description, recipe_type):
        if self.valid_attributes(name, cooking_level, cooking_time, ingredients,
                             description, recipe_type) is False:
            exit()
        self.name = name
        self.cooking_level = cooking_level
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        _str = f"The famous {self.name} recipe\n\n"
        _str += f"- level: {self.cooking_level}\n"
        _str += f"- ingredients: {self.ingredients}\n"
        _str += f"- type: {self.recipe_type}\n"
        _str += f"\nDescription:\n{self.description}"
        return _str

    def valid_attributes(self, name, cooking_level, cooking_time, ingredients,
                        description, recipe_type):
        if type(name) is not str or not name:
            print('invalid name')
            return False
        if type(cooking_level) is not int or cooking_level not in range(1, 6):
            print('invalid cooking_level')
            return False
        if type(cooking_time) is not int or cooking_time < 0:
            print('invalid cooking_time')
            return False
        if type(ingredients) is not list or not list:
            print('invalid ingredients')
            return False
        for ingredient in ingredients:
            if type(ingredient) is not str or not ingredient:
                print('invalid ingredient')
                return False
        if type(description) is not str:
            print('invalid description')
            return False
        if type(recipe_type) is not str or not recipe_type or\
           recipe_type not in ['starter', 'lunch', 'dessert']:
            print('invalid recipe_type')
            return False
        return True
