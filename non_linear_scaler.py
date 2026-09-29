import numpy as np
from core.base_recipe import BaseRecipe
from core.decorators import execution_logger

class RecipeScaler(BaseRecipe):
    def __init__(self, recipe_name: str, base_servings: int):
        super().__init__(recipe_name, base_servings)

    def display_recipe(self):
        print(f"\n--- Recipe: {self.recipe_name} (Base Servings: {self.base_servings}) ---")
        for ing, data in self._ingredients.items():
            print(f"- {ing}: {data['quantity']} {data['unit']} ({data['scaling_type']})")

    @execution_logger
    def scale_recipe(self, target_servings: int):
        scale_factor = target_servings / self.base_servings
        quantities = np.array([data["quantity"] for data in self._ingredients.values()], dtype=float)
        scaled_results = {}

        for idx, (ing_name, data) in enumerate(self._ingredients.items()):
            scaling_type = data["scaling_type"]
            original_qty = quantities[idx]

            if scaling_type == "linear":
                new_qty = original_qty * scale_factor
            elif scaling_type == "sub_linear":
                new_qty = original_qty * (scale_factor ** 0.75)
            elif scaling_type == "decay":
                new_qty = original_qty * (scale_factor ** 0.6)
            else:
                new_qty = original_qty * scale_factor

            scaled_results[ing_name] = {
                "scaled_qty": round(float(new_qty), 2),
                "unit": data["unit"]
            }

        return scaled_results