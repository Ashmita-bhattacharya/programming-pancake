print ("Percentage calculator")
print ("---------------------")
print ("")

m = float(input("Maths: "))
s = float(input("Science: "))
e = float(input("English: "))

print ("")

percentage = ( (m + s + e) / 300 ) * 100
print ("Your percentage is ",percentage)

if percentage >= 60:
	print ("You got 1st division")
elif percentage >= 45:
	print ("You got 2nd division")
elif percentage >= 30:
	print ("You got 3rd division")
else:
	print ("You did not clear")

