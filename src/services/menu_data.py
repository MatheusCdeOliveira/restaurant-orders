# Req 3
from os.path import exists
import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.read_csv(source_path)

    def read_csv(self, source_path):
        with open(source_path, "r") as file:
            reader = csv.DictReader(file)
            dishes = {}
            for row in reader:
                name, price, ingredient, amount = row.values()
                if name not in dishes:
                    dish = Dish(name, float(price))
                    dishes[name] = dish

                ingredients = Ingredient(ingredient)
                dishes[name].add_ingredient_dependency(
                    ingredients, int(amount)
                )
                self.dishes.add(dish)
