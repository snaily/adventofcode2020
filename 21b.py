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

def solve(suspects):
    if len(suspects) == 0:
        return {}
    allergen_min = ''
    suspect_min = sys.maxsize
    for allergen, suspect_set in suspects.items():
        if len(suspect_set) < suspect_min:
            allergen_min = allergen
            suspect_min = len(suspect_set)

    print(suspects, allergen_min)

    for suspect in suspects[allergen_min]:
        new_suspects = {}
        for allergen, suspect_set in suspects.items():
            if allergen == allergen_min:
                continue
            new_suspects[allergen] = suspect_set - set((suspect,))
        result = solve(new_suspects)
        if result is not None:
            result[allergen_min] = suspect
            return result
    return None

solution = list(solve(suspects).items())
solution.sort(key=lambda s: s[0])
print(','.join(s[1] for s in solution))