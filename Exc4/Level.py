class difficulty_level:
    def __init__(self, mission_name, level):
        self.mission_name = mission_name
        self.level = level

    def get_level(self):
        return self.level
    
    def get_mission_name(self):
        return self.mission_name

    def set_level(self, level):
        self.level = level

    def __str__(self):
        return f"Level: {self.level}"