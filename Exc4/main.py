from Level import difficulty_level

missions = [difficulty_level("Mission 1", 1), difficulty_level("Mission 2", 2), difficulty_level("Mission 3", 3)]
organised_missions = []

def main():
    print("Misiones:")
    for m in missions:
        organised_missions.append(m)
        organised_missions.sort(key=lambda x: x.get_level())
   
    for o_m in organised_missions:
        print(o_m.get_mission_name())

if __name__ == "__main__":
    main()