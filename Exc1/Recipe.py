class Recipe:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories
    def __str__(self):
        return f"La receta de {self.name} tiene {self.calories} calorías"