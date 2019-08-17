#Code by IgneousCompas
from menu import * 

while True:
	while True:
		print("""\n•What do you want to do?

1. Calculate the area of a figure

2. Calculate the the volume of a solid

3. Calculate the area of a solid

4. Options (toggle neat facts about calculated areas/volumes)

5. ← Quit""")
		main_menu_do_what = input("\n")
		if main_menu_do_what == "1":
			areaMenu()
			break
		if main_menu_do_what == "2":
			volumeMenu()
			break
		if main_menu_do_what == "3":
			areaSolidsMenu()
			break
		elif main_menu_do_what == "4":
			optionsMenu()
			break
		elif main_menu_do_what == "5":
			quit()
		else:
			print("•Thats not an option. To choose an option, enter the number corresponding to the option that you want to access")