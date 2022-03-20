print("Wie alt sind sie")
print("We are learnin with Ammar")
print("We are learnin with Ammar")
print("We are learnin with Ammar")

# #functions definition
# #1
# def print_codanics():
#     print("We are learning with Ammar")
#     print("We are learning with Ammar")
#     print("We are learning with Ammar")
#     print("We are learning with Ammar")

# print_codanics()

#functions definition
#2
# def print_codanics():
#     text = "We are learning with Ammar"
#     print(text)
#     print(text)
#     print(text)

# print_codanics()

#function def
#3
def print_codanics(text):
    print(text)
    print(text)
    print(text)

print_codanics("We are learning Python with ammar 3rd method")

#function def elif
#4

def school_calculator(age,text):
    if age == 5:
        print("Hammad can join the school")

    elif age >5:
        print("Hammad should go to bigger school")
    else:
        print("hammad is still a baby boy")


school_calculator(8,"Hammad")

#function def of future (return scene)
#5

def future_age(age):
    new_age = age +20
    return new_age

# z = future_age(18)
print(future_age(18))