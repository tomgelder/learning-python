# Trying to make this a function
pyg = "ay"
first_letter = ""
second_letter = ""
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
vowels = ["a",  "e",  "i",  "o",  "u"]

def pyg_latin(word):

	while len(word) == 0 or not word.isalpha():
		print "Please use only one word made up only of letters"
		word = raw_input("What would you like us to translate for you?\n=> ")
	
	for x in consonants:
		if word[0].lower() == x:       
			first_letter = x             
			for z in consonants:         
				if word[1].lower() == z:   
					second_letter = z
					translated = word[2:len(word)] + "-" + first_letter + second_letter + pyg
					return translated
				elif len(second_letter) == 0:                     
					translated = word[1:len(word)] + "-" + first_letter + pyg
					return translated
		else:													 
			for y in vowels:						 
				if word[0].lower() == y:
					translated = word + "-yay"
					return translated

pyg_latin(raw_input("What would you like us to translate for you?\n=> "))
