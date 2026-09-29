from abc import ABC, abstractmethod

class BaseRecipe(ABC):
    def __init__(self, recipe_name: str, base_servings: int):
        self._recipe_name = recipe_name
        self._base_servings = base_servings
        self._ingredients = {}

    @property
    def recipe_name(self):
        return self._recipe_name

    @property
    def base_servings(self):
        return self._base_servings

    def add_ingredient(self, name: str, quantity: float, unit: str, scaling_type: str = "linear"):
        self._ingredients[name] = {
            "quantity": quantity,
            "unit": unit,
            "scaling_type": scaling_type
        }

    @abstractmethod
    def display_recipe(self):
        pass