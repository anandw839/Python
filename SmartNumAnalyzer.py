import os
import logging

logger=logging.getLogger(__name__)

def analyze_number(num):
    if num>0:
        logger.info("Number is Positive")
    elif num<0:
        logger.info("Number is Negative")
    else:
        logger.info("Number is zero")

    if num % 2 == 0:
        print("Number is Even")
    else:
        print("Number is Odd")

    if num %3 ==0 and num % 5 ==0:
        logger.info("Divisible by 3 and 5")
        print("FuzzBuzz")
    elif num %3 == 0:
        print("Divisible by 3 & 5")
        print("Fuzz")
    elif num % 5 == 0:
        print("Divisible by 3 & 5")
        print("buzz")
    else:
        print("Not divisible by 3 and 5")

while True:
    user_input= input("\n Enter a number or type 'exit' to quit")

    if user_input.lower=="exit":
        print("Program Ended.")
    break

try:
    number= int(user_input)
    analyze_number(number)
except ValueError:
    logger.info("Invalid input. Please enter a valid number.")