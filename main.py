import random
import datetime



'''
User Management created by Andrei Ursu

Waiting for the readFile method.
'''
def validateUser(userName, pwd):
	#data = readFile("userLog.bin")
	valid = True
	try:
		with open("userLog.bin","r") as file:
			if userName and pwd in file.read():
				print("They are in the file")
			else:
				print("User not found.")
				valid = False
	except IOError:
		valid = False

	return valid

def addUser(userName, pwd):
	success = True
	exists = validateUser(userName, pwd)
	#data = readFile("userLog.bin")

	while(exists != True):
		try:
			with open("userLog.bin","a") as file:
					s_arg = "<USER>\n userName="+userName+"\n password="+pwd+"\n</USER>\n"
					file.write(s_arg)
					exists = True
					break
		except IOError:
			print("Unable to open file.")
			success = False

	return success

'''
addUser("andreiu","cheese1")

print(validateUser("andreiu","cheese1"))

print("\n")
valid = validateUser("andreiu","cheese1")
print("Valid",str(valid))

print("\n")
print(validateUser("michaelg","poop1"))
'''




def playGame(probluem):
	int1 = random.Randint(0, 100)
	int2 = random.Randint(0, 100)
	

	#create probluems starting at division, to addition)
	if(probluem >= 6):
		print("Probluem " + (probluem + 1) + "! :D")
		number = input(int1 + " / " + int2 + " = ")
		if(int2 == 0):
			playGame(probluem)
		elif(number == (int1 / int2)):
			return
		elif(number != (int1 / int2)):
			Print("take your time, there's no rush.")
			playGame(probluem)


	elif(probluem >= 4):
		print("Probluem " + (probluem + 1) + "! :D")
		number = input(int1 + " * " + int2 + " = ")
		if(number == (int1 * int2)):
			return 
		elif(number != (int1 - int2)):
			Print("TRY AGAIN HURRY THERES NO TIME!!!!!!")
			playGame(probluem)


	elif(probluem >= 2):
		print("Probluem " + (probluem + 1) + "! :D")
		number = input(int1 + " - " + int2 + " = ")
		if(number == (int1 - int2)):
			return 
		elif(number != (int1 - int2)):
			Print("Do IT AGAIN FASTER!!!")
			playGame(probluem)


	elif(probluem >= 0):
		print("Probluem " + (probluem + 1) + "! :D")
		number = input(int1 + " + " + int2 + " = ")
		if(number == (int1 + int2)):
			Print("NOOO GO AGAIN!!!!!!")
			return
		elif(number != (int1 + int2)):
			Print("Thats Wrong!")
			playGame(probluem)






startTime = datetime.datetime.now().time()
for n in range(0, 12):
	playGame(n)

endTime = datetime.datetime.now().time()

playTime = endTime - startTime
print(playTime)








# display menu and process menu options
# display choices to users depending on if user is logged in.
# If activeUser="" then only show login and quit options.
# If activeUser!="" then welcome logged in user and display logout and menu options.
# Validate user input and return user choice
# menu options: login/logout, play game, display scores, quit
def Menu ():
    activeuser = ""
    activeuser = input("Enter your username: ")
    if (activeuser != ""):
        menu = ["
        print("Welcome user" + activeuser)
    else:
        print()
def main():
    return 1;
if __name__ == '__main__':
    main()


