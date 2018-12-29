#!/usr/bin/python2
####################################
import sys,platform,hashlib,datetime
sys.path.append('./lib/')
import tools_core
####################################
opsys = platform.system()
sekarang = datetime.datetime.now()
waktufull = str(sekarang.year) + "-" + str(sekarang.month) + "-" + str(sekarang.day) + "_" + str(sekarang.hour) + "-" + str(sekarang.minute)
#hassh_output = './result/{0}_{1}.txt'.format(mode_nya,waktufull)
#hassh_wlist = './wordlist/mxact666_password.txt'
#32,40,56,64,96,128

def break_coeg():
	print ""
	print "[+] Job Complete..."
	tools_core.keluar()
def dec2():
	list_hash = []
	hasil_crack = []
	tools_core.clearscreen(opsys)
	tools_core.judul()
	print ""
	print "[IMPORTANT] !!!"
	print " Before using this Tools...You must save list of Hash in one File"
	print " and remeber...the Hash Type for all hash in the List must same..."
	tools_core.jeda()
	print ""
	print "[?] Enter the File contain Hash List to Crack"
	dec2_hfile = raw_input("hassh (crack_hashfile):HASH_FILE > ")
	if dec2_hfile == "":
		print tools_core.err_blank
		tools_core.jeda()
		dec2()
	elif dec2_hfile == "exit":
		tools_core.keluar()
	print "[>] Set Hash File ---> %s" % dec2_hfile
	print ""
	print "[*] Checking File...then Open and Reading it..."
	try:
		dec2_bacahash = open(dec2_hfile,'r').readlines()
		dec2_jumlahhash = str(len(dec2_bacahash))
		print "[+] Found {} line of Hash".format(dec2_jumlahhash)
		for i in dec2_bacahash:
			a = i.strip()
			list_hash.append(a)
		print "[+] Saved to HassH List..."
		if len(list_hash[0]) == 32:
			dec2_type = "md5"
		elif len(list_hash[0]) == 40:
			dec2_type = "sha1"
		elif len(list_hash[0]) == 56:
			dec2_type = "sha224"
		elif len(list_hash[0]) == 64:
			dec2_type = "sha256"
		elif len(list_hash[0]) == 96:
			dec2_type = "sha384"
		elif len(list_hash[0]) == 128:
			dec2_type = "sha512"
		else:
			print "[!] Error: Hash Type is not Supported !!!"
			print "    Please try with another Hash List !!!"
			tools_core.keluar()
		print "[+] Hash Type is : %s" % dec2_type
		print "[+] Done"
	except:
		print "[!] Error: Directory or File is doesn't exist !!!"
		print tools_core.err_wlist
		tools_core.jeda()
		dec2()
	print ""
	print "[?] Specify Wordlist to use ! (Leave blank to use mine...)"
	dec2_wlist = raw_input("hassh (crack_hashfile): WORDLIST > ")
	if dec2_wlist == "exit":
		tools_core.keluar()
	elif dec2_wlist == "":
		dec2_wlist = './wordlist/mxact666_password.txt'
	print "[>] Set Wordlist ---> %s" % dec2_wlist
	print ""
	print "[*] Preparing Wordlist..."
	try:
		baca_wlist = open(dec2_wlist,'r').readlines()
		dec2_jumlah = str(len(baca_wlist))
		print "[+] {} Word-Phrase is Loaded !".format(dec2_jumlah)
		print "[+] Done"
	except IOError:
		print "[!] Error: Can't find Wordlist !"
		print "     Check the Directory or Wordlist Location !"
		tools_core.jeda()
		dec2()
	except:
		print tools_core.err_wlist
		tools_core.jeda()
		dec2()
	print ""
	print "[*] Cracking Hash...Please be patient...this may take times..."
	print ""
	hitung = 0
	for a in baca_wlist:
		hitung += 1
		try:
			dicoba = a.strip()
			if dec2_type == "md5":
				before = hashlib.md5(dicoba).hexdigest()
				if before in list_hash:
					#print ""
					hasil_crack.append("{0} : {1}".format(before,dicoba))
					print "[ CRACKED ]==[{0}/{1}]==[{2}]==> {3}".format(hitung,dec2_jumlah,before,dicoba)
					#print ""
				else:
					#print "[ INVALID ]==[{0}/{1}]==[{2}]==> {3}".format(hitung,dec2_jumlah,before,dicoba)
					pass
			elif dec2_type == "sha1":
				before = hashlib.sha1(dicoba).hexdigest()
				if before in list_hash:
					#print ""
					hasil_crack.append("{0} : {1}".format(before,dicoba))
					print "[ CRACKED ]==[{0}/{1}]==[{2}]==> {3}".format(hitung,dec2_jumlah,before,dicoba)
					#print ""
				else:
					#print "[ INVALID ]==[{0}/{1}]==[{2}]==> {3}".format(hitung,dec2_jumlah,before,dicoba)
					pass
			elif dec2_type == "sha224":
				before = hashlib.sha224(dicoba).hexdigest()
				if before in list_hash:
					#print ""
					hasil_crack.append("{0} : {1}".format(before,dicoba))
					print "[ CRACKED ]==[{0}/{1}]==[{2}]==> {3}".format(hitung,dec2_jumlah,before,dicoba)
					#print ""
				else:
					#print "[ INVALID ]==[{0}/{1}]==[{2}]==> {3}".format(hitung,dec2_jumlah,before,dicoba)
					pass
			elif dec2_type == "sha256":
				before = hashlib.sha256(dicoba).hexdigest()
				if before in list_hash:
					#print ""
					hasil_crack.append("{0} : {1}".format(before,dicoba))
					print "[ CRACKED ]==[{0}/{1}]==[{2}]==> {3}".format(hitung,dec2_jumlah,before,dicoba)
					#print ""
				else:
					#print "[ INVALID ]==[{0}/{1}]==[{2}]==> {3}".format(hitung,dec2_jumlah,before,dicoba)
					pass
			elif dec2_type == "sha384":
				before = hashlib.sha384(dicoba).hexdigest()
				if before in list_hash:
					#print ""
					hasil_crack.append("{0} : {1}".format(before,dicoba))
					print "[ CRACKED ]==[{0}/{1}]==[{2}]==> {3}".format(hitung,dec2_jumlah,before,dicoba)
					#print ""
				else:
					#print "[ INVALID ]==[{0}/{1}]==[{2}]==> {3}".format(hitung,dec2_jumlah,before,dicoba)
					pass
			elif dec2_type == "sha512":
				before = hashlib.sha512(dicoba).hexdigest()
				if before in list_hash:
					#print ""
					hasil_crack.append("{0} : {1}".format(before,dicoba))
					print "[ CRACKED ]==[{0}/{1}]==[{2}]==> {3}".format(hitung,dec2_jumlah,before,dicoba)
					#print ""
				else:
					#print "[ INVALID ]==[{0}/{1}]==[{2}]==> {3}".format(hitung,dec2_jumlah,before,dicoba)
					pass
		except KeyboardInterrupt:
			print ""
			print tools_core.err_keyint
			break
	print ""
	print "[+] Cracked Hash [{0}/{1}]: ".format(len(hasil_crack),len(list_hash))
	for a in hasil_crack:
		print "[>>>] " + str(a)
def dec1():
	tools_core.clearscreen(opsys)
	tools_core.judul()
	print ""
	print "[?] Enter Your Hash to crack into Text"
	dec1_hash = raw_input("hassh (crack_hash):ENTER HASH > ")
	if dec1_hash == "":
		print tools_core.err_blank
		tools_core.jeda()
		dec1()
	elif dec1_hash == "exit":
		tools_core.keluar()
	print "[>]  Set Hash ---> %s" % dec1_hash
	print ""
	print "[*] Checking Hash Type..."
	if len(dec1_hash) == 32:
		print "[+] Hash Type is MD5"
		dec1_type = "md5"
	elif len(dec1_hash) == 40:
		print "[+] Hash Type is SHA1"
		dec1_type = "sha1"
	elif len(dec1_hash) == 56:
		print "[+] Hash Type is SHA224"
		dec1_type = "sha224"
	elif len(dec1_hash) == 64:
		print "[+] Hash Type is SHA256"
		dec1_type = "sha256"
	elif len(dec1_hash) == 96:
		print "[+] Hash Type is SHA384"
		dec1_type = "sha384"
	elif len(dec1_hash) == 128:
		print "[+] Hash Type is SHA512"
		dec1_type = "sha512"
	else:
		print "[-] Hash Type not found !!!"
		print "    This Tools not support this Hash Type !!!"
		print "    You can try to use Online Cracker like HashKiller"
		tools_core.jeda()
		dec1()
	print ""
	print "[?] Specify Wordlist to use ! (Leave blank to use mine...)"
	dec1_wlist = raw_input("hassh (crack_hash): WORDLIST > ")
	if dec1_wlist == "exit":
		tools_core.keluar()
	elif dec1_wlist == "":
		dec1_wlist = './wordlist/mxact666_password.txt'
	print "[>] Set Wordlist ---> %s" % dec1_wlist
	print ""
	print "[*] Preparing Wordlist..."
	try:
		baca = open(dec1_wlist,'r').readlines()
		dec1_jumlah = str(len(baca))
		print "[+] {} Word-Phrase is Loaded !".format(dec1_jumlah)
		print "[+] Done"
	except IOError:
		print "[!] Error: Can't find Wordlist !"
		print "     Check the Directory or Wordlist Location !"
		tools_core.jeda()
		dec1()
	except:
		print tools_core.err_wlist
		tools_core.jeda()
		dec1()
	print ""
	hitung = 0
	for line in baca:
		try:
			hitung += 1
			baris = line.strip()
			if dec1_type == "md5":
				a = hashlib.md5(baris).hexdigest()
				if str(a) == str(dec1_hash):
					print ""
					print "[ ACCEPT ]===[{0}/{1}]===[{2}]===> {3}".format(hitung,dec1_jumlah,a,baris)
					break
				else:
					print "[ INVALID ]===[{0}/{1}]===[{2}]===> {3}".format(hitung,dec1_jumlah,a,baris)
					pass
			elif dec1_type == "sha1":
				a = hashlib.sha1(baris).hexdigest()
				if str(a) == str(dec1_hash):
					print ""
					print "[ ACCEPT ]===[{0}/{1}]===[{2}]===> {3}".format(hitung,dec1_jumlah,a,baris)
					break
				else:
					print "[ INVALID ]===[{0}/{1}]===[{2}]===> {3}".format(hitung,dec1_jumlah,a,baris)
					pass
			elif dec1_type == "sha224":
				a = hashlib.sha224(baris).hexdigest()
				if str(a) == str(dec1_hash):
					print ""
					print "[ ACCEPT ]===[{0}/{1}]===[{2}]===> {3}".format(hitung,dec1_jumlah,a,baris)
					break
				else:
					print "[ INVALID ]===[{0}/{1}]===[{2}]===> {3}".format(hitung,dec1_jumlah,a,baris)
					pass
			elif dec1_type == "sha256":
				a = hashlib.sha256(baris).hexdigest()
				if str(a) == str(dec1_hash):
					print ""
					print "[ ACCEPT ]===[{0}/{1}]===[{2}]===> {3}".format(hitung,dec1_jumlah,a,baris)
					break
				else:
					print "[ INVALID ]===[{0}/{1}]===[{2}]===> {3}".format(hitung,dec1_jumlah,a,baris)
					pass
			elif dec1_type == "sha384":
				a = hashlib.sha384(baris).hexdigest()
				if str(a) == str(dec1_hash):
					print ""
					print "[ ACCEPT ]===[{0}/{1}]===[{2}]===> {3}".format(hitung,dec1_jumlah,a,baris)
					break
				else:
					print "[ INVALID ]===[{0}/{1}]===[{2}]===> {3}".format(hitung,dec1_jumlah,a,baris)
					pass
			elif dec1_type == "sha512":
				a = hashlib.sha512(baris).hexdigest()
				if str(a) == str(dec1_hash):
					print ""
					print "[ ACCEPT ]===[{0}/{1}]===[{2}]===> {3}".format(hitung,dec1_jumlah,a,baris)
					break
				else:
					print "[ INVALID ]===[{0}/{1}]===[{2}]===> {3}".format(hitung,dec1_jumlah,a,baris)
					pass
		except KeyboardInterrupt:
			print ""
			print tools_core.err_keyint
			exit()
	print ""
	print "[+] Job Complete..."
	tools_core.keluar()
def enc2():
	tools_core.clearscreen(opsys)
	tools_core.judul()
	print ""
	print "[?] Enter the File contain Text to convert into Hash File"
	enc2_tfile = raw_input("hassh (encrypt_textfile):TEXT_FILE > ")
	if enc2_tfile == "":
		print tools_core.err_blank
		tools_core.jeda()
		enc2()
	elif enc2_tfile == "exit":
		tools_core.keluar()
	print "[>] Set Text File ---> %s" % enc2_tfile
	print ""
	print "[*] Checking File...then Open and Reading it..."
	try:
		enc2_baca = open(enc2_tfile,'r').readlines()
		enc2_jumlah = str(len(enc2_baca))
		print "[+] Found {} line of Text !".format(enc2_jumlah)
		print "[+] Done"
	except:
		print "[!] Error: Directory or File is doesn't exist !!!"
		print tools_core.err_wlist
		tools_core.jeda()
		enc2()
	print ""
	print "[?] Where the Output File will be saved ?"
	enc2_output = raw_input("hassh (encrypt_textfile):OUTPUT_FILE > ")
	if enc2_output == "":
		print tools_core.err_blank
		tools_core.jeda()
		enc2()
	elif enc2_output == "exit":
		tools_core.keluar()
	print "[>] Set Output ---> %s" % enc2_output
	print ""
	print "[*] Now...Creating the Output File..."
	try:
		enc2_file = open(str(enc2_output),'w+')
		print "[+] Done"
	except:
		print "[!] Error: Directory is not found or not accessable !"
		tools_core.jeda()
		enc2()
	print ""
	print "[?] Choose Hash Type (md5,sha1,sha224,sha256,sha384,sha512)"
	enc2_type = raw_input("hassh (encrypt_textfile):HASH TYPE > ")
	if enc2_type == "":
		print tools_core.err_blank
		tools_core.jeda()
		enc2()
	elif enc2_type == "exit":
		tools_core.keluar()
	print "[>] Set Type ---> %s" % enc2_type
	print ""
	print "[*] Now Generating Hash from File..."
	for line in enc2_baca:
		baris = line.strip()
		if enc2_type == "md5":
			hasil = hashlib.md5(baris).hexdigest()
			enc2_file.write(hasil + "\n")
		elif enc2_type == "sha1":
			hasil = hashlib.sha1(baris).hexdigest()
			enc2_file.write(hasil + "\n")
		elif enc2_type == "sha224":
			hasil = hashlib.sha224(baris).hexdigest()
			enc2_file.write(hasil + "\n")
		elif enc2_type == "sha256":
			hasil = hashlib.sha256(baris).hexdigest()
			enc2_file.write(hasil + "\n")
		elif enc2_type == "sha384":
			hasil = hashlib.sha384(baris).hexdigest()
			enc2_file.write(hasil + "\n")
		elif enc2_type == "sha512":
			hasil = hashlib.sha512(baris).hexdigest()
			enc2_file.write(hasil + "\n")
		else:
			print "[!] Error: Hash Type is not Available !!!"
			break
	print "[+] Job Complete !!!"
	enc2_file.close()
	tools_core.jeda()
	main()
def enc1():
	tools_core.clearscreen(opsys)
	tools_core.judul()
	print ""
	print "[?] Enter Your Text to convert into Hash"
	enc1_text = raw_input("hassh (encrypt_text):ENTER TEXT > ")
	if enc1_text == "":
		print tools_core.err_blank
		tools_core.jeda()
		enc1()
	elif enc1_text == "exit":
		tools_core.keluar()
	print "[>] Set Text ---> %s" % enc1_text
	print ""
	print "[?] Choose Hash Type (md5,sha1,sha224,sha256,sha384,sha512)"
	enc1_type = raw_input("hassh (encrypt_text):HASH TYPE > ")
	if enc1_type == "":
		print tools_core.err_blank
		tools_core.jeda()
		enc1()
	elif enc1_type == "exit":
		tools_core.keluar()
	print "[>] Set Type ---> %s" % enc1_type
	print ""
	if enc1_type == "md5":
		print "[+] Hash Generated !!!"
		hasil = hashlib.md5(enc1_text.strip()).hexdigest()
		print "[>>>] MD5 : %s" % hasil
	elif enc1_type == "sha1":
		print "[+] Hash Generated !!!"
		hasil = hashlib.sha1(enc1_text.strip()).hexdigest()
		print "[>>>] SHA1 : %s" % hasil
	elif enc1_type == "sha224":
		print "[+] Hash Generated !!!"
		hasil = hashlib.sha224(enc1_text.strip()).hexdigest()
		print "[>>>] SHA224 : %s" % hasil
	elif enc1_type == "sha256":
		print "[+] Hash Generated !!!"
		hasil = hashlib.sha256(enc1_text.strip()).hexdigest()
		print "[>>>] SHA256 : %s" % hasil
	elif enc1_type == "sha384":
		print "[+] Hash Generated !!!"
		hasil = hashlib.sha384(enc1_text.strip()).hexdigest()
		print "[>>>] SHA384 : %s" % hasil
	elif enc1_type == "sha512":
		print "[+] Hash Generated !!!"
		hasil = hashlib.sha512(enc1_text.strip()).hexdigest()
		print "[>>>] SHA512 : %s" % hasil
	else:
		print "[!] Error: Hash Type is not Available !!!"
		tools_core.jeda()
		enc1()
	tools_core.jeda()
	main()

def main():
	tools_core.clearscreen(opsys)
	tools_core.judul()
	print ""
	print "[+] Mode: (1)---( Single Text to Hash )-----[ENCRYPT]"
	print "          (2)---( Text File to Hash File )--[ENCRYPT]"
	print "          (3)---( Crack Single Hash )-------[DECRYPT]"
	print "          (4)---( Crack List Hash on File )-[DECRYPT]"
	print ""
	pilihan_main = raw_input("hassh > ")
	if pilihan_main == "1":
		enc1()
	elif pilihan_main == "2":
		enc2()
	elif pilihan_main == "3":
		dec1()
	elif pilihan_main == "4":
		dec2()
	elif pilihan_main == "exit":
		tools_core.keluar()
	else:
		print tools_core.err_invld
		tools_core.jeda()

if __name__ == '__main__':
	main()