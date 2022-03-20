# equal to ==
# not equal to  !=
# less than     <
# greater than  >
# less than and equal to <=
# greater than and equal to >=

# logic oprators are boolean like TRUE/FALSE, YES/N0

x = 4 != 4
print(x)
print(3>4)
print(3<=3)

#applications of logical operator includes 
hammad_age = 4
age_at_school=5
print("The eligibility says",hammad_age==age_at_school)

#input fns and logical operator
age_at_school=5
hammad_age= input("How old is Hammad")
hammad_age = int (hammad_age)
print(type(hammad_age))
print("The eligibility now says because of type conversion to int is ",hammad_age==age_at_school)


