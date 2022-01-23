#WELCOME
# THIS IS PROBLEM SET 1 OF MIT OPENCOURSEWARE 6.0001 INTRODUCTION TO PYTHON

# PART A: HOUSE HUNTING

# totalCost = 1000000
# portionDownPayment = 0.25
# currentSavings = 0
# monthlyGain = currentSavings * (r/12)
# r = 0.04
# annualSalary = 
# portionSaved = 0.1


# print("Welcome to your dream house prize calculator")
# annualSalary = int(input("Write your annual salary: "))
# portionSaved = float(input("Write the portion of your salary saved (Write in decimal e.g 0.1 = 10%): "))
# totalCost = int(input("Write the total cost of the house: "))
# r = 0.04
# savings = 0
# months = 0
# downPayment = totalCost * 0.25
# while savings < downPayment:
#     months += 1
#     savings += (savings*0.04)/12+ (annualSalary*portionSaved)/12

# print(months)


# PART B: SAVING WITH A RAISE

# print("Welcome to your dream house prize calculator")
# annualSalary = int(input("Write your annual salary: "))
# portionSaved = float(input("Write the portion of your salary saved (Write in decimal e.g 0.1 = 10%): "))
# totalCost = int(input("Write the total cost of the house: "))
# semiAnnualRaise = float(input("Write your semmi annual raise: "))
# r = 0.04
# savings = 0
# months = 0
# downPayment = totalCost * 0.25
# newSalary = annualSalary
# while savings < downPayment:
#     months += 1
#     savings += (savings*0.04)/12+ (newSalary*portionSaved)/12
#     if months % 6 == 0:
#         newSalary += newSalary * semiAnnualRaise

# print(months)



# PART C: FINDING THE RIGHT AMOUNT TO SAVE AWAY
# IN PROGRES...

from calendar import month


print("Welcome to your dream house prize calculator")
annualSalary = int(input("Write your annual salary: "))
# months = int(input("Number of months in wich you will pay the downpayment: "))
portionSaved = 1
totalCost = 1000000
semiAnnualRaise = 0.07
r = 0.04
savings = 0
downPayment = totalCost * 0.25
newSalary = annualSalary
time = 0
months = 36
savingsRateLow = 0
savingsRateHigh = 1
epsilon = 0.01
month = 0
while month != 36:
        portionSaved = (savingsRateLow + savingsRateHigh)/2
        time += 1
        
        while savings < downPayment:
                savings += (savings*0.04)/12+ (newSalary*portionSaved)/12
                if month % 6 == 0:
                        newSalary += newSalary * semiAnnualRaise
                month += 1

        if month < 36:
                    savingsRateHigh = portionSaved
                    month -= month
                    savings -= savings
                    newSalary = annualSalary
        if month > 36:
                    savingsRateLow = portionSaved
                    month -= month
                    savings -= savings
                    newSalary = annualSalary

print(time)
print(portionSaved)



     
    

print(months)