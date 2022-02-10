
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = weight/(height*height)
bmi = round(bmi, 2)
if bmi <= 18.5 : print(f"your bmi is {bmi}, you're underweight") 
elif bmi >18.5 and bmi<=25: print(f"your bmi is {bmi}, you have a normal weight")
elif bmi >25 and bmi<=30: print(f"your bmi is {bmi}, you are slightly overweight")
elif bmi >30 and bmi<=35: print(f"your bmi is {bmi}, you are obese")
else: print("you are clinically obese ")

input('Press ENTER to exit')


