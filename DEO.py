h = float(input("Enter your height"))
w = float(input("Enter your weight"))
bmi = w/(h ** 2)
if bmi <= 18.5 :
 print("You are underweight")
elif bmi <= 25.9 :
 print("You are normal")
elif bmi <= 29.9 :
 print("You are overweight")
elif bmi <= 39.9 :
 print("You are obese")
else :
 print("You are severly obese")