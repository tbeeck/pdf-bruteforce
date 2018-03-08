import sys
import PyPDF2
import bruteforcer

def main(argv):
	if len(sys.argv) != 3:
		print("Usage: pdfbf.py <file> <wordlist>\n")
	else:
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
					guesser = bruteforcer.Guesser()
					guesser.brute(wordList, pdfReader)
				except IOError:
					print("There was an IO error")
		except IOError:
			print("There was an IO error")

if __name__ == "__main__":
	main(sys.argv)
