import math

def calculateInvestment():
    deposit = float(input("Enter the amount of money you are depositing: "))
    interestRate = float(input("Enter the interest rate (as a percentage): "))
    years = int(input("Enter the number of years you plan on investing for: "))
    interestType = input("Enter 'simple' or 'compound' interest: ").lower()

    interest = interestRate / 100
    totalAmount = 0

    if interestType == "simple":
        totalAmount = deposit * (1 + interest * years)
    elif interestType == "compound":
        totalAmount = deposit * math.pow((1 + interest), years)
    else:
        print("Invalid interest type entered. Please choose 'simple' or 'compound'.")

    print(f"The total amount after {years} years at an interest rate of {interestRate}% will be: R {totalAmount:.2f}")

def calculateBond():
    presentValue = float(input("Enter the present value of the house: R "))
    interestRate = float(input("Enter the interest rate: "))
    months = int(input("Enter the number of months for bond repayment: "))

    monthlyInterestRate = interestRate / 12 / 100
    repayment = (monthlyInterestRate * presentValue) / (1 - math.pow((1 + monthlyInterestRate), -months))

    print(f"The amount to be repaid each month for the bond will be: R {repayment:.2f}")

def main():
    print("Choose either 'investment' or 'bond' from the menu below to proceed:")
    print("investment - to calculate the amount of interest you'll earn on interest.")
    print("bond - to calculate the amount you'll have to pay on a home loan.")

    choice = input("Enter your choice: ").lower()

    if choice == "investment":
        calculateInvestment()
    elif choice == "bond":
        calculateBond()
    else:
        print("Invalid choice entered. Please choose 'investment' or 'bond'.")

if __name__ == "__main__":
    main()
