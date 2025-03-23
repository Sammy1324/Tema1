import os
import subprocess

def run_Excercise(Exc_num):
    if Exc_num == 1:
        subprocess.run(["python", "Exc1/main.py"])
    if Exc_num == 2:
        subprocess.run(["python", "Exc2/main.py"])
    if Exc_num == 3:
        subprocess.run(["python", "Exc3/main.py"])
    if Exc_num == 4:
        subprocess.run(["python", "Exc4/main.py"])
    if Exc_num == 5:
        subprocess.run(["python", "Exc5/main.py"])
    if Exc_num == 6:
        subprocess.run(["python", "Exc6/main.py"])
    if Exc_num == 7:
        subprocess.run(["python", "Exc7/main.py"])

def main():
    while True:    
        print("Menú: ")
        print("1. Ejercicio_1")
        print("2. Ejercicio_2")
        print("3. Ejercicio_3")
        print("4. Ejercicio_4")
        print("5. Ejercicio_5")
        print("6. Ejercicio_6")
        print("7. Ejercicio_7")

        choice = input("Seleccione ejercicio a ejecutar: ")
        
        if choice == "1":
                run_Excercise(1)
        if choice == "2":
            run_Excercise(2)
        if choice == "3":
            run_Excercise(3)
        if choice == "4":
            run_Excercise(4)
        if choice == "5":
            run_Excercise(5)
        if choice == "6":
            run_Excercise(6)
        if choice == "7":
            run_Excercise(7)
        if choice == "8":
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()