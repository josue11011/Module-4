###################################################
#Josue Cifuentes
#CIS 225
#1) Number of errors found: 7
#2) Error Types: Syntax error on first line the " should be '.
#                Syntax error on first line an extra =
#                Syntax error on first line missing ) after int.
#                Syntax error on third line the ' should be " because of the 's
#                Syntax error on second line missing a :
#                Syntax error on fourth line an extra &
#                Syntax error on sixth line unnecessary :
# Program Name: branching.py
# Purpose of a program: A time traveler has suddenly appeared in your classroom!
# The travelor enters his/her year of origin
# Program returns a greeting message according to the year.
# Distant Past: Before 1900
# Present Era-Years between 1900-2020
# Far Future: After 2020

year = int(input('Greetings! What is your year of origin? '))
        
#                                                 #
#       1900                2020                  #  
#=========|===================|================== #
#   I              II              III            #
    
#for the region I    
if year <= 1900: 
    print ("Woah, that's the past!")
elif year > 2020: 
    print ("Far out, that's the future!!")
#for the region II
#elif year > 1900 & year < 2020:
elif year > 1900 & year < 2020:  
    print("That's totally the present!")
#the rest area: for the region III
#should use  else: 
