hammad_age=input("Enter Hammad age \n ")


hammad_age = int(hammad_age)
minimum_age =5
print(type(hammad_age),type(minimum_age))



if (hammad_age < minimum_age & hammad_age != 2) :
    print ("Hammad cannot join the school")

elif hammad_age==2 : 
    print("Hammad abhi chota hay")
else: 
    print("Hammad can join the school")