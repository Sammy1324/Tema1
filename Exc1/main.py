from Recipe import Recipe

def main():
    recipe1 = input("Pegue la información de la receta: ")
    nums = ["0","1","2","3","4","5","6","7","8","9"]
    calories = 0

    for r in recipe1:
        if r in nums:
            calories *= 10
            calories += int(r)
            recipe1 = recipe1.replace(r, "")
            name = recipe1[::-1]
    
    recipe = Recipe(name, calories)
    print(recipe)

if __name__ == "__main__":
    main()