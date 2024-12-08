print("Welcome to the BMI Calculator")
#take input from user
weight = int(input("What is your weight in kg? "))
height = float(input("what is your height in m?  "))

#calculate for BMI using formula
BMI = weight/(height)**2
bmi = round(BMI,2)
print(f"Your BMI is {bmi}")

#categorize BMI
if BMI < 18.5:
    print("You are underweight")
elif 18.5 < BMI < 25:
    print("You are normal")
elif 25 < BMI < 30:
    print("You are overweight")
else:
    print("You are obese")