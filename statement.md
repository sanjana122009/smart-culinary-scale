# Problem Statement: Smart Culinary Scale & Grocery Wastage Optimizer Engine

## Real-World Problem
Scaling food recipes linearly for large catering events or group meals often leads to ruined taste and high grocery wastage. Key issues include:
1. **Flavor Distortions:** Ingredients like salt, spices, and yeast do not scale linearly ($N \times$). They follow exponential and non-linear scaling curves.
2. **Retail Grocery Mismatch:** Retail items are sold in fixed package sizes (e.g., 200g, 500g). Cooking math fails to optimize minimum packet purchases, leading to food and money wastage.

## Proposed Solution
The **Smart Culinary Scale Engine** solves this using:
- **Non-Linear Vector Scaling:** Uses exponential decay formulas and NumPy array math to preserve recipe taste across variable guest sizes.
- **Wastage Minimization Engine:** Calculates exact grocery packets required to minimize unused inventory and financial waste.
