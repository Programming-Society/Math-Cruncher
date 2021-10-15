import random
import datetime

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
def main():

    return 1;



