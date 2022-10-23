###################################################
#Josue Cifuentes
#CIS 225
#1) Number of errors found: 5
#2) Error Types:SyntaxError First line missing a " at the end of ?
#				SyntaxError Second line [ should be (
#				SyntaxError fourth line elif should be else:
#				SyntaxError Fifth line neds an indentation
#				SyntaxError Second line Arrri! should be Arrr!
#####################################################
# Program Name: pirate.py
# Purpose of a program:
# User can be screened by the greeting message user enters as: a pirate or pirate hater
# Pirates greet each other with a password.
# If the greeting is matched to Arrr!,the user is identified as a pirate.
# Otherwise, the user is a hater of pirates.

greeting = input("Hello, possible pirate! What's the password?")
if greeting in ("Arrr!"):
	print("Go away, pirate.")
else:
	print("Greetings, hater of pirates!")
