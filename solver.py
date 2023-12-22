class LetterBox:
	def __init__(self, input, dictionary):
		self.input = input.lower()
		self.sides = {side for side in self.input.split('-')}
		self.letters = {letter for side in self.sides for letter in side}
		self.root = TrieNode('')
		print("Creating dictionary...")
		with open(dictionary) as f:
			for line in f.readlines():
				self.insert(line.strip().lower())

	def insert(self, word):
		node = self.root

		for char in word:
			if char in node.children:
				node = node.children[char]
			else:
				new_node = TrieNode(char)
				node.children[char] = new_node
				node = new_node
		node.is_end = True

	def findValidWords(self):
		valid_words = []

		for side in self.sides:
			for letter in side:
				if letter in self.root.children:
					valid_words += self.makeWords(self.root.children[letter], letter, side)
		return valid_words

	def makeWords(self, node, prefix, side):
		if node.is_end:
			words = [prefix]
		else:
			words = []
		if node.children:
			for next_side in self.sides - {side}:
				for next_letter in next_side:
					if next_letter in node.children:
						new_prefix = prefix + next_letter
						words += self.makeWords(node.children[next_letter], new_prefix, next_side)
		return words

	def findSolutions(self, words):
		solutions = []
		for word1 in words:
			second_words = [word for word in words if word[0] == word1[-1]]
			for word2 in second_words:
				pair = {word1, word2}
				word_combo = word1 + word2
				word_set = {char for char in word_combo}
				if word_set == self.letters:
					solutions.append(word1.upper() + '-' + word2.upper())
		return solutions

	def printSolutions(self, solutions):
		for sol in solutions:
			print(sol)


class TrieNode:
	def __init__(self, char):
		self.char = char
		self.is_end = False
		self.children = {}

def checkString(s):
	if len(s) != 15:
		return False
	for char in s:
		if char.isalpha() or char == '-':
			continue
		else:
			return False
	split = s.split('-')
	for section in split:
		if len(section) != 3:
			return False
	return True

letters = 'tlq-srw-ecn-uao'
answer = input("Welcome to this Letter Boxed solver! Would you like to enter your own puzzle? (Y or N): ")
if answer == "Y" or answer == "y":
	done = False
	while not done:
		letters = input("Please enter your puzzle with dashes (-) in between each side: ")
		if checkString(letters):
			done = True
		else:
			print("Sorry, your input was not in a valid format. Please try again.")
else:
	print("Ok! We will use the following puzzle: TLQ-SRW-ECN-UAO")

box = LetterBox(letters, 'words.txt')

print("Finding valid words...")
valid = box.findValidWords()

print("Finding solutions...")
solutions = box.findSolutions(valid)
print("Found " + str(len(solutions)) + " valid solutions:")
box.printSolutions(solutions)