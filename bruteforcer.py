import sys
import PyPDF2
import itertools

class Guesser:

    def bruteWordlist(self, dictionary, reader, minLength=1, maxLength=0):
    	currentLine = 1
    	for line in dictionary.readlines():
            if (len(line.replace("\n","")) >= minLength or minLength == 1) and \
                (len(line.replace("\n","")) <= maxLength or maxLength == None):
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

    def bruteRandom(self, list, reader, minLength=1, maxLength=0):
        attempt = 0
        for lengths in range(minLength, maxLength + 1):
            for guess in itertools.product(list, repeat=lengths):
                attempt = attempt + 1
                guess = "".join(guess)
                sys.stdout.write("\r\033[K"+"Attempt "+str(attempt)+", trying: "
                    + guess)
        	sys.stdout.flush()
                if reader.decrypt(guess) == 1:
            		print("\nSuccess! The password was: " + guess)
    			return
        print("\nThe password was not discovered.")
        return
