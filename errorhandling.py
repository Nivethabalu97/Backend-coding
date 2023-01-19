a=int(input("enter first number"))
b=int(input("enter second number"))
try:
    print("file opened")
    print(a/b)
    number=int(input("enter a number"))
    print(number)
except ZeroDivisionError as error:
    print("Sorry, Error has occured and the error message is:", error)
except ValueError as error:
    print("Sorry, Error has occured and the error message is:", error)
except Exception as error:
    print("Sorry, Error has occured and the error message is:", error)
finally:
    print("file closed")
print("thankyou")