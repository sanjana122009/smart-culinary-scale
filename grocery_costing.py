import math

class GroceryWastageOptimizer:
    @staticmethod
    def calculate_bulk_buying(scaled_ingredients: dict, package_sizes: dict):
        buying_plan = {}
        print("\n=== GROCERY BULK BUYING & WASTAGE OPTIMIZER ===")
        for ing_name, details in scaled_ingredients.items():
            required_qty = details["scaled_qty"]
            unit = details["unit"]
            pkt_size = package_sizes.get(ing_name, 100)  
            packets_to_buy = math.ceil(required_qty / pkt_size)
            total_purchased = packets_to_buy * pkt_size
            wastage = total_purchased - required_qty
            buying_plan[ing_name] = {
                "required": required_qty,
                "packets_to_buy": packets_to_buy,
                "packet_size": pkt_size,
                "total_bought": total_purchased,
                "wastage": round(wastage, 2),
                "unit": unit
            }
            print(f"• {ing_name}: Need {required_qty}{unit} | Buy {packets_to_buy} pkt(s) of {pkt_size}{unit} | Waste: {round(wastage, 2)}{unit}")
        return buying_plan