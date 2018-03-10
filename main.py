import sys
import argparse
import PyPDF2
import bruteforcer
import lists
import signal

def main(argv):
	signal.signal(signal.SIGINT, lambda x,y: sys.exit(0)) # Ctrl+c
	argParser = argparse.ArgumentParser()
	argParser.add_argument("pdf", help="Designate a pdf file")
	argParser.add_argument("-w", help="Use a wordlist")
	argParser.add_argument("-b", help="Bruteforce every possible password",
		action="store_true")
	argParser.add_argument("-l", help="Chose character lists for -b argument")
	argParser.add_argument("-c", help="Designate custom character set")
	argParser.add_argument("-max", help="Chose maximum length of password",
		type=int)
	argParser.add_argument("-min", help="Chose minimum length of password",
		type=int)
	args = argParser.parse_args()
	print(args)
	try:
		print("[*] Opening PDF...")
		pdfReader = PyPDF2.PdfFileReader(open(args.pdf, 'rb'))
		if pdfReader.isEncrypted == False:
			print("[!] Operation failed, the PDF is not encrypted.")
			exit()
		else:
			print("[*] PDF is encrypted, continuing...")
			try:
				guesser = bruteforcer.Guesser()
				guesserMinLength = 1
				guesserMaxLength = 0
				if args.min or args.max:
					print("[*] Setting length requirements: "+str(args.min)+
					"-"+str(args.max) + " characters")
					guesserMaxLength = args.max
					guesserMinLength = args.min
				if args.w:
					print("[*] Opening wordlist...")
					wordList = open(args.w, 'rbU')
					guesser.bruteWordlist(wordList, pdfReader, guesserMinLength,
						guesserMaxLength)
				elif args.b:
					print("[*] Compiling lists...")
					selectedLists = []
					if args.l:
						if "l" in args.l:
							selectedLists.extend(lists.Lists.lower)
						if "c" in args.l:
							selectedLists.extend(lists.Lists.upper)
						if "s" in args.l:
							selectedLists.extend(lists.Lists.symbols)
					guesser.bruteRandom(selectedLists, pdfReader,
						guesserMinLength, guesserMaxLength)

			except IOError:
				print("There was an IO error")
	except IOError:
		print("There was an IO error. Is the file name correct?")

if __name__ == "__main__":
	main(sys.argv)
