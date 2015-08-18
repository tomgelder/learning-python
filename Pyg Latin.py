pyg = "ay"
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
vowels = ["a",  "e",  "i",  "o",  "u"]  # This may not be necessary, as there is a check for non-alphas 

word = raw_input('Enter a word:')

# While statement checks to make sure you have a word and will prompt a new entry till it gets it
while len(word) == 0 or not word.isalpha():
    print "Please enter only words, no numerals"
    word = raw_input("Enter a word:")

for x in consonants:
	if word[0].lower() == x:       # checks if the first letter is a consonant
		first_letter = x             # if it is, it creates a new variable
		for x in consonants:         # it then loops through again checking the second letter
			if word[1].lower() == x:   # if it's a consonant, it makes a two letter construction
				second_letter = x
				translated = word[2:len(word)] + "-" + first_letter + second_letter + pyg
			else:                      # if there's not a consonant, it makes a one letter construction
				translated = word[1:len(word)] + "-" + first_letter+pyg
	else:													 # if it's not a consonant, it must be a vowel
		for y in vowels:						 # loop through the vowel list
			if word[0].lower() == y:
				translated = word + "-yay"

print translated