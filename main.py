# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def multiply(num1,num2):

   if num2==1:
        return num1
   else:
    return num1 + multiply(num1,num2-1)

print(multiply(6,8))