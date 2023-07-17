print("Python BMI Calculator\n")

print("How tall are you? First enter feet, then enter inches.")
# ask user to input height in feet, then input inches, convert feet to inches, and add all inches for total inches
Height_Feet=float(input("Enter Feet: "))
Height_Inches=float(input("And Enter Inches: "))
Height_Feet_Convert_To_Inches = Height_Feet * 12
Height_Total_Inches = Height_Inches + Height_Feet_Convert_To_Inches

# ask user to input weight
Weight=float(input("Enter your Weight in pounds: "))

# math - square total inches 'inches * inches', and divide weight by height squared, then multiply bmi_one by 703
Height_Squared = Height_Total_Inches*Height_Total_Inches
BMI_One = Weight/Height_Squared
BMI_Two = BMI_One * 703

# print thanks
print("\nThank You\nYou Are " + str(Height_Feet) + " Feet, " +str(Height_Inches)+" Inches Tall.\nYou Weigh: "+str(Weight)+" Pounds.\n")

# determine bmi weight status 18.5 or less	- underweight,  18.5 - 24.99	- normal weight,  25 - 29.99	- overweight,  30+			- obesity
if(BMI_Two > 0):

	# 18.5 or less	- underweight result
	if(BMI_Two <= 18.5):
		print("Your BMI is: '" + str(BMI_Two) + "'.\nWhich means you are classified as 'Underweight'.")
	# 18.5 - 24.99	- normal weight result
	elif(BMI_Two >= 18.5 and BMI_Two <= 24.99):
		print("Your BMI is: '" + str(BMI_Two) + "'.\nWhich means you are classified as 'Normal Weight'.")
	# 25 - 29.99	- overweight result
	elif(BMI_Two >= 25 and BMI_Two <= 29.99):
		print("Your BMI is: '" + str(BMI_Two) + "'.\nWhich means you are classified as 'Overweight'.")
	# 30+			- obesity result
	elif(BMI_Two >= 30):
		print("Your BMI is: '" + str(BMI_Two) + "'.\nWhich means you are classified as 'Obese'.")

	print("\nThanks For Using - Python Bmi Calculator\n")

# request valid details 
else:("enter valid details")

