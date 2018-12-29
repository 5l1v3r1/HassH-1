#!/usr/bin/python2
import os, platform, time, random
sembarang = random.randint(1,3)

err_keyint = "[!] Keyboard Interrupted by User !!!"
err_invld = "[!] Error: Invalid number selected !"
err_invalid = "[!] Error: Invalid option !"
err_blank = "[!] Error: Don't leave it blank !"
err_cantcon = "[!] Error: Can't connect with Target !"
err_cantconp = '''[!] Error: Can't connect to Target's Port !
    Are You sure that Port is opened and allow connection ?
    Try to scan it with Nmap'''
err_cantfind = '''[!] Error: Can't reach Target ! Are You sure Your Target
	is Online ? Are the URL is correct ? Are You Online ?'''
err_cantbck = "[!] Error: Can't go back ! this is the main Modules !"
err_notavai = '''[!] Sorry: This Modules is currently not available right now...
    This Modules maybe Unlocked in the next Version of M-Evil Tools :)
     so...stay with Me :)'''
err_wlist = '''[!] Error: Can't open List File ! The file is too large
    or the File is not exists or corrupted !
    Please Try Again !'''
err_makeoutpt = '''[!] Error: Can't create File! Are You try to make File in root area
    Location ??? Try to save it to another place !!!'''
banner1 = '''
      d8b                                 d8b      
      ?88                                 ?88      
       88b                                 88b     
       888888b  d888b8b   .d888b, .d888b,  888888b 
       88P `?8bd8P' ?88   ?8b,    ?8b,     88P `?8b
      d88   88P88b  ,88b    `?8b    `?8b  d88   88P
     d88'   88b`?88P'`88b`?888P' `?888P' d88'   88b

 What's happend to HashKiller Mr.Hacker? You are Offline?
  No Internet? Its okay...I am help You for free, and..
              I am actually work OFFLINE

      ---{ HassH v1 }---{ Coded by M-XacT-666 }---'''
banner2 = '''
         _     _                 _     _
        | |   | |               | |   | |
        | |__ | | ____  ___  ___| |__ | |
        |  __)| |/ _  |/___)/___)  __)| |
        | |   | ( ( | |___ |___ | |   | |
        |_|   |_|\_||_(___/(___/|_|   |_|

 Let Me guess...after play with some SQLinjection
 got some Password in database, forget to Crack it
 and You lost Your internet connection? so You use
 OFFLINE Hash cracker? LOL XD...Its okay Mr.Hacker

   ---{ HassH v1 }---{ Coded by M-XacT-666 }---'''
banner3 = '''
  MMMMMMMMMMMM                            MMMMMMMMMMMM
  M""MMMMM""MM                            M""MMMMM""MM 
  M  MMMMM  MM                            M  MMMMM  MM 
  M         `M .d8888b. .d8888b. .d8888b. M         `M 
  M  MMMMM  MM 88'  `88 Y8ooooo. Y8ooooo. M  MMMMM  MM 
  M  MMMMM  MM 88.  .88       88       88 M  MMMMM  MM 
  M  MMMMM  MM `88888P8 `88888P' `88888P' M  MMMMM  MM 
  MMMMMMMMMMMM                            MMMMMMMMMMMM

  Looks like Mr.Hacker need to secure their Password..
      whats Your plan? Double-Hashed-Password ???

     ---{ HassH v1 }---{ Coded by M-XacT-666 }---'''
def clearscreen(x):
	if x == "Windows":
		os.system('CLS')
	else:
		os.system('clear')
def jeda():
  print ""
  raw_input(">>> Press [ENTER] To Continue...")
def tidur(x):
	time.sleep(x)
def keluar():
	print ""
	print "[*] Closing Tools..."
	tidur(1)
	print "[^] Thanks for using My Tools !"
	exit()
def banner(x):
	if x == 1:
		print banner1
	elif x == 2:
		print banner2
	elif x == 3:
		print banner3
def judul():
	banner(sembarang)