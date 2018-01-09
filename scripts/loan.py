print ("Welcome to SBI Bank")
print ("-------------------")
print ('')
print ('FD computation:')
print ('')

rate = 7.25
deposit = float(input("Your FD amount : "))

interest = deposit * rate /100

per_month_earning = interest/12

print ("Monthly earning : ", per_month_earning)
