plain = "abcdefghijklmnopqrstuvwxyz"
def toCipher( val ):
	res = ""
	for i in range(0,len(val)):
		res += val[ i - 7 ]
	return res

cipher = toCipher( plain )

def encrypt( msg ):
	res = ""

	for i in range(0,len(msg)):
		for o in range(0,len(plain)):
			if msg[i] == plain[o]:
				res += cipher[o]
		if msg[i] == " ":
			res += " "
	return res

def decrypt( msg ):
	res = ""

	for i in range(0,len(msg)):
		for o in range(0,len(cipher)):
			if msg[i] == cipher[o]:
				res += plain[o]
		if msg[i] == " ":
			res += " "
	return res


def preload():
	stat = True
	while stat:
		cmd = str(input("Encrypt/Decrypt ( E / D )-> "))
		if cmd.lower() == "e" or cmd.lower() == "encrypt":
			msg = str(input("Message : "))
			print(encrypt( msg.lower() ))
		elif cmd.lower() == "d" or cmd.lower() == "decrypt":
			msg = str(input("Hidden Message : "))
			print(decrypt( msg.lower() ))

if __name__ == "__main__":
	try:
		preload()
	except KeyboardInterrupt:
		print("\n[ ! ] Interrupted by CTRL + C")
	except EOFError:
		print("\n[ ! ] EOFError ")
	except Exception as e:
		print("\n[ ! ] An exection has occured : "+e)