ZeroDivisionError
result = 10 / 0 
print(result)
# Raises ZeroDivisionError

ValueError

num = int("abc")
# Raises ValueError

FileNotFoundError
with open("nonexistent_file.txt", "r") as file:
        content = file.read()   # Raises FileNotFoundError

IndexError
my_list = [1, 2, 3]
value = my_list[1]  # No IndexError, within range
missing = my_list[5]  # Raises IndexError

KeyError
my_dict = {"name": "Alice", "age": 30}
value = my_dict.get("city")  # No KeyError, using .get() method
missing = my_dict["city"]  # Raises KeyError

TypeError
result = "hello" + 5   
# Raises TypeError

AttributeError
text = "example"
length = len(text)  # No AttributeError, correct method usage
missing = text.some_method()  # Raises AttributeError

ImportError
This error is encountered when an attempt is made to import a module that is unavailable. 


Handling Exceptions
Python has a handy tool called try and except that helps us manage exceptions.

Try and Except: You can use the try and except blocks to prevent your program from crashing due to exceptions.

Here's how they work:

The code that may result in an exception is contained in the try block.

If an exception occurs, the code directly jumps to except block.

In the except block, you can define how to handle the exception gracefully, like displaying an error message or taking alternative actions.

After the except block, the program continues executing the remaining code.

Attempting to divide by zero
# using Try- except 
try:
    # Attempting to divide 10 by 0
    result = 10 / 0
except ZeroDivisionError:
    # Handling the ZeroDivisionError and printing an error message
    print("Error: Cannot divide by zero")
# This line will be executed regardless of whether an exception occurred
print("outside of try and except block")

try:
except:
  else:
finally:

Try Except Specific
A specific try except allows you to catch certain exceptions and also execute certain code depending on the exception.
This is useful if you do not want to deal with some exceptions and the execution should halt.
It can also help you find errors in your code that you might not be aware of. Furthermore, it can help you differentiate responses to different exceptions.
In this case, the code after the try except might not run depending on the error.

try:
    # code to try to execute
except (ZeroDivisionError, NameError):
    # code to execute if there is an exception of the given types
    
# code that will execute if there is no exception or a one that we are handling

# potential code before try catch

try:
    # code to try to execute
except ZeroDivisionError:
    # code to execute if there is a ZeroDivisionError
except NameError:
    # code to execute if there is a NameError
    
# code that will execute if there is no exception or a one that we are handling

# potential code before try catch

try:
    # code to try to execute
except ZeroDivisionError:
    # code to execute if there is a ZeroDivisionError
except NameError:
    # code to execute if there is a NameError
except:
    # code to execute if ther is any exception
    
# code that will execute if there is no exception or a one that we are handling


a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=",a)
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")


Try Except Else and Finally
else allows one to check if there was no exception when executing the try block. This is useful when we want to execute something only if there were no errors.
finally allows us to always execute something even if there is an exception or not. This is usually used to signify the end of the try except.

# potential code before try catch

try:
    # code to try to execute
except ZeroDivisionError:
    # code to execute if there is a ZeroDivisionError
except NameError:
    # code to execute if there is a NameError
except:
    # code to execute if ther is any exception
else:
    # code to execute if there is no exception
    
# code that will execute if there is no exception or a one that we are handling



# potential code before try catch

try:
    # code to try to execute
except ZeroDivisionError:
    # code to execute if there is a ZeroDivisionError
except NameError:
    # code to execute if there is a NameError
except:
    # code to execute if ther is any exception
else:
    # code to execute if there is no exception
finally:
    # code to execute at the end of the try except no matter what
    
# code that will execute if there is no exception or a one that we are handling

Try Except Else and Finally Example
a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)


a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)
finally:
    print("Processing Complete")

