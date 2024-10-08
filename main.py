# Thayer Yang
# 16 SEP 2024
# Mad Lib Practice

#Greetings list
greetings = ["Ahola ", "Bonjour ", "Ciao ", "Do you know me ", "Ello ", "Finally nice to meet you ", "Greetings ", "Hello ", "I know who you are ","Jello ", "Konichiwa ", "Lovely meeting you ", "Morning to you ", "Namaste ", "Oh, hey  ", "Pleasure to meet you ","Quite an honor to meet you ", "Really nice to meet you ", "Shalom ", "Today I welcome you ", "Unique name you've got ", "Very nice to meet you ", "Well well, finally get to meet you ", "Xylophones must be your favorite instrument then huh ","Yo ","Zero clue you were "]

#Byes list
byes = ["Adios ", "Be safe ","Catch you later ","Don't worry, see you later ", "Eventually we'll meet again ", "Farewell ","Goodbye ","Hasta manana ", "I'll see you later", "Join me tomorrow ", "Kill it out there ", "Later ", "Meet you tomorrow ", "Nice seeing you again ", "Oh, I'll catch up with you tomorrow ", "Party with me after you're done ", "Quick you gotta go ", "Really hope to see you again " , "Sayonara ", "Time to go. See you around ", "Unload your stuff soon. Later ", "Very nice seeing you again ", "Well, go on ", "X-rays are coming in now, see you later ", "You'll see me soon ", "Zero time left, I'll see you around "]

#name inputs
first_name = input("What is your first name?: ")
last_name = input("What is your last name?: ")

#traversal for greetings
#Matches greetings with the letter of the first name
i = 0
for x in greetings:
    greet = greetings[i]
    if first_name.upper()[0:1] == greet.upper()[0:1]:
        greeting_index = i
    i = i+1
    #print(i)
#print(greeting_index)
    
#Mad lib inputs
verb1 = input("Enter an verb without an -ing: ")
noun1 = input("Enter a place: ")
verb2 = input("Enter a verb that ends in -ing: ")
adjective1 = input("Give an adjective to describe the weather: ")
noun2 = input("Enter a handheld object: ")
adjective2 = input("Enter a color: ")
adjective3 = input("Enter another color: ")
noun3 = input("Enter a 1 digit number: ")
noun4 = input("Enter a 2 digit number: ")

#messages set up
greet_message = (f'{greetings[greeting_index]}{first_name.capitalize()} {last_name.capitalize()}.')

if len(first_name) >= 10 and len(last_name) >= 10:
    greet_message = greet_message+" Long name you got there "+first_name+"."
elif len(first_name) >= 10:
    greet_message = greet_message+" Long first name you got there "+first_name+"."
elif len(last_name) >= 10:
    greet_message = greet_message+" Long last name you got there "+first_name+"."



#Lines may be different depending on name conditions.
#Line with verb action in the place
line1 = ""
if last_name.lower()[0:1] == "q" or last_name.lower()[0:1] == 'p' or last_name.lower()[0:1] == 'd':
    line1 = f"You've been selected to {verb1.lower()} at {noun1}. "
    if noun1.lower() == 'australia':
        line1 = line1.replace('. ', "mate. ")
    elif noun1.lower() == 'ireland':
        line1 = line1.replace('. ', 'laddie. ')

elif noun1.lower() == 'australia':
    line1 = f'We get to {verb1.lower()} in the {noun1} today mate. '

elif noun1.lower() == 'ireland':
    line1 = f'We get to {verb1.lower()} in the {noun1} today laddie. '
else:
    line1 = f"We get to {verb1.lower()} in the {noun1} today. "

#Line with describing the weather
line2 = ""
if last_name.lower()[0:1] == "x" or last_name.lower()[0:1] == 'a' or last_name.lower()[0:1] == 's':
    line2 = f"Kind of crazy since the weather recently has been {adjective1.lower()}. "
else:
    line2 = f"I don't know what you'll do when the weather starts to be {adjective1.lower()}. "

#Line with the object and it's possible colors
line3 = ""
if first_name.lower()[0:1] == "w" or first_name.lower()[0:1] == 'i' or first_name.lower()[0:1] == 'j':
    line3 = f"Its the {noun2.lower()} you wanted, but in {adjective2}. Weirdly the label says \"{adjective3.upper()}\" though. "
else:
    line3 = f"Its the {noun2.lower()} from the {noun1}. Its suppose to be {adjective2.lower()} because it says \"{adjective2.upper()}\" on the label but its {adjective3}. "

#Bye message
#message output is dependant on the input of the first name
i = 0
for x in byes:
    bye = byes[i]
    if last_name.upper()[0:1] == bye.upper()[0:1]:
        bye_index = i
    i = i+1
#finalized bye message
bye_message = f"{byes[bye_index]}{first_name.capitalize()}."

#print to make space
print("")

#Full mad lib script
madlipScript = f"{greet_message} {line1}{first_name.capitalize()} how do you feel? I know you've also gone {verb2.lower()} in the mornings now. {line2}\nHere, I got a present for you. {line3}Don't worry its only {noun3} of {noun4} you'll get. Good luck in the {noun1} today {first_name.capitalize()}. {bye_message}"

#Additional Story switch ups to get it random
if first_name.lower()[0:1] == 'b' or first_name.lower()[0:1] == 'p' or last_name.lower()[0:1] == 'y':
    madlipScript = madlipScript.replace('mornings', 'evenings')

if first_name.lower()[0:1] == 'w' or last_name.lower()[0:1] == 'd' or last_name.lower()[0:1] == 'h':
    madlipScript = madlipScript.replace('today', 'tomorrow')




print(madlipScript)