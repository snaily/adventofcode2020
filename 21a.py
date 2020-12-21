import sys
import re

ingredients_ex = re.compile(r'(.*) \(contains (.*)\)')
# allergen: set(ingredient)
suspects = {}
# ingredient: count
all_ingredients = {}
with open(sys.argv[1]) as file:
    for line in file:
        ingredients, allergens = ingredients_ex.match(line).groups()
        ingredients = ingredients.split(' ')

        for ingredient in ingredients:
            count = all_ingredients.get(ingredient, 0)
            count += 1
            all_ingredients[ingredient] = count

        allergens = allergens.split(', ')
        for allergen in allergens:
            suspect = suspects.get(allergen, set(ingredients))
            suspect = suspect & set(ingredients)
            suspects[allergen] = suspect

total = 0
remaining = set(all_ingredients.keys())
for suspect in suspects.values():
    remaining = remaining - suspect
for ingredient in all_ingredients.keys():
    if ingredient in remaining:
        total += all_ingredients[ingredient]
print(total)