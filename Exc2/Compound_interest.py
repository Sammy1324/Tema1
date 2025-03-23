class CalculateCompoundInterest:
    def __init__(self, principal, rate, time):
        self.principal = principal
        self.rate = rate
        self.time = time

    def calculate(self):
        return self.principal * (1 + self.rate) ** self.time
    
    def __str__(self):
        return f"Compound interest is {self.calculate()}"