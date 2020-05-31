from datetime import datetime
from recipe import Recipe


class Book:
    def get_recipe_by_name(self, name):
        for key in self.recipes_list.keys():
            for recipe in self.recipes_list[str(key)]:
                if recipe.name is name:
                    print(str(recipe))
                    return recipe
        return None

    def get_recipes_by_types(self, recipe_type):
        if recipe_type not in self.recipes_list.keys():
            print(f'There is no {recipe_type} categorie')
            return
        print(f'These are the recipes in the {recipe_type} categorie.')
        for recipe in self.recipes_list[str(recipe_type)]:
            print(f'- {recipe.name}')

    def add_recipe(self, recipe):
        if type(recipe) is not Recipe:
            return
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now().strftime("%d/%m/%y %H:%M:%S")

    def __init__(self, name, recipes_list):
        self.name = name
        self.creation_date = datetime.now().strftime("%d/%m/%y %H:%M:%S")
        self.last_update = self.creation_date
        self.recipes_list = recipes_list

    def __str__(self):
        name = f"Title: {self.name}\n\n"
        recipes = f"The book contains following recipes:"
        for recipe_type in self.recipes_list:
            recipes += f"\n- {recipe_type}:"
            if not self.recipes_list[recipe_type]:
                recipes += " None"
            for recipe in self.recipes_list[recipe_type]:
                recipes += f" {recipe.name}"
        times = f"\n\nCreated: {self.creation_date}\
                Updated: {self.last_update}\n"
        return name + recipes + times
