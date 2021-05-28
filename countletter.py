def single_letter_count(word,letter):
	if letter in word:
		return word.lower().count(letter.lower())
	return "Dosent exist"
	
print(single_letter_count("Akhila", "A"))