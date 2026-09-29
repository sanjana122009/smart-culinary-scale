import numpy as np

class IngredientSubstitutionEngine:
    @staticmethod
    def adjust_for_substitution(scaled_ingredients: dict, original_item: str, sub_item: str, ratio: float):
        updated_ingredients = scaled_ingredients.copy()
        if original_item in updated_ingredients:
            orig_data = updated_ingredients.pop(original_item)
            new_quantity = orig_data["scaled_qty"] * ratio
            updated_ingredients[sub_item] = {
                "scaled_qty": round(new_quantity, 2),
                "unit": orig_data["unit"]
            }
            print(f"\n[SUBSTITUTION] Replaced '{original_item}' with '{sub_item}' (Ratio: {ratio}x). New Qty: {round(new_quantity, 2)}{orig_data['unit']}")
        return updated_ingredients