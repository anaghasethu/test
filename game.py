
import time
import random

print "----WELCOME TO QUIZ----";

name = raw_input("What's your name?\n");
print "\nHello "+name+".Let's Start";
print "\nHere are the instructions.\n1.All the questions are not multiple choice\n2.In case of questions other than MCQs you need to write it in small letters.\n3.Only 10 questions will be asked.\n4.At the end of the quiz your score will be displayed.\n5. In case of more than 2 word write with space";
correct=0;
time.sleep(2);

for x in range (1,6):
	qno = random.randint(1,6);
	que = ["Capital of India ","In india agriculture of jute is maximum on which delta area","lake Baikal is located in","T20 world cup is associated with which game","french open is associated with 	which sports","first indian women to go to space","first indian in space"]
	ansl = ["delhi","ganga","japan","cricket","tennis","kalpana chawla","rakesh sharma"];
	print "\n"+que[qno];
	ans = raw_input(">>>");
	if ans == ansl[qno]:
		correct=correct+1;
	else:
		correct=correct+0;

print "\n"+name+",your score: ";
print correct;



