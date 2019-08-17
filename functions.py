#Code by IgneousCompas
from time import sleep
from math import tan,pi,radians

menuError = "•Thats not an option. To choose an option, enter the number corresponding to the option that you want to access"

def readOptionsArea():
	openConfigFile = open("config.txt","r")
	textInConfigFile = openConfigFile.read()
	if "togglePaintTrue" in textInConfigFile:
		togglePaint = True
	else:
		togglePaint = False
	return togglePaint
	
def readOptionsVolume():
	openConfigFile = open("config.txt","r")
	textInConfigFile = openConfigFile.read()
	if "toggleWeightTrue" in textInConfigFile:
		toggleWeight = True
	else:
		toggleWeight = False
	return toggleWeight

def convertUnitCubedIntoMetersCubed(volume):			
	while True:	
		print("""What is the unit (mm3, cm3, m3, km3, ft3, yd3, in3, mi3) that the volume uses? Input the number corresponding to the unit used to represent the volume.
			
1. Millimeters cubed (mm3)

2. Centimeters cubed (cm3)

3. Meters cubed (m3)

4. Kilometers cubed (km3)

5. Feet cubed (ft3)

6. Yards cubed (yd3)

7. Inches cubed (in3)

8. Mile cubed (mi3)\n""")

		unit = input("")
			
					#Converting a certain unit squared to m3
		if unit == "1":				# mm3 to m3 (because there is 1 m3 / 1 000 000 000 mm3)
			volume = float(volume) / 1000000000
			break
		elif unit == "2":			# cm3 to m3 (because there is 1 m3 / 1 000 000 cm3)
			volume = float(volume) / 1000000
			break
		elif unit == "3":			# m3 to m3 (because 1 m3 = 1 m3)
			break
		elif unit == "4":			# km3 to m3 (because there is 1 000 000 000 m3 / 1 km3)
			volume = float(volume) * 1000000000
			break
		elif unit == "5":			# ft3 to m3 (because there is 1 m3 / 35.3147248277 ft3)
			volume = float(volume) / 35.3147248277
			break
		elif unit == "6":			# yd3 to m3 (because there is 1 m3 / 1.3079506193 yd3)
			volume = float(volume) / 1.3079506193
			break
		elif unit == "7":			#in3 to m3 (because there is 1 m3 / 61 023.744094732 in3)
			volume = float(volume) / 61023.744094732
			break
		elif unit == "8":			#mi3 to m3 (because there is 4 168 181 825.44057941 m3 / 1 mi3)
			volume = float(volume) * 4168181825.44057941
			break
		else:
			print ("Invalid input. Please input the number corresponding to the unit used to represent the volume.")
	return volume
	
def editDensities():
	# ! = 1 (First custom density)
	# @ = 2 (Second custom density)
	# $ = 3 (Third custom density)
	# When this symbol appears two times in the begging of the line (in config file(config.txt)), than signifies that this line corresponds to the name of the density. Otherwise, if it appears one time (with dollar sign ($)), this represents the value of the density of the custom densities.

	while True:
		openConfigFile = open("config.txt","r")
		textInConfigFile = openConfigFile.readlines()
		for everyLine in textInConfigFile:
			if "!!" in everyLine:
				customEntry1 = everyLine.replace("!!","")			
			elif "!%" in everyLine:
				customEntry1Density = everyLine.replace("!%","")
				customEntry1Density = customEntry1Density.replace("\n","")
			elif "@@" in everyLine:
				customEntry2 = everyLine.replace("@@","")			
			elif "@%" in everyLine:
				customEntry2Density = everyLine.replace("@%","")
				customEntry2Density = customEntry2Density.replace("\n","")			
			elif "$$" in everyLine:
				customEntry3 = everyLine.replace("$$","")			
			elif "$%" in everyLine:
				customEntry3Density = everyLine.replace("$%","")
				customEntry3Density = customEntry3Density.replace("\n","")
			
		print("\nWhat entry do you want to edit?\n")
		print("1.",customEntry1.replace("\n",""),"(" + answer(float(customEntry1Density),None,None) + " Kg / m3)\n")
		print("2.",customEntry2.replace("\n",""),"(" + answer(float(customEntry2Density),None,None) + " Kg / m3)\n")
		print("3.",customEntry3.replace("\n",""),"(" + answer(float(customEntry3Density),None,None) + " Kg / m3)\n")
		print("4. ← Go back")
		editEntry = input("\n")
		openConfigFile = open("config.txt","r")
		textInConfigFile = openConfigFile.read()
		
		if editEntry == "4":
			break
			
		newName = input("\nWhat will be the new name of this material?\n")

		while True:
			newDensity = input("\nWhat will be the density of this material?\n")
			newDensity = verification(newDensity)
			if newDensity == False:
				pass
			else:
				break
				
		while True:
			unitDensity = input("""\nWhat are the units used for the previously saved density?
			
1.  Kg / m3 (Kilograms per cubic meter)

2.  g / cm3 (Grams per cubic centimeter)

3.  lb / in3 (Pounds per cubic inch)

4.  lb / ft3 (Pounds per feet)\n""")
		
			if unitDensity == "1":
				break
			elif unitDensity == "2":
				newDensity = float(newDensity) * 1000
				break
			elif unitDensity == "3":		# 1 lb = 0.4535923kg and 1 cubic inch = 0.000 016 387 064 m3
				newDensity = float(newDensity) * 27679.90470291
				break
			elif unitDensity == "4":
				newDensity = float(newDensity) * 16.01846337
				break	
			else:
				print("Invalid input. Please type the number corresponding to the option that you wish to choose.")
		
		if editEntry == "1":
			customEntry1 = "!!" + customEntry1
			customEntry1Density = "!%" + str(customEntry1Density)
			newName = "!!" + newName
			newDensity = "\n" + "!%" + str(newDensity)
			textInConfigFile = textInConfigFile.replace(customEntry1,newName)
			textInConfigFile = textInConfigFile.replace(customEntry1Density,newDensity)
					
		elif editEntry == "2":
			customEntry2 = "@@" + customEntry2
			customEntry2Density = "@%" + str(customEntry2Density)
			newName = "@@" + newName
			newDensity = "\n" + "@%" + str(newDensity)
			textInConfigFile = textInConfigFile.replace(customEntry2,newName)
			textInConfigFile = textInConfigFile.replace(customEntry2Density,newDensity)
			
		elif editEntry == "3":
			customEntry3 = "$$" + customEntry3
			customEntry3Density = "$%" + str(customEntry3Density)
			newName = "$$" + newName
			newDensity = "\n" + "$%" + str(newDensity)
			textInConfigFile = textInConfigFile.replace(customEntry3,newName)
			textInConfigFile = textInConfigFile.replace(customEntry3Density,newDensity)
			
		else:
			print("That isn't an option. Please enter in a number corresponding to the option that you want to choose.")
			
		openConfigFile = open("config.txt","w")
		openConfigFile.write(textInConfigFile)
		openConfigFile.close()			

#whats
answerArea = "    ► The area of this"
answerVolume = "    ► The volume of this"

def answer(data,shape,what):

	data = round(data,10)
	#Removes the useless ".0" in floats to make it nicer to see
	if data - int(data) == 0: #finds if number is a integer
		data = int(data)
	#Separates each 3 characters with a space to look nicer
	data = str(data)
	counter = 0
	prettyData = ""
	
		#Reversing the part of the number that isn't a decimal number
	normalPart = "" 	#normal part-->[1234].01234
	decimalPart = ""	#1234[.01234]<-- decimal part
	replacement = ""
	for eachCharacter in data:
		if eachCharacter == ".":
			normalPart = eachCharacter + normalPart
			replacement = replacement + eachCharacter
			break
		else:
			normalPart = eachCharacter + normalPart
			replacement = replacement + eachCharacter

	decimalPart = data.replace(replacement,"")
	#Reverses back the normal part and stores it in "prettyData"
	for eachNumber in normalPart: 
		if eachNumber == ".":
			prettyData = eachNumber + prettyData
			pass
		elif counter == 3:
			prettyData = eachNumber + " " + prettyData
			counter = 1
		else:
			prettyData = eachNumber + prettyData
			counter += 1
		
	#Adds the decimal part to "prettyData"		
			
	prettyData = prettyData + decimalPart
	
	if what != None:

		if "area" in what:
			unitType = "squared (u2)\n\n"
		elif "volume" in what:
			unitType = "cubed (u3)\n\n"
			
		if prettyData == "1":
			print("\n\n"+what,shape,"is",prettyData,"unit",unitType)
		else:
			print("\n\n"+what,shape,"is",prettyData,"units",unitType)

		sleep(2.5)
		
	else:
		return prettyData #for answering how many of a thing in a thing(paint buckets, etc.)
	
def verification(measure):	#Verifying if the measure is actually a number
	acceptedCharacters = ["0","1","2","3","4","5","6","7","8","9"]
	verified = False
	alreadyADot = False
	totalAmountOfAcceptedCharacters = 0
	if measure == "":
		print("Please type in a number. Enter in a positive value that corresponds to a measure.")
		return False

	for everyCharacter in measure:
		for everyAcceptedCharacter in acceptedCharacters:
			if everyAcceptedCharacter in everyCharacter:
				totalAmountOfAcceptedCharacters += 1
	if "." in measure:
		totalAmountOfAcceptedCharacters += 1
		lengthWithNoDot = measure.replace(".","",1)
		if "." in lengthWithNoDot:
			print("Please type in a number, not a bunch of dots and letters. Enter in a positive value that corresponds to a measure.")
			return False
		if lengthWithNoDot == "":
			print("Please type in a number, not a single dot. Enter in a positive value that corresponds to a measure.")
			return False
	if "-" in measure:
		print("A measure cannot be negative. Please enter in a positive value that corresponds to a measure.")
		return False
	if len(measure) != totalAmountOfAcceptedCharacters:
		print("Please type in a number, not letters. Enter in a positive value that corresponds to a measure.")
		return False		
		
	return measure

###############################
##  Area of Shapes/Perimeter ##
###############################

def returnAreaSquare(noExtraInfo,isPerimeter):
	while True:
		length = input("\n•How long is the length of one side of this square?\n")
		length = verification(length)
		if length == False:
			pass
		else:
			break
	if isPerimeter == True:
		perimeter = float(length) * 4
		
	area = float(length) ** 2
	
	if noExtraInfo == False:
		answer(area,"square",answerArea)
	
		homManyPaintCans(area)
	
	if isPerimeter == True:
		return area,perimeter
	
	return area

def returnAreaCircle(noExtraInfo,isPerimeter):
	while True:
		radius = input("\n•How long is the radius of this circle? If you do not have this answer and have the diameter of this circle, press enter without writing anything.\n")
		if radius == "":
			diameter = input("\n•How long is the diameter of this circle?\n")
			diameter = verification(diameter)
			if diameter == False:
				pass
			else:
				radius = str(float(diameter) / 2)	
				if isPerimeter == True:
					perimeter = float(diameter) * pi				
				break
		else:
			radius = verification(radius)
			if radius == False:
				pass
			else:
				if isPerimeter == True:
					perimeter = float(radius) * pi * 2
				break
		
	area = pi * (float(radius) ** 2)
	
	if noExtraInfo == False:
		answer(area,"circle",answerArea)
	
		homManyPaintCans(area)
		
	if isPerimeter == True:
		return area,perimeter
	
	return area
	
def returnAreaTriangle(noExtraInfo,isPerimeter):
	while True:
		base = input("\n•How long is the base of this triangle?\n")
		base = verification(base)
		if base == False:
			pass
		else:
			break
			
	while True:	
		height = input("\n•How long is the height of this triangle?\n")
		height = verification(height)
		if height == False:
			pass
		else:
			break
			
	if isPerimeter == True:
		while True:
			a = input("\nHow long is one of the sides of this triangle, except the base? If you do not have this answer and you have the length of one of the projections of the triangle onto its base, enter in nothing (don't type anything)\n")
			if a == "":		
				while True:
					print("""
+-------------------------------------------------+
|            XX                                   |
|           X| XXX                                |
|          X |   XXX                              |
|         X  |     XXX                            |
|        XX  |       XXXX                         |
|       XX   |          XXXX                      |
|      XX    |             XXX                    |
|      X     |               XXXX                 |
|     XX     |                  XXXX              |
|    XX      |                     XXXX           |
|    X       |                        XXXX        |
|   X        |                           XXX      |
|  XX        |                             XXXX   |
| XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX |
| <---------> <---------------------------------> |
|     ???    OR               ???                 |
+-------------------------------------------------+""")
					projA = input("\n•How long is one of the projections of any side of that triangle (in other words, what is the shortest length in between one of the vertices of the base of the triangle and the vertex drawn by the height of the triangle, perpendicular to the base) ? \n")
					projA = verification(projA)  # projA = Projection A and projB = projection B
					if projA == False:
						pass
					else:
						projB = float(base) - float(projA)
						a = ((float(projA)) ** 2 + (float(height)) ** 2) ** 0.5
						b = ((float(projB)) ** 2 + (float(height)) ** 2) ** 0.5
						break
				break	
			else:	
				a = verification(a)  # projA = Projection A and projB = projection B
				if a == False:
					pass
				else:
					while True:
						b = input("\nHow long is the other of the sides of this triangle, except the base and the other side previously given?\n")
						b = verification(b)  # projA = Projection A and projB = projection B
						if b == False:
							pass
						else:
							break
					break
			

		perimeter = float(a) + float(b) + float(base) # base = c
			
	area = (float(base)) * float((height)) / 2
	
	if isPerimeter == True:
		return area,perimeter
			
	if noExtraInfo == False:	
		answer(area,"triangle",answerArea)
	
		homManyPaintCans(area)

	return area
	
def returnAreaRectangleParallelogram(is_rectangle,noExtraInfo,isPerimeter,isOnlyPerimeter = False):
	
	if is_rectangle == True:
		figure = "rectangle"
	else:
		figure = "parallelogram"
	
	questionBase = "\n•How long is the base of this " + figure + "?\n"
	
	questionHeight = "\n•How long is the height of this " + figure + "?\n"
	
	while True:
		base = input(questionBase)
		base = verification(base)
		if base == False:
			pass
		else:
			break
	while True:
		if isOnlyPerimeter == True:
			if is_rectangle != True:
				break
			else:
				pass
		height = input(questionHeight)
		height = verification(height)
		if height == False:
			pass
		else:
			break
			
	if isOnlyPerimeter == False:
		area = (float(base)) * float((height))
	if isPerimeter == True:
		if is_rectangle == True:
			if isOnlyPerimeter == False:
				perimeter = 2 * (float(base) + float(height))
			
		else:
			while True:
				diagonal = input("\n•How long is one of the diagonals of this parallelogram?\n")
				diagonal = verification(diagonal)
				if diagonal == False:
					pass
				else:
					break
			
			perimeter = 2 * (float(base) + float(diagonal))
			if isOnlyPerimeter == True:
				return perimeter
		return area,perimeter
			
	if noExtraInfo == False:
		answer(area,figure,answerArea)
	
		homManyPaintCans(area)
	
	return area
	
def returnAreaPolygon(noExtraInfo,isPerimeter):
	while True:
		nbSides = input("\n•How many sides are there on this polygon?\n")

		nbSides = verification(nbSides)
		if nbSides == False:
			pass
		elif float(int(float(nbSides))) - float(nbSides) != 0:				
			print("\nWhat..? That can't exist!\n")	
		elif float(nbSides) < 3:
			print("\nHold on... That cannot be possible! That wouldn't be even a shape!\n")
		else:
			break
				
	if nbSides != "":
		while True:		
			measureSide = input("\n•How long is one single side on this polygon?\n")
			measureSide = verification(measureSide)
			if measureSide == False:
				pass
			else:
				break

	apothem = (float(measureSide)) / (2 * tan(radians(180 / float(nbSides))))

	area = (float(measureSide) * float(nbSides) * float(apothem)) / 2
	
	if isPerimeter == True:
		perimeter = float(measureSide) * float(nbSides)
		return area,perimeter
		
	
	if noExtraInfo == False:
		answer(area,"polygon",answerArea)
	
		homManyPaintCans(area)
	
	return area	
	
def returnAreaTrapezoid(noExtraInfo,isPerimeter,isOnlyPerimeter = False):
	while True:
		smallBase = input("\n•How long is the first base of this trapezoid?\n")
		smallBase = verification(smallBase)
		if smallBase == False:
			pass
		else:
			break
	while True:
		largeBase = input("\n•How long is the second base of this trapezoid?\n")
		largeBase = verification(largeBase)
		if largeBase == False:
			pass
		else:
			break
	while True:
		if isOnlyPerimeter == False:
			height = input("\n•How long is the height of this trapezoid?\n")
			height = verification(height)
			if height == False:
				pass
			else:
				break
		else:
			break
	
	if isOnlyPerimeter == False:
		area = ((float(smallBase) + float(largeBase)) * float(height)) / 2
	
	if isPerimeter == True:
		while True:
			diagonal1 = input("\n•How long is the first diagonal of this trapezoid (one of the sides of the trapazoid that isn't parallel to its opposite side)?\n")
			diagonal1 = verification(diagonal1)
			if diagonal1 == False:
				pass
			else:
				break
				
		while True:
			diagonal2 = input("\n•How long is the second diagonal of this trapezoid (an other one of the sides of the trapazoid that isn't parallel to its opposite side, exepct the one mentionned previously)?\n")
			diagonal2 = verification(diagonal2)
			if diagonal2 == False:
				pass
			else:
				break
			
		perimeter = float(smallBase) + float(largeBase) + float(diagonal1) + float(diagonal2)
		if isOnlyPerimeter == True:
			return perimeter
		return area,perimeter
		
	if noExtraInfo == False:
		answer(area,"trapezoid",answerArea)
	
		homManyPaintCans(area)
	
	return area	

def returnAreaDiamond(noExtraInfo,isPerimeter):
	while True:
		firstDiagonal = input("\n•How long is the first diagonal of this diamond?\n")
		firstDiagonal = verification(firstDiagonal)
		if firstDiagonal == False:
			pass
		else:
			break
	while True:
		secondDiagonal = input("\n•How long is the second diagonal of this diamond?\n")
		secondDiagonal = verification(secondDiagonal)
		if secondDiagonal == False:
			pass
		else:
			break
			
	area = (float(firstDiagonal)) * float((secondDiagonal)) / 2 
	
	if isPerimeter == True:
		halfFirstDiagonal = float(firstDiagonal) / 2
		halfSecondDiagonal = float(secondDiagonal) / 2
		perimeter = (((float(halfFirstDiagonal) ** 2) + (float(halfSecondDiagonal) ** 2)) ** 0.5) * 4
		return area,perimeter
		
	if noExtraInfo == False:
		answer(area,"diamond",answerArea)
	
		homManyPaintCans(area)
	
	return area

##############################
##	Volume/Area of Solids	##
##############################

def returnVolumeCube(isArea):
	while True:
		length = input("\n•How long is one side of this cube?\n")
		length = verification(length)
		if length == False:
			pass
		else:
			break
	if isArea == True:
		area = (float(length) ** 2) * 6
		answer(area,"cube",answerArea)
		homManyPaintCans(area)
		return area
		
	volume = float(length) ** 3
	answer(volume,"cube",answerVolume)		
	weight(volume)
	return volume
	
def returnVolumePrismOrCylinder(isCylinder,isArea):
	
	if isCylinder == True:
		print("\n•A cylinder is a prism with a circle for its base.\n")
		if isArea == True:
			baseArea,basePerimeter = returnAreaCircle(True,isPerimeter = True)
		else:
			baseArea = returnAreaCircle(True,isPerimeter = False)
		nameOfSolid = 'cylinder'
	else:
		prismDetail = "-based prism"
		
		baseArea = input("""\n•What shape is the base of this prism?\n
1. Square

2. Triangle

3. Rectangle

4. Parallelogram

5. Regular polygon

6. Trapezoid

7. Diamond\n\n""")
		while True:
				
			if baseArea == '1':
				if isArea == True:
					baseArea,basePerimeter = returnAreaSquare(True,isPerimeter = True)
				else:
					baseArea = returnAreaSquare(True,isPerimeter = False)
				nameOfSolid = "square" + prismDetail
				break
			elif baseArea == '2':
				if isArea == True:
					baseArea,basePerimeter = returnAreaTriangle(True,isPerimeter = True)
				else:
					baseArea = returnAreaTriangle(True,isPerimeter = False)
				nameOfSolid = "triangle" + prismDetail
				break
			elif baseArea == '3':
				if isArea == True:
					baseArea,basePerimeter = returnAreaRectangleParallelogram(True,True,isPerimeter = True)
				else:
					baseArea = returnAreaRectangleParallelogram(True,True,isPerimeter = False)
				nameOfSolid = "rectangle" + prismDetail
				break
			elif baseArea == '4':
				if isArea == True:
					baseArea,basePerimeter = returnAreaRectangleParallelogram(False,True,isPerimeter = True)
				else:
					baseArea = returnAreaRectangleParallelogram(False,True,isPerimeter = False)
				nameOfSolid = "parallelogram" + prismDetail
				break
			elif baseArea == '5':
				if isArea == True:
					baseArea,basePerimeter = returnAreaPolygon(True,isPerimeter = True)
				else:
					baseArea = returnAreaPolygon(True,isPerimeter = False)
				nameOfSolid = "polygon" + prismDetail
				break
			elif baseArea == '6':
				if isArea == True:
					baseArea,basePerimeter = returnAreaTrapezoid(True,isPerimeter = True)
				else:
					baseArea = returnAreaTrapezoid(True,isPerimeter = False)
				nameOfSolid = "trapezoid" + prismDetail
				break
			elif baseArea == '7':
				if isArea == True:
					baseArea,basePerimeter = returnAreaDiamond(True,isPerimeter = True)
				else:
					baseArea = returnAreaDiamond(True,isPerimeter = False)
				nameOfSolid = "diamond" + prismDetail
				break
			else:
				print("•Thats not an option. To choose an option, enter the number corresponding to the option that you want to choose.")
				break
	questionForHeight = "\n•What is the measure of the height of the " + nameOfSolid + "?\n"
	while True:
		height = input(questionForHeight)
		height = verification(height)
		if height == False:
			pass
		else:
			break
	
	if isArea == True:
		area = (float(baseArea) * 2) + (float(basePerimeter) * float(height))
		answer(area,nameOfSolid,answerArea)
		homManyPaintCans(area)	
		return area
	
	volume = float(height) * float(baseArea)
	answer(volume,nameOfSolid,answerVolume)
	weight(volume)
	return volume

def returnVolumeSphere(isArea):
	while True:
		radius = input("\n•How long is the radius of the sphere? If you do not know this answer and you have the diameter of the sphere, press enter without writing anything\n")
		if radius == "":
			diameter = input("\n•How long is the diameter of the sphere?\n")
			diameter = verification(diameter)
			if diameter == False:
				pass
			else:
				radius = float(diameter) / 2
				break
		radius = verification(radius)
		if radius == False:
			pass
		else:
			break
	if isArea == True:
		area = 4 * pi * (float(radius) ** 2)
		answer(area,"sphere",answerArea)		
		homManyPaintCans(area)		
		return area
		
	volume = (4 / 3) * pi * (float(radius) ** 3)
	answer(volume,"sphere",answerVolume)
	weight(volume)
	return volume
	
def returnVolumeTorus(isArea):
	diameter = ""
	majorRadius = ""
	circumference = ""
	while True:
		print("\n•What shape is the figure that is spun around the y axis to make the torus?\n")
		print("""
1. Circle (normal torus)

2. Square

3. Triangle

4. Rectangle

5. Parallelogram

6. Regular polygon

7. Trapezoid

8. Diamond\n\n""")


		base = input("")
		if base == '1':
			if isArea == True:
				base,basePerimeter = returnAreaCircle(True,isPerimeter = True)
			else:
				base = returnAreaCircle(True,isPerimeter = False)
			break
		elif base == '2':
			if isArea == True:
				base,basePerimeter = returnAreaSquare(True,isPerimeter = True)
			else:
				base = returnAreaSquare(True,isPerimeter = False)
			break
		elif base == '3':
			if isArea == True:
				base,basePerimeter = returnAreaTriangle(True,isPerimeter = True)
			else:
				base = returnAreaTriangle(True,isPerimeter = False)
			break
		elif base == '4':
			if isArea == True:
					base,basePerimeter = returnAreaRectangleParallelogram(True,True,isPerimeter = True)
			else:
				base = returnAreaRectangleParallelogram(True,True,isPerimeter = False)
			break
		elif base == '5':
			if isArea == True:
				basePerimeter = returnAreaRectangleParallelogram(False,True,isPerimeter = True,isOnlyPerimeter = True)
			else:
				base = returnAreaRectangleParallelogram(False,True,isPerimeter = False)
			break
		elif base == '6':
			if isArea == True:
				base,basePerimeter = returnAreaPolygon(True,isPerimeter = True)
			else:
				base = returnAreaPolygon(True,isPerimeter = False)
			break
		elif base == '7':
			if isArea == True:
				basePerimeter = returnAreaTrapezoid(True,isPerimeter = True,isOnlyPerimeter = True)
			else:
				base = returnAreaTrapezoid(True,isPerimeter = False)
			break
		elif base == '8':
			if isArea == True:
				base,basePerimeter = returnAreaDiamond(True,isPerimeter = True)
			else:
				base = returnAreaDiamond(True,isPerimeter = False)
			break
		else:
			print("•Thats not an option. To choose an option, enter the number corresponding to the option that you want to choose.")
			break
	
	while True:
		majorRadius = input("\n•What is the length of the major radius of the torus (radius of the torus itself)?  If you do not have this answer and have the diameter of the whole torus, press enter without typing anything.\n")
		if majorRadius == "":
			diameter = input("\n•What is the length of the diameter of the whole torus? If you do not have this answer and have the circumference of the torus, press enter without typing anything.\n")
			if diameter == "":	
				circumference = input("\n•What is the length of the circumference of the torus?\n")
				circumference = verification(circumference)
				if circumference == False:
					pass
				else:
					break
			else:
				diameter = verification(diameter)
				if diameter == False:
					pass
				else:
					break
					
		else:
			majorRadius = verification(majorRadius)
			if majorRadius == False:
				pass
			else:
				break
	
	if isArea == True:
		if diameter != "":
			area = float(basePerimeter) * pi * float(diameter)
		elif majorRadius != "":
			area = float(basePerimeter) * pi * 2 * float(majorRadius)
		elif circumference != "":
			area = float(basePerimeter) * float(circumference)
			
		answer(area,"torus",answerArea)
		homManyPaintCans(area)
		return area
		
	else:
		if diameter != "":
			volume = float(base) * pi * float(diameter)
		elif majorRadius != "":
			volume = float(base) * pi * 2 * float(majorRadius)
		elif circumference != "":
			volume = float(base) * float(circumference)
		
		answer(volume,"torus",answerVolume)
		weight(volume)
		return volume

def returnVolumeOrAreaPyramidOrCone(isCone,isArea):
	if isCone == True:	
		print("\n•A cone is a pyramid with a circle for its base.\n")
		baseArea,basePerimeter = returnAreaCircle(True,isPerimeter = True)
		radius = float(basePerimeter) / (2 * pi)
		while True:
			height = input("\n•What is the length of the height of the cone? If you do not have this answer and have the length of the slant of the cone, press enter without typing anything.\n")
			if height == "":
				slant = input("\n•What is the length of the slant of the cone?\n")
				slant = verification(slant)
				if slant == False:
					pass
				else:
					break
			else:
				height = verification(height)
				if height == False:
					pass
				else:
					break
		
		if height != "":
			slant = (float(radius) ** 2 + float(height) ** 2) ** 0.5
		
		if isArea == True:
			area = float(baseArea) + (pi * float(slant) * float(radius))
			answer(area,'cone',answerArea)
			homManyPaintCans(area)
			return area		
		else:
			volume = float(height) * float(baseArea) / 3
			answer(volume,'cone',answerVolume)
			weight(volume)
			return volume
		
	else:
		pyramidDetail = "-based pyramid"
		
		baseArea = input("""•What shape is the base of this pyramid?\n
1. Square

2. Equilateral Triangle

3. Triangle

4. Rectangle

5. Parallelogram

6. Regular polygon

7. Diamond

8. Trapezoid\n\n""")
		while True:
			figure = "rectangle"
			if baseArea == '5':
				baseArea = '4'
				figure = "parallelogram"
				
			if baseArea == '1':
				baseArea,basePerimeter = returnAreaSquare(True,isPerimeter = True)
				side = float(basePerimeter) / 4
				nameOfSolid = "square" + pyramidDetail
				while True:
					slant = input("\n•What is the length of the slant of the square based pyramid? If you do not have this answer and have the measure of the height of the square based pyramid, press enter without writing anything.\n")
					
					if slant == "":
						height = input("\n•What is the length of the height of the square based pyramid?\n")
						height = verification(height)
						if height == False:
							pass
						else:
							slant = (( ( (float(side) / 2) ** 2) + (float(height) ** 2) ) ** 0.5)
							break

					else:
						slant = verification(slant)
						if slant == False:
							pass
						else:
							break
				
				if isArea == True:
					area = (float(side) ** 2) + ((float(slant) * float(side) * 0.5) * 4)
					answer(area,nameOfSolid,answerArea)
					homManyPaintCans(area)
					return area	
				else:
					if slant != "":
						height = (((float(slant)) ** 2) - ((float(side) / 2) ** 2)) ** 0.5
					
					volume = float(height) * float(baseArea) / 3
					answer(volume,nameOfSolid,answerVolume)
					weight(volume)
					return volume	
							
			elif baseArea == '2':
				while True:
					side = input("\n•How long is one of the sides of this triangle? If you do not have this information and have the height of this triangle, press enter without writting anything.\n")
					if side == "":
						height = input("\n•What is the length of the height of this triangle?\n")
						height = verification(height)
						if height == False:
							pass
						else:
							side = (2 * float(height)) / (tan(radians(60)))
							break
							
					
					if side != "":
						side = verification(side)
						if side == False:
							pass
						else:
							height = (float(side) / 2) * (tan(radians(60)))
							break
				
				areaBase = (float(side) * float(height)) / 2
				nameOfSolid = "triangle" + pyramidDetail
				while True:
					slant = input("\n•What is the length of the slant of the triangular based pyramid? If you do not have this answer and have the measure of the height of the square based pyramid, press enter without writing anything.\n")
					
					if slant == "":
						heightPyramid = input("\n•What is the length of the height of the triangular based pyramid?\n")
						heightPyramid = verification(heightPyramid)
						if heightPyramid == False:
							pass
						else:
							yPointMiddleSide = float(height) / 2
							xPointMiddleSide = float(side) / 4
							xPointTipOfHeight = -1 * (float(side)/ 2)
							a = (float(yPointMiddleSide)) / (float(xPointMiddleSide) - float(xPointTipOfHeight))
							b = -1 * (float(a) * float(xPointTipOfHeight))
							slant = ((float(b) ** 2) + (float(heightPyramid) ** 2)) ** 0.5			
							break
					else:
						slant = verification(slant)
						if slant == False:
							pass
						else:
							break
				
				if isArea == True:
					area = ((float(side) * float(height)) / 2) + (((float(side) * float(slant)) / 2) * 3)
					answer(area,nameOfSolid,answerArea)
					homManyPaintCans(area)
					return area
				else:
					if slant != "":
						yPointMiddleSide = float(height) / 2
						xPointMiddleSide = float(side) / 4
						xPointTipOfHeight = -1 * (float(side)/ 2)
						a = (float(yPointMiddleSide)) / (float(xPointMiddleSide) - float(xPointTipOfHeight))
						b = -1 * (float(a) * float(xPointTipOfHeight))
						heightPyramid = ((float(slant) ** 2) - (float(b) ** 2)) ** 0.5
						
					volume = (float(heightPyramid) * float(areaBase)) / 3
					answer(volume,nameOfSolid,answerVolume)
					weight(volume)
					return volume					
						
			elif baseArea == '3':
				nameOfSolid = "triangle" + pyramidDetail
				if isArea != True:
					baseArea = returnAreaTriangle(True,False)
					while True:
						heightPyramid = input("\n•What is the measure of the height of the triangle-based pyramid?\n")
						heightPyramid = verification(heightPyramid)
						if heightPyramid == False:
							pass
						else:
							break
				else:
					while True:
						base = input("\n•How long is the base of this triangle?\n")
						base = verification(base)
						if base == False:
							pass
						else:
							break
				
				
					while True:
						a = input("\nHow long is one of the sides of this triangle, except the base? If you do not have this answer and you have the length of the height of the triangle and the length of one of the projections of the triangle onto its base and the height of the triangle, enter in nothing (don't type anything)\n")
						if a == "":		
							height = input("\n•What is the length of the height of this triangle?\n")
							height = verification(height)
							if height == False:
								pass	
							else:
								print("""
+-------------------------------------------------+
|            XX                                   |
|           X| XXX                                |
|          X |   XXX                              |
|         X  |     XXX                            |
|        XX  |       XXXX                         |
|       XX   |          XXXX                      |
|      XX    |             XXX                    |
|      X     |               XXXX                 |
|     XX     |                  XXXX              |
|    XX      |                     XXXX           |
|    X       |                        XXXX        |
|   X        |                           XXX      |
|  XX        |                             XXXX   |
| XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX |
| <---------> <---------------------------------> |
|     ???    OR               ???                 |
+-------------------------------------------------+""")	
								
								projA = input("\n•How long is one of the projections of any side of that triangle (in other words, what is the shortest length in between one of the vertices of the base of the triangle and the vertex drawn by the height of the triangle, perpendicular to the base) ? \n")
								projA = verification(projA)  # projA = Projection A and projB = projection B
								if projA == False:
									pass
								else:
									projB = float(base) - float(projA)
									a = ((float(projA)) ** 2 + (float(height)) ** 2) ** 0.5
									b = ((float(projB)) ** 2 + (float(height)) ** 2) ** 0.5
									break
						else:	
							a = verification(a)  # projA = Projection A and projB = projection B
							if a == False:
								pass
							else:
								while True:
									b = input("\nHow long is the other of the sides of this triangle, except the base and the other side previously given?\n")
									b = verification(b)  # projA = Projection A and projB = projection B
									if b == False:
										pass
									else:
										break
								break
								
					while True:	
						slantBase = input("\n•How long is the slant of the pyramid that is perpendicular to the base of the triangle?\n")
						slantBase = verification(slantBase)
						if slantBase == False:
							pass
						else:
							break
					while True:
						slantA = input("\n•How long is the slant of the pyramid that is perpendicular to the side of the triangle that has a length of " + str(a) + "? (for context, the base of the triangle has a length of " + base + ", one of the sides of this triangle has a length of " + str(a) + ", and the other side has length of " + str(b) + ". )\n")
						slantA = verification(slantA)
						if slantA == False:
							pass
						else:
							break					
					while True:	
						slantB = input("\n•How long is the slant of the pyramid that is perpendicular to the side of the triangle that has a length of " + str(b) + "? (for context, the base of the triangle has a length of " + base + ", one of the sides of this triangle has a length of " + str(a) + ", and the other side has length of " + str(b) + ". )\n")
						slantB = verification(slantB)
						if slantB == False:
							pass
						else:
							break
						
				if isArea == True:
					halfPerimeter = (float(base) + float(a) + float(b)) / 2	
					baseArea = (float(halfPerimeter) * (float(halfPerimeter) - float(base)) * (float(halfPerimeter) - float(a)) * (float(halfPerimeter) - float(b))) ** 0.5
					area = (float(baseArea)) + (float(base) * float(slantBase) / 2) + (float(a) * float(slantA) / 2) + (float(b) * float(slantB) / 2)
					answer(area,nameOfSolid,answerArea)
					homManyPaintCans(area)
					return area
				else:
					volume = (float(heightPyramid) * float(baseArea)) / 3
					answer(volume,nameOfSolid,answerVolume)
					weight(volume)
					return volume

			elif baseArea == '4':
				while True:	
					base = input("\n•What is the length of the base of the " + figure + "?\n")
					base = verification(base)
					if base == False:
						pass
					else:
						break
				while True:	
					height = input("\n•What is length of the height of the " + figure + "?\n")
					height = verification(height)
					if height == False:
						pass
					else:
						break
				
				if isArea == True:
					while True:
						if figure != "parallelogram":
							heightPyramid = input("\n•What is the height of the pyramid? If you do not have this answer and have the two lengths of the two different slants of the pyramid, press enter without typing anything.\n")
							if heightPyramid == "":
								slantBase = input("\n•What is the length of the slant that is perpendicular to one of the bases of the " + figure + "? If you do not have this answer and have the length of the slant that is perpendicular to one of the heights of the " + figure + ", press enter without typing anything.\n")
								if slantBase == "":
									slantHeight = input("\n•What is the length of the slant that is perpendicular to one of the heights of the " + figure + "?\n")
									slantHeight = verification(slantHeight)
									if slantHeight == False:
										pass
									else:
										heightPyramid = ((float(slantHeight) ** 2) - ((float(base) / 2) ** 2)) ** 0.5
										slantBase = ((float(heightPyramid) ** 2) + ((float(height) / 2) ** 2)) ** 0.5
										break
								else:
									slantBase = verification(slantBase)
									if slantBase == False:
										pass
									else:
										heightPyramid = ((float(slantBase) ** 2) - ((float(height) / 2) ** 2)) ** 0.5
										slantHeight = ((float(heightPyramid) ** 2) + ((float(base) / 2) ** 2)) ** 0.5
										break
							else:
								heightPyramid = verification(heightPyramid)
								if heightPyramid == False:
									pass
								else:
									slantBase = ((float(height) / 2) ** 2 + float(heightPyramid) ** 2) ** 0.5
									slantHeight = ((float(base) / 2) ** 2 + float(heightPyramid) ** 2) ** 0.5
									break
								
						else:
							while True:
								slantedSide = input("\n•What is the length of the slanted side of the " + figure + "?\n")
								slantedSide = verification(slantedSide)
								if slantedSide == False:
									pass
								else:
									break
							while True:
								slantBase = input("\n•What is the length of the slant that is perpendicular to one of the bases of the " + figure + "?\n")
								slantBase = verification(slantBase)
								if slantBase == False:
									pass
								else:
									break
							while True:
								slantSlantedSide = input("\n•What is the length of the slant that is perpendicular to one of the slanted sides of the " + figure + "?\n")
								slantSlantedSide = verification(slantSlantedSide)
								if slantSlantedSide == False:
									pass
								else:
									break
							break
				else:
					while True:
						if figure != "parallelogram":
							heightPyramid = input("\n•What is the height of the pyramid? If you do not have this answer and have one of the two lengths of the slant of the pyramid, press enter without typing anything.\n")
							if heightPyramid == "":
								slantBase = input("\n•What is the length of the slant that is perpendicular to one of the bases of the " + figure + "? If you do not have this answer and have the length of the slant that is perpendicular to one of the heights of the " + figure + ", press enter.\n")
								if slantBase == "":
									slantHeight = input("\n•What is the length of the slant that is perpendicular to one of the heights of the " + figure + "?\n")
									slantHeight = verification(slantHeight)
									if slantHeight == False:
										pass
									else:
										heightPyramid = ((float(slantHeight) ** 2) - ((float(base) / 2) ** 2)) ** 0.5
										break
								else:
									slantBase = verification(slantBase)
									if slantBase == False:
										pass
									else:
										heightPyramid = ((float(slantBase) ** 2) - ((float(height) / 2) ** 2)) ** 0.5
										break
							else:
								heightPyramid = verification(heightPyramid)
								if heightPyramid == False:
									pass
								else:
									break
								
						else:
							heightPyramid = input("\n•What is the length of the height of the pyramid?\n")
							heightPyramid = verification(heightPyramid)
							if heightPyramid == False:
								pass
							else:
								break
				
				nameOfSolid = figure + pyramidDetail
				if isArea == True:
					if figure == "rectangle":
						area = float(base) * float(height) + (float(base) * float(slantBase)) + (float(height) * float(slantHeight))
					else:
						area = float(base) * float(height) + (float(base) * float(slantBase)) + (float(slantedSide) * float(slantSlantedSide))
					answer(area,nameOfSolid,answerArea)
					homManyPaintCans(area)
					del figure
					return area
				else:
					volume = ((float(base) * float(height)) * float(heightPyramid)) / 3
					answer(volume,nameOfSolid,answerVolume)
					weight(volume)
					return volume
					
			elif baseArea == '6':
				nameOfSolid = "polygon" + pyramidDetail
				while True:
					nbSides = input("\n•How many sides does the polygon have? (as the base of the pyramid)\n")		
					nbSides = verification(nbSides)
					if nbSides == False:
						pass
					elif float(int(float(nbSides))) - float(nbSides) != 0:				
						print("\nWhat..? That can't exist!\n")
					elif float(nbSides) < 3:
						print("\nHold on... That cannot be possible! That wouldn't be even a shape!\n")
					else:
						break
				
				while True:		
					measureSide = input("\n•How long is one single side on this polygon?\n")
					measureSide = verification(measureSide)
					if measureSide == False:
						pass
					else:
						break
						
				apothem = (float(measureSide)) / (2 * tan(radians(180 / float(nbSides))))

				while True:
					height = input("\n•What is the length of the height of the pyramid? If you do not have this answer and have the length of the slant of the pyramid, press enter.\n")
					if height == "":
						slant = input("\n•How long is the slant of this pyramid?\n")
						slant = verification(slant)
						if slant == False:
							pass
						else:
							break
					else:
						height = verification(height)
						if height == False:
							pass
						else:
							slant = (float(apothem) ** 2 + float(height) ** 2) ** 0.5
							break
						
				if isArea == True:
					area = ((float(measureSide) * float(nbSides) * float(apothem)) / 2) + ((float(measureSide) * float(slant) / 2) * float(nbSides))
					answer(area,nameOfSolid,answerArea)
					homManyPaintCans(area)
					return area
				else:
					if height == "":
						height = ((float(slant) ** 2) - (float(apothem) ** 2)) ** 0.5
					
					volume = (float(measureSide) * float(apothem) * float(nbSides) / 2) * float(height) / 3
					answer(volume,nameOfSolid,answerVolume)
					weight(volume)
					return volume
				
			elif baseArea == '7':
				nameOfSolid = "diamond" + pyramidDetail
				while True:
					diagonal1 = input("\n•What is the length of the first diagonal of the diamond shaped base?\n")
					diagonal1 = verification(diagonal1)
					if diagonal1 == False:
						pass
					else:
						break
						
				while True:
					diagonal2 = input("\n•What is the length of the second diagonal of the diamond shaped base?\n")
					diagonal2 = verification(diagonal2)
					if diagonal2 == False:
						pass
					else:
						break
				
				if isArea == True:
					side = ((float(diagonal1) / 2) ** 2 + (float(diagonal2) / 2) ** 2) ** 0.5
					while True:
						height = input("\n•What is the length of the height of the pyramid? If you do not have this answer and have the length of the slant of the pyramid, press enter.\n")
						if height == "":
							slant = input("\n•How long is the slant of this pyramid?\n")
							slant = verification(slant)
							if slant == False:
								pass
							else:
								area = ((float(diagonal1) * float(diagonal2)) / 2) + ((float(side) * float(slant) / 2) * 4)
								break
						else:
							height = verification(height)
							if height == False:
								pass
							else:
								diagonalSlant1 = ((float(diagonal1) / 2) ** 2 + (float(height)) ** 2) ** 0.5
								diagonalSlant2 = ((float(diagonal2) / 2) ** 2 + (float(height)) ** 2) ** 0.5
								halfPerimeter = (float(diagonalSlant1) + float(diagonalSlant2) + float(side)) / 2
								areaOneSide = (float(halfPerimeter) * (float(halfPerimeter) - float(diagonalSlant1)) * (float(halfPerimeter) - float(diagonalSlant2)) * (float(halfPerimeter) - float(side))) ** 0.5
								area = (float(areaOneSide) * 4) + ((float(diagonal1) * float(diagonal2)) / 2)
								break
					answer(area,nameOfSolid,answerArea)
					homManyPaintCans(area)
					return area	
				
				else:
					while True:
						height = input("\n•What is the length of the height of the pyramid?\n")
						height = verification(height)
						if height == False:
							pass
						else:
							volume = (float(diagonal1) * float(diagonal2) / 2) * float(height) / 3
							answer(volume,nameOfSolid,answerVolume)
							weight(volume)
							return volume								
						
			elif baseArea == '8':
				nameOfSolid = "trapazoid" + pyramidDetail
				while True:
					smallBase = input("\n•How long is the first base of the trapezoid?\n")
					smallBase = verification(smallBase)
					if smallBase == False:
						pass
					else:
						break
				while True:
					largeBase = input("\n•How long is the second base of the trapezoid?\n")
					largeBase = verification(largeBase)
					if largeBase == False:
						pass
					else:
						break
				while True:
					height = input("\n•How long is the height of the trapezoid?\n")
					height = verification(height)
					if height == False:
						pass
					else:
						break
				
				if isArea == True:
					while True:
						diagonal1 = input("\n•How long is the first diagonal of the trapezoid (one of the sides of the trapazoid that isn't parallel to its opposite side)?\n")
						diagonal1 = verification(diagonal1)
						if diagonal1 == False:
							pass
						else:
							break
							
					while True:
						diagonal2 = input("\n•How long is the second diagonal of the trapezoid (an other one of the sides of the trapazoid that isn't parallel to its opposite side, exepct the one mentionned previously)?\n")
						diagonal2 = verification(diagonal2)
						if diagonal2 == False:
							pass
						else:
							break
							
					while True:
						slantSmallBase = input("\n•How long is the slant of the pyramid that is perpendicular to the first base of the trapazoid (which measures " + smallBase +")\n")
						slantSmallBase = verification(slantSmallBase)
						if slantSmallBase == False:
							pass
						else:
							break
					while True:
						slantLargeBase = input("\n•How long is the slant of the pyramid that is perpendicular to the second base of the trapazoid (which measures " + largeBase +")\n")
						slantLargeBase = verification(slantLargeBase)
						if slantLargeBase == False:
							pass
						else:
							break
					while True:
						slantDiagonal1 = input("\n•How long is the slant of the pyramid that is perpendicular to the first diagonal of the trapazoid (which measures " + diagonal1 +")\n")
						slantDiagonal1 = verification(slantDiagonal1)
						if slantDiagonal1 == False:
							pass
						else:
							break
					while True:
						slantDiagonal2 = input("\n•How long is the slant of the pyramid that is perpendicular to the second diagonal of the trapazoid (which measures " + diagonal2 +")\n")
						slantDiagonal2 = verification(slantDiagonal2)
						if slantDiagonal2 == False:
							pass
						else:
							break
				
					area = (((float(smallBase) + float(largeBase)) * float(height)) / 2) + ((float(smallBase) * float(slantSmallBase)) / 2) + ((float(largeBase) * float(slantLargeBase)) / 2) + ((float(diagonal1) * float(slantDiagonal1)) / 2) + ((float(diagonal2) * float(slantDiagonal2)) / 2)
					answer(area,nameOfSolid,answerArea)
					homManyPaintCans(area)
					return area			
				else:
					while True:
						heightPyramid = input("\n•What is the length of the height of the pyramid?\n")
						heightPyramid = verification(heightPyramid)
						if heightPyramid == False:
							pass
						else:
							volume = ((((float(smallBase) + float(largeBase)) * float(height)) / 2) * float(heightPyramid)) / 3
							answer(volume,nameOfSolid,answerVolume)
							weight(volume)
							return volume					
			else:
				print(menuError)
				break
	
#########################################
##			OTHER FEATURES			   ##
#########################################

def homManyPaintCans(area):
	togglePaint = readOptionsArea()
	if togglePaint == True:
		while True:
			unit = input("""What is the unit (mm2, cm2, m2, km2, ft2, yd2, in2, mi2) that the area uses? Input the number corresponding to the unit used to represent the area.
			
1. Millimeters squared (mm2)

2. Centimeters squared (cm2)

3. Meters squared (m2)

4. Kilometers squared (km2)

5. Feet squared (ft2)

6. Yards squared (yd2)

7. Inches squared (in2)

8. Mile squared (mi2)
\n""")									#Converting a certain unit squared to m2
			if unit == "1":				# mm2 to m2 (because there is 1 m2 / 1 000 000 mm2)
				area = area / 1000000
				break
			elif unit == "2":			# cm2 to m2 (because there is 1 m2 / 1 000 cm2)
				area = area / 10000	
				break
			elif unit == "3":			# m2 to m2 (because 1 m2 = 1 m2)
				break
			elif unit == "4":			# km2 to m2 (because there is 1 000 000 m2 / 1 km2)
				area = area * 1000000
				break
			elif unit == "5":			# ft2 to m2 (because there is 1 m2 / 10.7639104 ft2)
				area = area / 10.7639104
				break
			elif unit == "6":			# yd2 to m2 (because there is 1 m2 / 1.19599005 yd2)
				area = area / 1.19599005
				break
			elif unit == "7":			#in2 to m2 (because there is 1 m2 / 1550.003100006 in2)
				area = area / 1550.003100006
				break
			elif unit == "8":			#mi2 to m2 (because there is 2 589 988.110336 m2 / 1 mi2)
				area = area * 2589988.110336
				break
			else:
				print ("Invalid input. Please input the number corresponding to the unit used to represent the area.")


		area = area / 45.36 #Because in every normal sized paint bucket (3.78 liters), there is enough paint to cover approximately 45.36 m2. (The paint used is paint used to paint indoor walls)

		paintAnswer = - int(- area // 1) #rounding it up
		
		paintAnswer = answer(paintAnswer,None,None) #making the answer "pretty" (putting "None" will return the "pretty number")
		
		coatsAnswer = - int((- area * 2)// 1 ) #rounding it up
		
		coatsAnswer = answer(coatsAnswer,None,None) #making the answer "pretty" (putting "None" will return the "pretty number")
		
		if paintAnswer == "1":
			if coatsAnswer == "1":
				print ("\n   ► It would take  1  paint bucket (3.78 liters) to cover this area with ordinary paint (not counting the coats. If so, it would be 1 paint bucket).")
			else:
				print ("\n   ► It would take  1  paint bucket (3.78 liters) to cover this area with ordinary paint (not counting the coats. If so, it would be",coatsAnswer,"paint buckets).")
		else:
			print ("\n   ► It would take ",paintAnswer," paint buckets (3.78 liters) to cover this area with ordinary paint (not counting the coats. If so, it would be",coatsAnswer,"paint buckets).")	
		
		sleep(2.5)

def weight(volume):
	toggleWeight = readOptionsVolume()
	if toggleWeight == True:
		openConfigFile = open("config.txt","r")
		textInConfigFile = openConfigFile.readlines()
		for everyLine in textInConfigFile:
			if "!!" in everyLine:
				customEntry1 = everyLine.replace("!!","")			
			elif "!%" in everyLine:
				customEntry1Density = everyLine.replace("!%","")
				customEntry1Density = customEntry1Density.replace("\n","")
			elif "@@" in everyLine:
				customEntry2 = everyLine.replace("@@","")			
			elif "@%" in everyLine:
				customEntry2Density = everyLine.replace("@%","")
				customEntry2Density = customEntry2Density.replace("\n","")			
			elif "$$" in everyLine:
				customEntry3 = everyLine.replace("$$","")			
			elif "$%" in everyLine:
				customEntry3Density = everyLine.replace("$%","")
				customEntry3Density = customEntry3Density.replace("\n","")
				
		volume = convertUnitCubedIntoMetersCubed(volume)
		
		while True:
			print("""What material is the solid made of (what is the density of the material)?
			
1. Iron (7 874 Kg/m3)

2. Copper (8 944 Kg/m3)

3. Lead (11 343 Kg/m3)

4. Gold (19 320 Kg/m3)

5. American red oak wood (740 Kg/m3)\n""")	
			print("6.",customEntry1.replace("\n",""),"(" + answer(float(customEntry1Density),None,None) + " Kg / m3) (CUSTOM)\n")
			print("7.",customEntry2.replace("\n",""),"(" + answer(float(customEntry2Density),None,None) + " Kg / m3) (CUSTOM)\n")
			print("8.",customEntry3.replace("\n",""),"(" + answer(float(customEntry3Density),None,None) + " Kg / m3) (CUSTOM)\n")
			print("9. Edit a custom entry\n")
			
			unit = input("")
			if unit == "1":				
				weight = 7874 * float(volume)
				break
			elif unit == "2":			
				weight = 8944 * float(volume)
				break
			elif unit == "3":			
				weight = 11343 * float(volume)
				break
			elif unit == "4":			
				weight = 19320 * float(volume)
				break
			elif unit == "5":			
				weight = 740 * float(volume)
				break
			elif unit == "6":			
				weight = float(customEntry1Density.replace("\n","")) * float(volume)
				break
			elif unit == "7":			
				weight = float(customEntry2Density.replace("\n","")) * float(volume)
				break
			elif unit == "8":			
				weight = float(customEntry3Density.replace("\n","")) * float(volume)
				break
			elif unit == "9":
				editDensities()
			else:
				print("Invalid input. Please type the number corresponding to the option that you wish to choose.")
				
		answerCigarette = 1
		answerMan = 1
		
		weightInGrams = weight * 1000
		weightInGrams = answer(weightInGrams,None,None)
		weightInPounds = weight / 0.45359237
		weightInPounds = answer(weightInPounds,None,None)
		weight = answer(weight,None,None) #making the answer "pretty" (putting "None" will return the "pretty number")
		
		print ("\n   ► This solid has a weight of " + weight + " Kg, which is equal to " + weightInGrams + " g, and equal to " + weightInPounds + " lbs.")

		sleep(2.5)