import os
while True:
	print("enter ur choice what u want : ",end='')
	p=input()
	if (("run" in p) or ("execute" in p) or ("launch" in p)) and (("gedit" in p) or ("editor" in p) or ("notepad" in p)):
		os.system("gedit")
	elif (("run" in p) or ("execute" in p) or ("launch" in p)) and ((("firefox" in p) or ("browser" in p)) and ("chrome" not in p)):
		os.system("firefox")
	elif (("run" in p) or ("execute" in p) or ("launch" in p)) and (("rhythmbox" in p) or ("audio" in p)):
		os.system("rhythmbox")
	elif (("run" in p) or ("execute" in p) or ("launch" in p)) and (("vlc" in p) or ("video" in p)):
		os.system("vlc")
	elif (("run" in p) or ("execute" in p) or ("launch" in p)) and ("calendar" in p):
		os.system("cal")
	elif (("run" in p) or ("execute" in p) or ("launch" in p)) and (("virtualbox" in p) or ("virtual box" in p)):
		os.system("virtualbox")
	elif (("run" in p) or ("execute" in p) or ("launch" in p)) and (("cheese" in p) or ("camera" in p) or ("cam" in p)):
		os.system("cheese")
	elif (("run" in p) or ("execute" in p) or ("launch" in p)) and ("terminal" in p):
		os.system("gnome-terminal")
	elif (("run" in p) or ("execute" in p) or ("launch" in p)) and ("calculator" in p):
		os.system("bc")
	elif (("exit" in p) or ("stop" in p) or ("terminate" in p) or ("quit" in p)):
		break 
	else:
		print("sorry try again")
