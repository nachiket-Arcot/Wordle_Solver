


#Opens the wordlist
file = open("words.txt")
for lines in file:
    words = file.readlines()


#Inputs of how many letters there are
correctnumber = int(input("How many correctly placed letters do you have ?: "))
incorrectplacenumber = int(input("How many incorrectly placed letters do you have ?: "))
incorrectletternumber = int(input("How many incorrect letters do you have ?: "))


#If letter is correctly placed
wellplacedlist = ["?","?","?","?","?"]
correct_position = {}
if correctnumber != 0:
    for trials in range(correctnumber):
        correctplaceletter = str(input("Enter the correctly placed letters here: "))
        correctplaceposition = int(input("Enter the position of the letter here: "))
        correct_position[correctplaceposition] = correctplaceletter
        wellplacedlist[correctplaceposition] = correctplaceletter
        print(wellplacedlist)
else:
    correct_position = {}

                     
#If letter is in the word but incorrectly placed
if incorrectplacenumber != 0:
    misplacedlist = []
    for num in range(incorrectplacenumber):
        incorrectplaceletter = str(input("Enter the incorrectly placed letters here: "))
        misplacedlist.append(incorrectplaceletter)
else:
    misplacedlist = []



#If letter isn't in the word
if incorrectletternumber != 0:
    incorrectlist = []
    for num in range(incorrectletternumber):
        wrongletters = str(input("Enter the letters that aren't in the word here: "))
        incorrectlist.append(wrongletters)
else:
    incorrectlist = []
 

#Finds word that satisfies all 3 conditions
filtered_word = []
for result in words:
    resultlist = list(result)
    if all(resultlist[pos] == letter for pos, letter in correct_position.items()) and all(item in resultlist for item in misplacedlist) and  not set(incorrectlist) & set(resultlist):
        filtered_word.append(''.join(resultlist))

print(filtered_word)