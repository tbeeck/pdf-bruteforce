import sys
import PyPDF2

class Guesser:

    def bruteWordlist(self, dictionary, reader, minLength=1, maxLength=0):
    	currentLine = 1
    	for line in dictionary.readlines():
            if (len(line.replace("\n","")) >= minLength or minLength == 0) and \
                (len(line.replace("\n","")) <= maxLength or maxLength == 0):
        		sys.stdout.write("\r\033[K"+"Attempt "+str(currentLine)+
                    ", trying: " + str(line.replace("\n","")))
        		sys.stdout.flush()
        		if reader.decrypt(line.replace("\n","")) == 1:
        			print("\nSuccess! The password was: " + line)
        			return
        		else:
        			currentLine = currentLine + 1
    	print("\nThe password is not in the wordlist.")
    	return
