'''
QUIZ MASTER PROJECT  (4pts)
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
while True:
    points = 0
    print("Welcome to my humble quiz\nLet's hope you get more than two right")
    try:
        guess = int(input("1. What year did Javascript get invented?\n"))
        if guess == 1995:
            print("Yes, Javascript was made in the span of a week in 1995")
            points += 1
        else:
            print("No, Javascript was made in the span of a week in 1995")
    except ValueError:
        print("Be real, insert a year using arabic numerals")
    guess = input("2. What is the default desktop environment of Ubuntu?\n")
    if guess.lower() == "gnome":
        print("That's right, since 2017 Ubuntu Linux has used Gnome as its default desktop environment")
        points += 1
    else:
        print("Wrong, since 2017 Ubuntu Linux has used Gnome as its default desktop environment")
    guess = input("3. Who of the following won the NBA Finals MVP in 2019?\nA: Steph Curry\nB: Kawhi Leonard\nC: Kevin Durant\nD: James Harden\nE: Wilt Chamberlain\n")
    if guess.lower() == "b":
        print("Bullseye, Kawhi Leonard was the finals MVP in 2019 for winning the championship with the Toronto Raptors")
        points += 1
    elif guess.lower() == "e":
        print("Bruh he hasn't played since the 70's :|, I'm revoking all your prior points for that one. Kawhi was the right choice")
        points = 0
    else:
        print("Not even close, Kawhi Leonard was the finals MVP in 2019 for winning the championship with the Toronto Raptors")
    guess = input("4. True or False! Apple completed it\'s transition from PowerPC to Intel CPUs in 2002\n")
    if guess.lower() == "false":
        print("Keen eye, Apple finally ditched the RISC PowerPC architecture in 2006")
        points += 1
    elif guess.lower() == "true":
        print("Just a little off, Apple finally ditched the RISC PowerPC architecture in 2006")
    else:
        print("Just because you can doesn't mean you should. -1 point to your name")
        points -= 1
    guess = input("5. What book (which has been adapted into three movies) has been described by many as Star Wars before Star Wars?\n")
    if guess.lower() == "dune":
        print("Wise one you are, Frank Herbert's Dune (1965) has been routinely called the Star Wars before Star Wars since 1977 due its immense influence on the space franchise with it's use of then new sand-born rebelion, autocratic space empires, and planetary fast travel just to name a few")
        points += 1
    else:
        print("Unlucky, Frank Herbert's Dune (1965) has been routinely called the Star Wars before Star Wars since 1977 due its immense influence on the space franchise with it's use of then new sand-born rebelion, autocratic space empires, and planetary fast travel just to name a few")
    try:
        guess = int(input("6. In what year did the Americas get their name?\n"))
        if guess == 1507:
            print("Nice, some German bloke named the continent America in 1507 after Amerigo Vespucci")
            points += 1
        else:
            print("Get a better memory, some German bloke named the continent America in 1507 after Amerigo Vespucci")
    except ValueError:
        print("Great, now you gotta start over. Use arabic numerals next time")
    guess = input("7. Who of following won the the first UEFA Champions League?\nA: Real Madrid\nB: Manchester City\nC: Juventus\nD: Marseille\nE: Liverpool\nF: Chelsea\nG: AC Milan\nH: Galatasaray\n")
    if guess.lower() == "d":
        print("Smart one aren't you, Marseille was the first winner of the UEFA Champions League, the renamed competition succeeding the European Cup")
        points += 1
    else:
        print("Watch the language, Marseille was the first winner of the UEFA Champions League, the renamed competition succeeding the European Cup")
    guess = input("8. True or False! Punchcards were the first form of software storage\n")
    if guess.lower() == "true":
        print("Spot on, Punchcards were the first and primary way to store computer data until the popularization of the floppy disk")
        points += 1
    elif guess.lower() == "false":
        print("Misinput? Punchcards were the first and primary way to store computer data until the popularization of the floppy disk")
    else:
        print("Are you serious? Minus 2 points from your total")
        points -= 2
    guess = input("9. What is the Wayland drop-in replacement for the i3 window manager?\n")
    if guess.lower() == "sway":
        print("Amazing, the Sway window manager is a wayland compatible tiling window manager built to be the future replacement the old i3 window manager")
        points += 1
    else:
        print("Wrong, the Sway window manager is a wayland compatible tiling window manager built to be the future replacement the old i3 window manager")
    try:
        guess = float(input("10. What will be the next Python 3.x version?\n"))
        if guess == 3.13:
            print("You ain't a stormtrooper, the current stable release of Python 3 is 3.12.7 and 3.13 will release in a few days")
            points += 1
        else:
            print("Off by a smidge, the current stable release of Python 3 is 3.12.7 and 3.13 will release in a few days")
    except ValueError:
        print("I'm done with you, start from scratch")
        points -= points
    guess = input("11. What was the first programming high-level language?\n")
    if guess.lower() == "fortran":
        print("Brilliant! Fortran was released in 1957 as the very first human-readable programming language")
        points += 1
    else:
        print("Wrong, Fortran was released in 1957 as the very first human-readable programming language")
    print("You got", points, "questions right out of 11")

    grade_input = points / 11

    if grade_input >= 0.9:
        letter = "A"
        print("Your grade:", letter)
        print("You looked at the code didn\'t you?")
        break
    elif grade_input >= 0.75:
        letter = "B"
        print("Your grade:", letter)
        print("Great work")
        break
    elif grade_input >= 0.6:
        letter = "C"
        print("Your grade:", letter)
        print("Better than expected")
        break
    elif grade_input >= 0.45:
        letter = "D"
        print("Your grade:", letter)
        print("Not horrible")
        break
    elif grade_input <= 0:
        letter = "Z-"
        print("Your grade:", letter)
        print("How on earth did you get negative right? Start the quiz over and you better not see this again")
    else:
        letter = "F"
        print("Your final grade:", letter)
        print("Bruh, that skull must be entirely occupied by echos")
        break

