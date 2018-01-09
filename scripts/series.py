a = 10
b = 20
c = [20, 30, 5, 2, 8, 34, 7, 2] # This is called a LIST

print ("The numbers are : ", c)

print ("1st number: ", c[0])
print ("2nd number: ", c[1])
print ("3rd number: ", c[2])



# This is a FOR loop

for num in range(8):
	print (c[num])

print ("2nd loop")

for num in c:
	print (num)

print ("Loop ends here")


#This one is called a dictionary

age = {"Ashmita": 25, "Raj": 29, "Ponkhy": 26}

print ("Ashmita's age is ", age["Ashmita"]) 

code = {"a":"b", "s":"k", "h":"r", "u":"x", " ":";"}

name = input("Name: ")

print ("The coded name is: ")
print (code[name[0]] , code[name[1]], code[name[2]], code[name[3]])


coded = ""

for x in range(len(name)):   
	coded = coded + code[name[x]]

print ("Coded name: ", coded)


##################################################



















