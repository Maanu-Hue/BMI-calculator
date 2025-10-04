name=input("Enter Your Name:")
weight=float(input("Enter Your Weight in Kg:"))
height=float(input("Enter Your Height in Meter:"))
BMI=weight/height**2
print(f"Your BMI is: {BMI:.2f}")
if BMI > 0:
    if BMI<18.5:
        print(name +",You are Underweight")
    elif BMI >= 18.5 and BMI <= 24.9 :
        print(name +",You are Normal weight")
    elif BMI >24.9 and BMI <=29.9:
        print(name +",You are Overweight")
    elif BMI >29.9 and BMI <=34.9:
        print(name +",You are Obese")
    elif BMI >34.9 and BMI <=39.9:
        print(name +",You are Severly Obese")
    else:
        print(name, "You are Morbidly Obese")   
else:
    print("Please Enter a Valid Values")