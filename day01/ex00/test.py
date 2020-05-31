from book import Book
from recipe import Recipe
from time import sleep

sandwich = Recipe("Sandwich", 3, 5, ["cheese", "bread", "ham", "pickles"], "basic sandwich", "lunch")
ice_cream = Recipe("Ice Cream", 4, 120, ["Milk", "Chocolate", "Vanilla"], "just ice cream", "dessert")
bruscetta = Recipe("Bruscetta", 2, 15, ["Bread", "Tomatoes"], "italian starter", "starter")
banana = Recipe("Banana", 1, 0, ["Banana"], "Just a banana.", "dessert")

recipes_dict = {
        'starter': [bruscetta],
        'lunch': [],
        'dessert': [],
        }

book = Book("My recipes", recipes_dict)

print("###########################")
print("#### BOOK __str__ test ####")
print("###########################")
print()
print(str(book))
print("##############################")
print("#### BOOK add_recipe test ####")
print("##############################")
print()
sleep(5)
book.add_recipe(sandwich)
book.add_recipe(ice_cream)
book.add_recipe(banana)
print(str(book))
print("######################################")
print("#### BOOK get_recipe_by_name test ####")
print("######################################")
print()
book.get_recipe_by_name("Sandwich")
print("######################################")
print("#### BOOK get_recipe_by_type test ####")
print("######################################")
print()
book.get_recipes_by_types("lunch")
book.get_recipes_by_types("dessert")
book.get_recipes_by_types("blabla")
