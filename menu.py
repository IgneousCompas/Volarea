#Code by IgneousCompas
from functions import *

def areaMenu():
	while True:
		print("""\n•What figure do you want to calculate the area of?

1. Square

2. Triangle

3. Rectangle

4. Parallelogram

5. Regular polygon

6. Trapezoid

7. Diamond

8. Circle

9. ← Go back""")
		choice = input("\n")
		if choice == '9':
			break
		while True:
			
			if choice == '1':
				returnAreaSquare(False,isPerimeter = False)
				break
			elif choice == '2':
				returnAreaTriangle(False,isPerimeter = False)
				break
			elif choice == '3':
				returnAreaRectangleParallelogram(True,False,isPerimeter = False)
				break
			elif choice == '4':
				returnAreaRectangleParallelogram(False,False,isPerimeter = False)
				break
			elif choice == '5':
				returnAreaPolygon(False,isPerimeter = False)
				break
			elif choice == '6':
				returnAreaTrapezoid(False,isPerimeter = False)
				break
			elif choice == '7':
				returnAreaDiamond(False,isPerimeter = False)
				break
			elif choice == '8':
				returnAreaCircle(False,isPerimeter = False)
				break
			else:
				print(menuError)
				break
				
def volumeMenu():
	while True:
		print("""\n•What solid do you want to calculate the volume of?

1. Cube

2. Right pyramid

3. Right cone

4. Right prism

5. Right cylinder

6. Sphere

7. Torus (Circular torus, square torus, etc.)

8. ← Go back""")
		choice = input("\n")
		if choice == '8':
			break
		while True:
			
			if choice == '1':
				returnVolumeCube(isArea = False)
				break
			elif choice == '2':
				returnVolumeOrAreaPyramidOrCone(False,False)
				break
			elif choice == '3':
				returnVolumeOrAreaPyramidOrCone(True,False)
				break
			elif choice == '4':
				returnVolumePrismOrCylinder(isCylinder = False,isArea = False)
				break
			elif choice == '5':
				returnVolumePrismOrCylinder(isCylinder = True,isArea = False)
				break
			elif choice == '6':
				returnVolumeSphere(isArea = False)
				break
			elif choice == '7':
				returnVolumeTorus(isArea = False)
				break
			else:
				print(menuError)
				break





def areaSolidsMenu():
	while True:
		print("""\n•What solid do you want to calculate the area of?

1. Cube

2. Pyramid

3. Cone

4. Prism

5. Cylinder

6. Sphere

7. Torus (Circular torus, square torus, etc.)

8. ← Go back""")
		choice = input("\n")
		if choice == '8':
			break
		while True:
			
			if choice == '1':
				returnVolumeCube(isArea = True)
				break
			elif choice == '2':
				returnVolumeOrAreaPyramidOrCone(False,True)
				break
			elif choice == '3':
				returnVolumeOrAreaPyramidOrCone(True,True)
				break
			elif choice == '4':
				returnVolumePrismOrCylinder(isCylinder = False,isArea = True)
				break
			elif choice == '5':
				returnVolumePrismOrCylinder(isCylinder = True,isArea = True)
				break
			elif choice == '6':
				returnVolumeSphere(isArea = True)
				break
			elif choice == '7':
				returnVolumeTorus(isArea = True)
				break
			else:
				print(menuError)
				break




def optionsMenu():
	toggleOption = False
	while True:
		togglePaint = readOptionsArea()
		if togglePaint == True:
			togglePaintTEXT = "ON"
		else:
			togglePaintTEXT = "OFF"
			
		toggleWeight = readOptionsVolume()
		if toggleWeight == True:
			toggleWeightTEXT = "ON"
		else:
			toggleWeightTEXT = "OFF"
			
		print('\n•What do you wish to change in the options?')
		print ("\n1. Toggle answer how many paint buckets could be used to cover a certain area ( ",togglePaintTEXT," )")
		print ("\n2. Toggle answer the weight of a solid by knowing the density of the material that it is made of ( ",toggleWeightTEXT," )")
		print ("""\n3. Create or edit a custom density (for volume of objects)
\n4. Reset options
\n5. ← Go back""")
		options_menu_do_what = input("\n")

		if options_menu_do_what == "1":
			toggleFalse = "togglePaintFalse"
			toggleTrue = "togglePaintTrue"
			toggleOption = True
		elif options_menu_do_what == "2":
			toggleFalse = "toggleWeightFalse"
			toggleTrue = "toggleWeightTrue"
			toggleOption = True
			
		if toggleOption == True:
			Close = False
			modifyConfigFile = open("config.txt","r")
			allTextInConfigFile = modifyConfigFile.read()
			modifyConfigFile = open("config.txt","r")
			eachLineInConfigFile = modifyConfigFile.readlines()
			for eachLine in eachLineInConfigFile:
				if toggleFalse.replace("\n","") == eachLine.replace("\n",""):
					allTextInConfigFile = allTextInConfigFile.replace(toggleFalse,toggleTrue,1)
					Close = True
				elif toggleTrue.replace("\n","") == eachLine.replace("\n",""):
					allTextInConfigFile = allTextInConfigFile.replace(toggleTrue,toggleFalse,1)
					Close = True		
					
				modifyConfigFile = open("config.txt","w")
				modifyConfigFile.write(allTextInConfigFile)
				modifyConfigFile.close()
				modifyConfigFile.close()
				toggleOption = False
				if Close == True:
					break
		if options_menu_do_what == "1":
			pass
		elif options_menu_do_what == "2":
			pass
		elif options_menu_do_what == "3":
			editDensities()
		elif options_menu_do_what == "4":
			while True:
				option = input("""Are you sure you want to reset all of the options (including the custom densities)?

1. Yes

2. No

""")
				if option == "1":
					resetConfigFile = open("config.txt","w")
					resetConfigFile.write("""togglePaintTrue
toggleWeightTrue
!!Custom density 1
!%500
@@Custom density 2
@%1000
$$Custom density 3
$%1500""")
					resetConfigFile.close()
					break
				elif option == "2":
					break
				else:
					print(menuError)
		elif options_menu_do_what == "5":
			break
		else:
			print(menuError)
		
		
	