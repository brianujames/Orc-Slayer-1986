#!/www/your/server/here
print "Content-Type: text/html"
print
print "<head><title>Orc Slayer 1986</title></head>"
print "</head><body>"
print "<img src=\"img/orc-slayer-1986.jpg\" width=\"400\"><br>"

import sys
import random
import time
import urllib
import cgi
import cgitb; cgitb.enable()  # for troubleshooting
form = cgi.FieldStorage() # instantiate only once!

def getTotal(attr, defaultval):
    totalNumber = form.getfirst(attr, None)
    if totalNumber == None:
        totalNumber = defaultval
    else:
        totalNumber = int(totalNumber)
    return totalNumber

orcHealth = getTotal('orcHealth', 500)
yourHealth = getTotal('yourHealth', 500)
winRecord = getTotal('winRecord', 0)
loseRecord = getTotal('loseRecord', 0)
roundNumber = getTotal('roundNumber', 1)

name = form.getfirst('name', 'None')
name = cgi.escape(name)
if name == 'None':
	loop = False
elif 'butt' in name:
	print "Not Butts allowed"
	exit()
else:
	loop = True

def getName(button):
	print "<form method='post' action='orc-slayer-1986.py'>"
	if name == 'None':
		print "Name: <input type='text' name='name'>"
	print "<input type='submit' value='%s'>" % button
	print "<input type='hidden' name='start' value='1'>"
	print "</form>"	
	return
		
def printForm(button):
	print "<form method='post' action='orc-slayer-1986.py'>"
	print "<input type='hidden' name='name' value='%s'>" % name
	print "<input type='hidden' name='orcHealth' value='%s'>" % orcHealth
	print "<input type='hidden' name='yourHealth' value='%s'>" % yourHealth
	print "<input type='hidden' name='winRecord' value='%s'>" % winRecord
	print "<input type='hidden' name='loseRecord' value='%s'>" % loseRecord
	print "<input type='hidden' name='roundNumber' value='%s'>" % roundNumber
	print "<input type='hidden' name='fight' value='1'>"
	print "<input type='submit' value='%s'>" % button
	print "</form>"	
	startbattle = 2
	return

def makeTotals(win, loss):
	global winRecord 
	winRecord = winRecord + win
	global loseRecord 
	loseRecord = loseRecord + loss
	global orcHealth 
	orcHealth = 500
	global yourHealth
	yourHealth = 500
	global roundNumber
	roundNumber = roundNumber + 1
	return
	
if loop == False:
	print "Welcome to Orc Slayer 1986!"
	print "<br><br>"
	print "What is your name?"
	print "<br><br>"
	getName('Submit')
startbattle = 1	

while loop == True:
	if yourHealth >= 500:
		if roundNumber <= 1:
			startbattle = form.getfirst('start', 'None')
			startbattle = cgi.escape(startbattle)
			if startbattle == '1':
				print "Hello", name,"!! <img src=\"img/sword.jpg\">"
				print "<br>"
				print "You come across an Orc. <img src=\"img/orc.jpg\"> He does not like you.<br>"
				print "--------------------<br>"
				print "| Your health is", yourHealth, "<br>"
				print "| Orc's health is", orcHealth, "<br>"
				print "--------------------<br>"
				print "<br>"
				print "Round", roundNumber, "<br>"
				printForm('Attack')
		else:
			print "You're a brave one %s. You dust yourself off and head back into battle!<br>" % name
			print "Round", roundNumber, "<br>"
	

	loop = False
	fight = form.getfirst('fight', 'None')
	fight = cgi.escape(fight)
	if fight == "1":
		battle = True
	else:
		battle = False
	while battle == True:
		startbattle = 2
		print "<br>"
		damage = random.randint(12,50)
		damageYou = random.randint(25,55)
		newHealth = orcHealth - damage
		orcHealth = newHealth
		newYou = yourHealth - damageYou
		yourHealth = newYou
		healRandom = random.randint(1,11)
		extraRandom = random.randint(1,25)
		print "<img src=\"img/sword.jpg\"> ", name, "strikes orc for", damage

		if extraRandom >= 15:

			extraTotal = random.randint(15,18)
			orcHealth = orcHealth - extraTotal
			print "<br>"	
			print "<img src=\"img/dagger.jpg\"> Sneak attack! You stun The Orc damaging him for", extraTotal, "health!"
		if extraRandom >= 20:

			extraTotal = random.randint(11,12)
			orcHealth = orcHealth - extraTotal
			print "<br>"	
			print "<img src=\"img/fist.jpg\"> Cheap Shot! You swung at the Orc when he wasn't ready, hitting him for", extraTotal, "health!"
		if healRandom == 7:

			healTotal = random.randint(10,60)
			yourHealth = yourHealth + healTotal	
			print "<br>"
			print "<img src=\"img/heal-you.jpg\"> With your Paladin Ninja Magic you heal yourself for", healTotal, "health!"
		print "<br>"
		print "<img src=\"img/orc.jpg\"> Orc mauls", name, "for", damageYou

		if extraRandom == 1:

			extraTotal = random.randint(25,50)
			yourHealth = yourHealth - extraTotal	
			print "<br>"
			print "<img src=\"img/axe.jpg\"> Yikes! The Orc lashes out and hit you for an extra", extraTotal, "health!"		
		if healRandom == 3:

			healTotal = random.randint(20,50)
			orcHealth = orcHealth + healTotal
			print "<br>"	
			print "<img src=\"img/blood.jpg\"> The Orc rubs dirt, spit and blood into his wounds healing him for", healTotal, "health!"

	
		if orcHealth <= 0:
			makeTotals(1, 0)
			battle = False
			print "<br><br>"
			print "<img src=\"img/trophy.jpg\"> You've Killed the Orc!"
			print "<br>"
			print "Congrats %s, you killed that smelly Orc!" % name
			print "<br>"
			print name,"'s record"
			print "<br>"
			print "Wins %i - Loses %i" % (int(winRecord),int(loseRecord))
			print "<br>"
			print "Anyone can get lucky once... but do you dare to..."
			printForm('Fight Again?')
			print "<br>"
		
		elif newYou <= 0:
			makeTotals(0, 1)
			battle = False
			print "<br><br>"
			print "<img src=\"img/skull.jpg\"> You've been killed by the Orc!"
			print "<br>"
			print "Sorry %s, Game Over!" % name
			print "<br>"
			print name,"'s record"
			print "<br>"
			print "Wins %i - Loses %i" % (int(winRecord),int(loseRecord))
			print "<br>"
			print "So you died. Run some cold tap water over your mortal wounds and..."
			printForm('Fight Again?')
			print "<br>"

		else:
			print "<br>"
			print "------------------------------------"
			print "<br>"
			print "Your health is now", yourHealth	
			print "<br>"
			print "Orc's health is now", orcHealth
			print "<br><br>"
			fight = "0"
			battle = False

			while fight == "0":
				print "<br>"
				printForm('Attack Again!')
				print "</form>"


				fight = form.getfirst('fight', 'None')
				fight = cgi.escape(fight)

print "</body>"
