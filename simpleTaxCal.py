# A small Income Tax calculator for getting understanding of if eles and logical operators in python
# Visit on github --> https://www.github.com/noumanbaloch
# Code --> https://github.com/NoumanBaloch/small_income_tax_calculator
# Grab the repo and play around it happy coding.

# First getting the sallery of user


user_sallery = float(input("Enter your sallery = "))

# Checking user input against conditions

# if user sallery is less than 250000
if(user_sallery < 250000) and (user_sallery > 0):
    print("You Have no tax")

# if user have sallery more than or equal to 250000 and less than 500000
elif(user_sallery >= 250000) and (user_sallery < 500000):
    user_sallery_per = user_sallery/5
    print("Your Total Tax is 5%")
    print(user_sallery_per , " is Detected")

# if user have sallery more than or equal to 500000 and less than 1000000
elif(user_sallery >= 500000) & (user_sallery < 1000000):
    user_sallery_per = user_sallery/20
    print("Your Total Tax is 20%")
    print(user_sallery_per, " is Detected")

# if user have sallery more than or equal to 1000000
elif(user_sallery >= 1000000):
    user_sallery_per = user_sallery/30
    print("Your Total Tax is 30%")
    print(user_sallery_per, " is Detected")

# this is error condition if user input is invalid e.g -4000, -444
else:
    print(user_sallery, "Is not Valid Amount")
