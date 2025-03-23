from Humans import Human
from Non_humans import Non_human

characters = [Human("John", 100, 10), Non_human("Orc", 100, 10)]
human_char = []
non_human_char = []

def main():
    for char in characters:
        if isinstance(char, Human):
            human_char.append(char.name)
        elif isinstance(char, Non_human):
            non_human_char.append(char.name)
    print("Humans:")
    for h in human_char:
        print(h)
    print("Non-humans:")
    for nh in non_human_char:
        print(nh)

if __name__ == "__main__":
    main()