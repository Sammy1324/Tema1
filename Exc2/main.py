from Compound_interest import CalculateCompoundInterest
import random

def main(): 
    initial_principal = 1000
    rate = random.uniform(0.01, 0.1)
    print(f"La tasa de interes anual es: {round(rate, 2)}")
    years = int(input("Enter the number of years: "))

    if years < 0:
        print("Invalid input")
    else:
        r = round(rate, 2)
        compound_interest = CalculateCompoundInterest(initial_principal, r, years)
        print(compound_interest)

if __name__ == "__main__":
    main()