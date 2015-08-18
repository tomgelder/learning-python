word = "frapuccino"
pyg = "ay"
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
vowels = ["a",  "e",  "i",  "o",  "u"]  # This may not be necessary, as there is a check for non-alphas 

for x in consonants:
	if word[0].lower() == x:       # checks if the first letter is a consonant
		first_letter = x             # if it is, it creates a new variable
		for z in consonants:         # it then loops through again checking the second letter
			if word[1].lower() == z:   # if it's a consonant, it makes a two letter construction
				second_letter = z
				translated = word[2:len(word)] + "-" + first_letter + second_letter + pyg
			else:                      # if there's not a consonant, it makes a one letter construction
				translated = word[1:len(word)] + "-" + first_letter + pyg
	else:													 # if it's not a consonant, it must be a vowel
		for y in vowels:						 # loop through the vowel list
			if word[0].lower() == y:
				translated = word + "-yay"

print translated