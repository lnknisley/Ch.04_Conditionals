# 4.0 Jedi Training (40pts)  Name:________________
#BELOW EACH PROGRAM LIST THE MISTAKES FOUND

#1. Make the following program work. (3 mistakes)  (3pts)

    midichlorians = float(input("Enter midichlorian count: "))
    if midichlorians > 10000:
        print("You have serious Jedi potential")
    else:
        print("Jedi, you will never be.")
#1 There should be a colon after 10000
#2 There's a missing parentheses for the float function
#3 There's a stateless elif instead of what should be an else

# 2. Make the following program work. (3 mistakes)  (3pts)
   
   x = int(input("Enter a number: "))
   if x == 3:
       print("You entered 3")

#1 two equal signs (==) needs to be used in place of a single sign
#2 there needs to be a colon after three
#3 an int function should be wrapped around the input function in order to prevent string-number comparison and thus an error

# 3. Make the following program work. (4 mistakes)  (4pts)
   
   answer = input("What is the name of Poe Dameron's Droid? ")
   if answer == "BB8":
       print("Correct!")
   else:
       print("Incorrect! It is BB8.")

#1 answer variable is not used, the undefined a variable is used in its place
#2 the equals sign in the if statement must be made into the correct double equal-sign operator
#3 else is on the wrong indention level, it must be on the same plane as the prior if statement
#4 a colon must come after else

# 4. Make the following program work. (4 mistakes) (4pts)
   
   x = input("Name one of the top 3 greatest Jedi.")
   if x == "Yoda" or x == "Luke Skywalker" or x == "Obi-Wan Kenobi":
       print("That is correct!")


#1 the print function lacks parentheses
#2 the x variable is unused, the undefined jedi variable is used in its place
#3 Quotation marks must be placed around each of the names that would be matched in the if statement
#4 the comparison of x == value must be placed after each or operator


# 5. Make the following program work whether they enter a, A, Jedi Master or jedi master
#    Print "Not a choice!" if they don't choose any of the three and set sensitivity to blank text.  (6pts)
   
   print("Welcome to the Jedi Academy!")
   A = "Jedi Master"
   B = "Sith Lord"
   C = "Droid"
   print(A + "\n" + B + "\n" + C)

   user_input = input("Choose a character?")
   sensitivity = 0

   if user_input.lower() == A.lower() or user_input.lower() == "a":
       sensitivity = 1000
   elif user_input.lower() == B.lower()  or user_input.lower() == "b":
       sensitivity = 900
   elif user_input.lower() == C.lower()  or user_input.lower() == "c":
       sensitivity = 0
   else:
       print("Not a choice!")
       sensitivity = ""

   print("Sensitivity: ", sensitivity)




'''
6. NUMBER ANALYSIS PROGRAM  (10pts)
-----------------------
Create a program that asks the user for a number and then analyzes it to determine if it is:
1.) odd or even
2.) positive, negative or zero
3.) inclusively between -100 and +100

A small report will then be printed. Use the following to test your program:

In: 32  
Out:  Test 1: Even
    Test 2: Positive
    Test 3: Inclusive

In: -123  
Out:  Test 1: Odd
    Test 2: Negative
    Test 3: Exclusive
'''
while True:
    try:
        x = int(input("Input any real integer: "))
        if x % 2 == 0:
            print("Even")
            if x > 0:
                print("Positive")
                if 100 >= x >= -100:
                    print("Inclusive")
                    break
                else:
                    print("Exclusive")
                    break
            if x < 0:
                print("Negative")
                if 100 >= x >= -100:
                    print("Inclusive")
                    break
                else:
                    print("Exclusive")
                    break
            if x == 0:
                print("Zero")
                print("Inclusive")
                break
        else:
            print("Odd")
            if x > 0:
                print("Positive")
                if 100 >= x >= -100:
                    print("Inclusive")
                    break
                else:
                    print("Exclusive")
                    break
            if x < 0:
                print("Negative")
                if 100 >= x >= -100:
                    print("Inclusive")
                    break
                else:
                    print("Exclusive")
                    break
            if x == 0:
                print("Zero")
                print("Inclusive")
                break
    except ValueError:
        print("Did you not follow the directions? Enter an INTEGER!")

'''
GRADING 2.0    (10pts)
-------------------
Copy your Grading 1.0 program below and then modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''
sem = int(input("Enter your semester grade: "))
final = int(input("Enter your final grade: "))
final_int = int(input("How much is that final exam worth?: "))
final_value = final_int * (10 ** -2)
overall = (final * final_value) + (sem * (1 - final_value))
#Floors, A = 90, B = 80, C = 70, D = 60, F <= 60
letter = ""
if overall >= 90:
    letter = "A"
    print("Your final grade:", overall, letter)
elif overall >= 80:
    letter = "B"
    print("Your final grade:", overall, letter)
elif overall >= 70:
    letter = "C"
    print("Your final grade:", overall, letter)
elif overall >= 60:
    letter = "D"
    print("Your final grade:", overall, letter)
else:
    letter = "F"
    print("Your final grade:", overall, letter)
    print("Bruh, that skull must be occupied entirely by echos. Do us a favor and ship yourself out to Johnston")

