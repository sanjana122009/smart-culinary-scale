from scaling.non_linear_scaler import RecipeScaler
from analytics.grocery_costing import GroceryWastageOptimizer

def main():
    print("==================================================")
    print(" SMART CULINARY SCALE & GROCERY WASTAGE OPTIMIZER ")
    print("==================================================")

    # 1. Initialize Recipe
    recipe_name = input("\nEnter Recipe Name (e.g., Kheer): ").strip() or "Kheer"
    base_servings = int(input("Enter Base Servings Count (e.g., 4): ") or 4)

    scaler = RecipeScaler(recipe_name, base_servings)

    # 2. Dynamic Ingredient Input Loop
    print("\n--------------------------------------------------")
    print(" IMPORTANT INSTRUCTIONS:")
    print(" 1. Please enter ONE ingredient at a time.")
    print(" 2. Do NOT separate ingredients with commas.")
    print(" 3. Type 'done' in Ingredient Name when finished.")
    print("--------------------------------------------------")
    
    package_sizes = {}
    
    while True:
        ing_name = input("\nEnter SINGLE Ingredient Name (e.g., milk) [or 'done' to finish]: ").strip()
        if ing_name.lower() == 'done' or not ing_name:
            break
            
        qty = float(input(f"Quantity for '{ing_name}' (e.g., 200): "))
        unit = input(f"Unit for '{ing_name}' (e.g., g, ml, pcs): ").strip() or "g"
        
        print(f"\nSelect Scaling Type for '{ing_name}':")
        print("  1. Linear (Regular items: Milk, Flour, Khoya, Paneer)")
        print("  2. Sub-linear (Spices, Salt, Sugar - Non-linear curves)")
        print("  3. Decay (Strong aromatic flavors)")
        choice = input("Choice (1/2/3, default 1): ").strip()
        
        scaling_type = "linear"
        if choice == "2":
            scaling_type = "sub_linear"
        elif choice == "3":
            scaling_type = "decay"
            
        pkt_size = float(input(f"Standard retail packet size for '{ing_name}' (e.g., 500): ") or 100)
        
        scaler.add_ingredient(ing_name, qty, unit, scaling_type)
        package_sizes[ing_name] = pkt_size

    scaler.display_recipe()

    # 3. Target Guest Input
    target_servings = int(input("\nEnter Target Guest/Servings Count: ") or 10)

    # 4. Scale Recipe
    scaled_recipe = scaler.scale_recipe(target_servings)

    print(f"\n--- SCALED INGREDIENTS FOR {target_servings} SERVINGS ---")
    for ing, details in scaled_recipe.items():
        print(f"-> {ing.capitalize()}: {details['scaled_qty']} {details['unit']}")

    # 5. Grocery Packet Optimization
    GroceryWastageOptimizer.calculate_bulk_buying(scaled_recipe, package_sizes)

if __name__ == "__main__":
    main()