
from random import randint

print "------GUESS ME IF YOU CAN------"


number = randint(1,10);
guess = -1;
while guess != number:
	num = int(raw_input(">>>"));
	if num != number:
		print "Sorry..Wrong guess!!"
	else:

		print "Congrats.. Right guess!!"
		break;
	 	




