import random
	# INSTRUCTIONS

	# In case it is not clear, the Question appears first, then examples, then any hints and finally the function that you need to complete appears underneath:

	# <QUESTION>

	# <EXAMPLES>

	# <HINT>

	# You are allowed access to the internet for this assessment, you can also use the DOCUMENTATION that comes bundled with your Python installation.  You should already be comfortable accessing this documentation, but to summarise:

	# Access Python from you CLI

	# Type help() or for example help(str)



	# <QUESTION 1>    
	
	# Given a string, return a string where for every char in the original string, there are three chars.
    
    # <EXAMPLES>

	# one("The") → "TTThhheee"
	# one("AAbb") → "AAAAAAbbbbbb"
	# one("Hi-There") → "HHHiii---TTThhheeerrreee"

	# <HINT>
	# How does a for loop iterate through a string?

def one(input):
	newstring =""
	for i in range(0,len(input)):
		newstring = newstring + input[i] + input[i] + input[i]


	return newstring

	# <QUESTION 2>

    #  Write a function which returns the boolean True if the input is only divisible by one and itself.
    
    # The function should return the boolean False if not.

	# <EXAMPLES>

    # two(3) → True
    # two(8) → False

	# <HINT>
	# What operator will give you the remainder?
	# Use your CLI to access the Python documentation and get help manipulating strings - help(range).

def two(input):
	num = float(input)
	for i in range(2,input -1):
		
		if (int(num/i) == float(num/i) ):
			return False
	return True

	# <QUESTION 3>

    # Write a function which takes an integer input, a, and returns the sum a+aa+aaa+aaaa.

	# So if 2 was the input, the function should return 2+22+222+2222 which is 2468.

	# <EXAMPLES>

	# three(9) → 11106
	# three(5) → 6170

	# <HINT>
	# What happens if you multiply a string by a number?

def three(a):
	term2= str(a)+str(a)
	term3= term2 + str(a)
	term4= term3 + str(a)

	numwang = a + int(term2) + int( term3) + int(term4)

	return numwang

	# <QUESTION 4>

    # Given two Strings of equal length, 'merge' them into one String.

    # Do this by 'zipping' the Strings together.

    # Start with the first char of the first String.
    # Then add the first char from the second String.
    # Then add the second char from the first String.
    # And so on.

    # Maintain case.

    # You will not encounter whitespace.
    
    # <EXAMPLES>

	# four("String","Fridge") → "SFtrriidngge"
	# four("Dog","Cat") → "DCoagt"
	# four("True","Tree") → "TTrrueee" 
	# four("return","letter") → "rleettutrenr"

	# <HINT>
	# Use your CLI to access the Python documentation and get help manipulating strings - help(list.insert).
	# How would you seperate a string into characters?

def four(input1, input2):
	list1= list(input1)
	list2= list(input2)
	stringy = ""
	for i in range(0, len(input1)):
		stringy = stringy + str(list1[i]) + str(list2[i])
	return stringy

	# <QUESTION 5>

	# Write a function to randomly generate a list with 5 even numbers between 100 and 200 inclusive.
    
    # <EXAMPLES>
    
    # five() → [100,102,122,198,200]
    # five() → [108,104,106,188,200]
    # five() → [154,102,132,178,164]
    
	# <HINT>
	# There is a module which can be used to generate random numbers, this module is called random.
	# The random module contains a function called randint.

def five():
	random.seed()
	listy=[]
	for i in range(0, 5):
		listy.append(int(random.randrange(100,200,2)))

	return listy
    

	# <QUESTION 6>

	# Given a string, return the boolean True if it ends in "py", and False if not. 
	
	# Ignore Case.

	# For Example:

	# six("ilovepy") → True
	# six("welovepy") → True
	# six("welovepyforreal") → False
	# six("pyiscool") → False

	# <HINT>
	# There are no hints for this question.
    
def six(input):
	stringy = input.lower()
	z = len(input)
	if stringy[z-1 ] == "y" :
		if stringy[z - 2 ] == "p":
			return True
	return False

	# <QUESTION 7>

    # Given three ints, a b c, one of them is small, one is medium and one is large. 
	
	# Return the boolean True if the three values are evenly spaced, so the
	# difference between small and medium is the same as the difference between
	# medium and large. 
	
	# Do not assume the ints will come to you in a reasonable order.
    
    # <EXAMPLES>

	# seven(2, 4, 6) → True
	# seven(4, 6, 2) → True
	# seven(4, 6, 3) → False
	# seven(4, 60, 9) → False

	# <HINT>
	# There is a function for lists called sort.
	# Use the cli to access the documentation help(list.sort)

def seven(a, b, c):
	list1 = [a,b,c]
	list2 = sorted(list1)
	if (list2[1] - list2[0] == list2[2] - list2[1]):
		return True
	return False

	# <QUESTION 8>

    # Given a string and an integer, n, return a string that removes n letters from the 'middle' of the string.
	
	# The string length will be at least n, and be odd when the length of the input is odd, so there will always be a 'middle'.

    # <EXAMPLES>

	# eight("Hello", 3) → "Ho"
	# eight("Chocolate", 3) → "Choate"
	# eight("Chocolate", 1) → "Choclate"

	# <HINT>
    # Use the cli to access the documentation help(str.replace)

def eight(input,  a):
	string = []
	back2 = []
	stringy = list(input)
	count = len(input) - a
	print(count)
	print(stringy)
	front = ""
	back = ""
	for i in range(0,len(input)):
		if ( count > 0):

			front = front + str(stringy[i])
			back = back + str(stringy[len(stringy) - i -1])
			count = count - 2
		else:
			flip = ""
			back2 = list(back)
			for j in range(0, len(back)):
				flip = flip + back2[len(back2) - j -1]
			return(front + flip)
      
	

	# <QUESTION 9>

    # Given two string inputs, if one can be made from the other return the boolean True, if not return the boolean False.

	# <EXAMPLES>

    # nine("god", "dog") → True
    # nine("tree", "tiredest") → True
    # nine("cat", "dog") → False
    # nine("tripping", "gin") → True

	# <HINT> 
	# There are no hints for this question.

def nine(string1, string2):
	alist = list(string1)
	blist = list(string2)
	alen = len(string1)
	blen = len(string2)
	counter = 0
	if ( alen <= blen):
		for i in range(0, alen):
			for j in range(0, blen):
				if alist[i] == blist[j]:
					counter = counter +1
					alist[i] = 789
					blist[j] = 8967
		if (counter == alen):
			return True
		else:
			return False

	elif ( alen > blen):
		for i in range(0, blen):
			for j in range(0, alen):
				if blist[i] == alist[j]:
					counter = counter +1
					blist[i] = 789
					alist[j] = 8967
		if (counter == blen):
			return True
		else:
			return False


	# <QUESTION 10>

    # Write a function which takes 2 integers greater than 0, X,Y as input and generates a 2-dimensional array. 
	
	# The element value in the i-th row and j-th column of the array should be i*j.

	# <EXAMPLES>

	# ten(3,2) → [[0,0,0],[0,1,2]]
	# ten(2,1) → [[0,0]]
	# ten(3,4) → [[0,0,0],[0,1,2],[0,2,4],[0,3,6]]

	# <HINT>
	# Think about nesting for loops.

def ten(X,Y):
	listy = []
	listy2 = []
	for i in range(0, Y):
		for j in range(0,X):
			listy2.append(i*j)
		listy.append(listy2)
		listy2 =[]

	return listy
