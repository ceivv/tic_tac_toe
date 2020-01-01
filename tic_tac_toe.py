import random 
import os

one=1
two=2
three=3
four=4
five=5
six=6
seven=7
eight=8
nine=9

def main_frame():
	print("\t\t","_"*10," TIC TAC TOE ","_"*10)
	print("""
	         ______   _____    ___    _     __
	        |  ___/  |  __/   /   |  | |   / /
	        | |      | |___  / /| |  | |  / /
	        | |      |  __/ /_/ | |  | | / /
	        | |____  | |___     | |  | |/ /
	        |_____/  |____/     |_|  |___/\n""");
def update(one,two,three,four,five,six,seven,eight,nine):
	print(f"""\t
		{one}|{two}|{three}
		_____
		{four}|{five}|{six}
		_____
		{seven}|{eight}|{nine}""")

def computer_plays(x):
	global one
	global two
	global three
	global four
	global five
	global six
	global seven
	global eight
	global nine
	if x==1:
		one='X'
	if x==2:
		two='X'
	if x==3:
		three='X'
	if x==4:
		four='X'
	if x==5:
		five='X'
	if x==6:
		six='X'
	if x==7:
		seven='X'
	if x==8:
		eight='X'
	if x==9:
		nine='X'

def human_plays(x):
	global one
	global two
	global three
	global four
	global five
	global six
	global seven
	global eight
	global nine
	if x==1:
		one='O'
	if x==2:
		two='O'
	if x==3:
		three='O'
	if x==4:
		four='O'
	if x==5:
		five='O'
	if x==6:
		six='O'
	if x==7:
		seven='O'
	if x==8:
		eight='O'
	if x==9:
		nine='O'


#main program
main_frame()
print("Press Enter to start..")
input()
print("\nYOU ARE 'O' I AM 'X'!")
my_list=[1,2,3,4,5,6,7,8,9]
pos=99
draw=0
while 1:
	while 1 :
		win=0 #computer wins
		os.system('cls')
		plays=random.choice(my_list)	
		computer_plays(plays)
		my_list.remove(plays)
		if one==two and one==three and two == three:
			break
		if four==five and four==six and six==five :
			break
		if seven==eight and seven==nine and nine == eight :
			break
		if one == four and one == seven and four == seven :
			break
		if two == five and two == eight and eight == five :
			break
		if three == six and three == nine and nine == six :
			break
		if one == five and one == nine and nine == five :
			break
		if three == five and three == seven and seven == five :
			break
		if draw==4:
			win=111
			break

		win=1 #human wins

		update(one,two,three,four,five,six,seven,eight,nine)
		pos=int(input("\nYOUR TURN: "))
		human_plays(pos)
		my_list.remove(pos)
		print(draw)
		if one==two and one==three and two == three:
			break
		if four==five and four==six and six==five :
			break
		if seven==eight and seven==nine and nine == eight :
			break
		if one == four and one == seven and four == seven :
			break
		if two == five and two == eight and eight == five :
			break
		if three == six and three == nine and nine == six :
			break
		if one == five and one == nine and nine == five :
			break
		if three == five and three == seven and seven == five :
			break
		draw+=1
		if draw==5:
			win=111
			break
		print(draw)

	update(one,two,three,four,five,six,seven,eight,nine)
	if win==0 :
		print("\a\a\aI (Computer) WON !")
	elif win == 1:
		print ("\a\a\aYOU (Human) WON !")
	else:
		print("it is a draw")
	input()








