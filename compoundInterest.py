def calculateCompoundInterest():
    
# This first 3 lines are provided for yougetACompoundIntrest()
# This first 3 lines are provided for you
 client_one_principal = float(input("Principle (amount): "))
 client_one_time =      float(input("Time:               "))
 client_one_rate =      float(input("Rate:               "))

 amount = (client_one_principal*(1+(client_one_rate/100))**client_one_time)
 interest = round((amount - client_one_principal),2)
 print("Compound Interest: "+str(interest)+"\n")

 client_two_principal = float(input("Principle (amount): "))
 client_two_time =      float(input("Time:               "))
 client_two_rate =      float(input("Rate:               "))

 amount = (client_two_principal*(1+(client_two_rate/100))**client_two_time)
 interest = round((amount - client_two_principal),2)
 print("Compound Interest: "+str(interest)+"\n")

 client_three_principal = float(input("Principle (amount): "))
 client_three_time =      float(input("Time:               "))
 client_three_rate =      float(input("Rate:               "))

 amount = (client_three_principal*(1+(client_three_rate/100))**client_three_time)
 interest = round((amount - client_three_principal),2)
 print("Compound Interest: "+str(interest))

    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateCompoundInterest() and run > python monkeyCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN

#calculateCompoundInterest()
