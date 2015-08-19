word = "goose"
pyg = "ay"
first_letter = ""
second_letter = ""
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
vowels = ["a",  "e",  "i",  "o",  "u"]  # This may not be necessary, as there is a check for non-alphas 

for x in consonants:
	if word[0].lower() == x:       
		first_letter = x             
		for z in consonants:         
			if word[1].lower() == z:   
				second_letter = z
				translated = word[2:len(word)] + "-" + first_letter + second_letter + pyg
			elif len(second_letter) == 0:                     
				translated = word[1:len(word)] + "-" + first_letter + pyg
	else:													 
		for y in vowels:						 
			if word[0].lower() == y:
				translated = word + "-yay"

print translated