
# Question_no1
# Calculate your age based on the current year and your birth year
print("Age Calculator")
birth_year:int = int(input("Enter your Birth-Year = "))
current_year:int = int(input("Enter your Current-Year = "))
print("Your age is = ",(current_year-birth_year))
# # ---------------------------------------------------

# # Question_no2 
# a program that calculates the area of a rectangle using length and width variables 
print("Rectangle Area Calculator")
length:int = int(input("Enter the length of rectangle = "))
width :int= int(input("Enter the width of rectangle =  "))

print("The area of your rectangle is = length*width = ",length*width,"square unit")
# # ---------------------------------------------------

# # Question_no3
# a program that calculates the area of a circle
print("Circle Area Calculator")
radius:int  = int(input("Enter the radius of = "))
pie_value:float =3.141592653589793238462643383279502884197

print("The area of circle is = value of pie *square of radius = ", pie_value*radius**2,"square unit")
# ---------------------------------------------------

# Question_no4
# a program that calculates the area of the cube
print("Cube Area Calculator")
variable :int = 6
edges:int =int(input("enter number of edges here ="))
print("The area of Cube is = 6*square of edges = ",6*edges**2,"meter cube")
# ---------------------------------------------------

# Question_no5
# a program that converts a temperature from Fahrenheit to Celsius and vice versa using a variable
print("Temperature Convertor (Celsius -> fahrenheit)")
temperature = int(input("Enter your temperature in celsius = "))
print("Temperature in Fahrenheit is = (temperature*9/5)+32) = ", ((temperature*9/5)+32), "degree fahrenheit")

print("Temperature Convertor (fahrenheit -> Celsius)")
temperature = int(input("Enter your temperature in Fahrenheit = "))
print("Temperature in Celsius is = (temperature-32)*5/9 = ", (temperature-32)*5/9 ,"degree celsius")
# ---------------------------------------------------

# Question_no6
# convert a number in seconds
print("Time Calculator")
time_minutes = int(input("Enter your time in minutes = "))
print("Time in seconds is = (time_minutes*60) =  ", (time_minutes*60) ,"sec")
# ---------------------------------------------------

# Question_no7
#  a program that calculates the percentage
print("Percentage Calculator")
obtainedMarks:int= int(input("Enter your obtained marks = "))
totalMarks:int= int(input("Enter your  total marks = "))
print("Percentage is = obtained marks /total marks *100  = ", obtainedMarks/totalMarks*100 , "%")
# ---------------------------------------------------

# Question_no8
#  program that calculates the BMI using height (in meters) and weight (in kilograms) variables
print("BMI Calculator")
weight:int = int(input("enter weight in kilogram = "))
height :int= int(input("enter height in meters = "))
result= weight/height**2
if result < 18.5:
    print('Underweight')
if result >=18.5 and result <25:
    print("Normal")
if result  >= 25 and result  < 30:
   print('Overweight')
if result  >= 30:
   print('Obesity')
# ---------------------------------------------------

# Question_no9
# a program that calculates the volume of a cylinder using the formula
print("Cylinder Volume Calculator")
radiusOfCylinder:int= int(input("Enter the radius of cylinder = "))
heightOfCylinder:int = int(input("Enter the height of cylinder =  "))
pie_value_for_cylinder:float = 3.141592653589793238462643383279502884197
print("Volume of Cylinder is = value of pie*(radius**2)*height = ", pie_value_for_cylinder*(radiusOfCylinder**2)*heightOfCylinder,"meter cube")
# ---------------------------------------------------