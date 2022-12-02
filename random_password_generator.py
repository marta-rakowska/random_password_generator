"""This program generates a random password of 8 characters. Each time the program is run,
a new password is generated randomly. The passwords generated are 8 characters long and include
2 uppercase letters from A to Z, 2 lowercase letters from a to z, 2 digits from 0 to 9, 2 punctuation signs."""

import random

#A function do shuffle all the characters of a string
def shuffle(string):
  temp_list = list(string)
  random.shuffle(temp_list)
  return ''.join(temp_list)

#Main program starts here
uppercase_letter_1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercase_letter_2=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
lowercase_letter_1 = chr(random.randint(97,122)) #Generate a random lowercase letter (based on ASCII code)
lowercase_letter_2 = chr(random.randint(97,122)) #Generate a random lowercase letter (based on ASCII code)
digit_1 = chr(random.randint(48,57)) #Generate a random digit (based on ASCII code)
digit_2 = chr(random.randint(48,57)) #Generate a random digit (based on ASCII code)
punctuation_sign_1 = chr(random.randint(33,47)) #Generate a random punctuation sign (based on ASCII code)
punctuation_sign_2 = chr(random.randint(58,64)) #Generate a random punctuation sign (based on ASCII code)

#Generate password using all the characters, in random order
password = uppercase_letter_1 + uppercase_letter_2 + lowercase_letter_1 + lowercase_letter_2 + digit_1 + digit_2\
           + punctuation_sign_1 + punctuation_sign_2
password = shuffle(password)

#Ouput
print(password)