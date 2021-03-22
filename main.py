import os
from linux import *
from docker import *
from aws import *
from hadoop import *
from k8s import *

#Task Main Menu

while True:
	os.system("clear")
	os.system("tput setaf 1")
	print("\t\t--------------------")
	print("\t\t| Welcome MYITA !! |")
	print("\t\t--------------------")
	os.system("tput setaf 7")

	os.system("tput setaf 2")
	print("""
	\t\tPress 1 : For Linux
	\t\tPress 2 : For Docker
	\t\tPress 3 : For Hadoop
	\t\tPress 4 : For AWS
       \t\tPress 5 : For Kubernates
	\t\tPress 6 : To Exit
	""")
	
	print()
	os.system("tput setaf 3")
	ch = input("\t\t\tEnter your Choice : ")
	os.system("tput setaf 7")	

	if int(ch) == 1:
		linux_menu()

	elif int(ch) == 2:
		docker_menu()	

	elif int(ch) == 3:
		hadoop_menu()

	elif int(ch) == 4:
		aws_menu()
	elif int(ch) == 5:
		k8s_menu()	

	else:
		os.system("clear")
		print()
		os.system("tput setaf 1")
		print("\t    ---------------------------------------")
		print("\t    | Thank You for Using MYITA !! |")
		print("\t    ---------------------------------------")
		os.system("tput setaf 7")
		print()
		exit()
