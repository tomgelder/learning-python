def bottle_song(bottles)
	for i in range(bottles,0,-1):
		if i == 1:
			print i, "bottle of beer on the wall,", i, "bottle of beer"
			print "You take one down, pass it around, no more bottles of beer on the wall."
		else:
			print i, "bottles of beer on the wall,", i, "bottles of beer" + "."
			print "You take one down, pass it around", i-1, "bottles of beer on the wall," + "!\n"

	print "No more bottles of beer on the wall, no more bottles of beer."
	print "Go to the store and buy some more, 99 bottles of beer on the wall."