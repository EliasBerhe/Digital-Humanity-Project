import nltk
nltk.download("punkt")

def accessComp1(textfolder, textfile):
	"""takes paper number and opens the file it is in """

	inFile = open('comparison data/' + str(textfolder) +'/' + str(textfile).lower()+ ".txt")
	return inFile

def readText1(textfolder,textfile):
	"""uses accessText to return the wholeText"""

	wholeText = accessComp1(textfolder,textfile).read()
	#edit readText to return a list 
	# wholeText = wholeText.split()
	accessComp1(textfolder,textfile).close()
	return wholeText
	
def Type_Token_Ratio1(textfolder,textfile):
	""" takes wordDict and calculates to Type Token Ratio """

	firstlist = nltk.word_tokenize(readText1(textfolder,textfile))
	filterList = removePunkt1(firstlist)
	wordDict = makeDict1(filterList)
	listLength = 0
	for key in wordDict:
		listLength += wordDict[key]
	return round((len(wordDict)/listLength), 3)


def makeDict1(wordList):
	"""takes the wordList and puts it into a dictionary"""

	dictionary = dict()
	
	for word in wordList:
		if word.lower() not in dictionary:
			dictionary[word.lower()] = 1
		else:
			dictionary[word.lower()] += 1

	return dictionary

def removePunkt1(wordList):
	"""takes a wordList and removes all non words and adds them to a new filterList"""

	filterList= []
	for item in wordList:
		if item[0].isalpha():
			newString = ""
			# we editied to remove any punctuations in a word
			for char in item:
				#print(item)
				if char.isalpha():
					#print(char)
					newString += char
					#print(newString)
			filterList.append(newString)
	return filterList

def avgSenLen1(textfolder,textfile):
	"""takes a list of sentences and finds the average number of words in the sentences """

	senList = nltk.sent_tokenize(readText1(textfolder,textfile))
	total_words = 0
	for sentence in senList:
		sent = nltk.word_tokenize(sentence)
		#print(sent)
		filtSent = removePunkt1(sent)
		for word in filtSent:
			total_words = total_words + 1
			#print(total_words)
		
	return round((total_words/len(senList)),3)
		
def avgPunkt1(textfolder,textfile):
	"""Takes a sentence list and calculates the average punctuation in the sentences"""

	senList = nltk.sent_tokenize(readText1(textfolder,textfile))
	total_punkt = 0
	for sentence in senList:
		sent = nltk.word_tokenize(sentence)
		#print(sent)
		for word in sent:
			if not word.isalnum():
				total_punkt = total_punkt + 1
			#print(total_words)
	return round((total_punkt/len(senList)),3)	


# change strategy from here when professor fruchter had talk to us about using dictionaries rather than lists, so we changed from a list based function to a dictionary based function
