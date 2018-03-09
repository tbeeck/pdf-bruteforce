import sys
import PyPDF2

class Guesser:

    def bruteWordlist(self, dictionary, reader, minLength=1, maxLength=0):
    	currentLine = 1
    	for line in dictionary.readlines():
            if (minLength <= len(line.replace("\n",""))) and ((maxLength >= len(line.replace("\n","")) or maxLength == None)):
        		sys.stdout.write("\r\033[K"+"Attempt "+str(currentLine)+", trying: " + str(line.replace("\n","")))
        		sys.stdout.flush()
        		if reader.decrypt(line.replace("\n","")) == 1:
        			print("\nSuccess! The password was: " + line)
        			return
        		else:
        			currentLine = currentLine + 1
    	print("\nThe password is not in the wordlist.")
    	return
