

def Charles(input: str):
	Cyrillic = {"А": 1, "а": 1, "Б": 2, "б": 2, "В": 3, "в": 3, "Г": 4, "г": 4, "Д": 5, "д": 5, "Е": 6, "е": 6, "Ё": 7, "ё": 7, "Ж": 8, "ж": 8, "З": 9, "з": 9, "И": 10, "и": 10, "Й": 11, "й": 11, "К": 12, "к": 12, "Л": 13, "л": 13, "М": 14, "м": 14, "Н": 15, "н": 15, "О": 16, "о": 16, "П": 17, "п": 17, "Р": 18, "р": 18, "С": 19, "с": 19, "Т": 20, "т": 20, "У": 21, "у": 21, "Ф": 22, "ф": 22, "Х": 23, "х": 23, "Ц": 24, "ц": 24, "Ч": 25, "ч": 25, "Ш": 26, "ш": 26, "Щ": 27, "щ": 27, "Ь": 28, "ь": 28, "Ы": 29, "ы": 29, "Ъ": 30, "ъ": 30, "Э": 31, "э": 31, "Ю": 32, "ю": 32, "Я": 33, "я": 33}
	print(Cyrillic)
	cipher = ""
	for k in Cyrillic:
		print(k, bin(Cyrillic[k]))
	for letter in input:
		n = Cyrillic[letter]
		print(n)
		n ^= 0b11111111
		n >>= 3
		print(bin(n))
		for key in Cyrillic:
			if Cyrillic[key] == n:
				cipher += key
				break
	print(cipher)
Charles("Чарльз")