
weight = int(input("Weight: "))
height = float(input("Height in meter: "))

bmi = weight / (height ** 2)

print(f"BMI: {round(bmi, 2)}")  

# using f-String to print the result 
# round(bmi, 2) = round to 2 decimal places 

#  // ---> floor division (rounds down) int type only 