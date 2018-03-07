from __future__ import print_function
import sys
import PyPDF2

def brute(dictionary, reader):
	# colorama.init() #windows sucks
	currentLine = 1
	for line in dictionary.readlines():
		sys.stdout.write("\r\033[K"+"Attempt "+str(currentLine)+", trying: "  +
			str(line.replace("\n","")))# end='\r')
		sys.stdout.flush() # re-comment if on windows
		if reader.decrypt(line.replace("\n","")) == 1:
			print("\nSuccess! The password was: " + line)
			return
		else:
			currentLine = currentLine + 1
	print("\nThe password is not in the wordlist :(")
	return

def main(argv):
	if len(sys.argv) != 3:
		print("Usage: pdfbf.py <file> <wordlist>\n")
	else:
		#print("Tim's PDF bruteforcer, brought to you by FYM Hot Sauce")
		try:
			print("[*] Opening PDF...")
			pdfReader = PyPDF2.PdfFileReader(open(sys.argv[1], 'rb'))
			print("[*] Opening wordlist...")
			wordList = open(sys.argv[2], 'rbU')
			if pdfReader.isEncrypted == False:
				print("Operation failed, the PDF is not encrypted!")
				exit()
			else:
				print("[*] PDF is encrypted, continuing...")
				try:
					brute(wordList, pdfReader)
				except IOError:
					print("There was an IO error")
		except IOError:
			print("There was an IO error")

if __name__ == "__main__":
	main(sys.argv)
