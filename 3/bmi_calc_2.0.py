height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = round(weight / height ** 2)

if(bmi < 18.5):
    print("Your BMI is: ", bmi, "You are underweight")
elif(bmi >= 18.5 and bmi < 25):
    print("Your BMI is: ", bmi, "You are normal weight")
elif(bmi >= 25 and bmi < 30):
    print("Your BMI is: ", bmi, "You are overweight")
else:
    print(f"Your BMI is: {bmi} You are obese")


