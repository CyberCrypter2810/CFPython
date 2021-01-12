# Body_Index.py

# asks user their weight and height
feet = int(input("How tall are you in feet? "))
inches = int(input("If your taller than provided feet, what is your remainding height in inches? "))
height = (feet * 12) + inches

weight = float(input("How much to do weight in pounds? "))

# calculation formula for BMI
BMI = weight * (703 / (height ** 2))

# displays resutls for BMI
print("Your BMI results is: ", format(BMI, '.2f'))
# determans weither the person is over or under weight
if BMI < 18.5:
    print("You are currently underweight.")
elif BMI > 18.5 and BMI < 25:
    print("You are currently in a healthy weight range.")
else:
    print("You are currently overweight.")
