def count_characters(string):
	dict_something ={}

	for c in string:
		if (c in dict_something):
			dict_something [c] += 1
		else:
			dict_something [c] = 1
	return dict_something
print(count_characters("abcda"))
