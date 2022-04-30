from art import logo
from os import system,name
import sys
import calc_inc

def clear_console():
     if(name == 'nt' or name == 'dos'):
          system('cls')
     else:
          system('clear')

def calculate(opt,n1,n2):
     function = calc_inc.operations[opt]
     result = function(n1,n2)
     return result    

def calculator():
     cont_calc = True
     
     first_num = int(input("Enter first number: "))
     for symbol in calc_inc.operations:
          print(symbol)

     while(cont_calc):      
          operator = input("Select an opertaion: ")     
          next_num = int(input("Enter next number: "))
          result = calculate(operator,first_num,next_num)
          print(f"{first_num} {operator} {next_num} = {result}")
          choice = input("Type 'y' to continue calculation, type 'n' to start a new calculation or type 'e' to exit: ").lower()
          if(choice == 'y'):
               first_num = result
          elif(choice == 'n'):
               clear_console()
               calculator()
          elif(choice == 'e'):
               clear_console()
               sys.exit()
          else:
               print("Invalid input, Try again")
               cont_calc = False
 
print(logo)
print("Simple Calculator with Python")
print("developer: Dinith Kumudika(https://github.com/DinithKumudika)\n")
calculator()
