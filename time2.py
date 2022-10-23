###################################################
#Josue Cifuentes
#CIS 225
#1) Number of errors found:3
#2) Error Types: SyntaxError line 2 should say number of hours not nours
#                SyntaxError line 4 should say wait_time missing t
#                SyntaxError line 5 should say time_when_to_start
####################################################
# Program Name: time2.py
# Purpose of a program:
# User inputs current time and hours to wait.
# Then program returns the time user's waiting tiime ends.

str_time = input("What time is it now?")
str_wait_time = input("What is the number of hours to wait?")
time = int(str_time)
wait_time = int(str_wait_time)

time_when_to_start = time + wait_time
print(time_when_to_start)
