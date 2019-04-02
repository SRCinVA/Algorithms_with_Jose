#=================
#PIG LATIN

def pig_latin(word):
    first_letter = word[0]
    # check if vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
    #place the first letter in a variable instead of shuffling around indexes!
    return pig_word
    
pig_latin("apple") 


#===================
#LESSER OF TWO EVENS: 
# Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd


def lesser_of_two_evens(num1, num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        return min(num1, num2)
    else:
        return max(num1, num2)

lesser_of_two_evens(2, 5)

#===============
#ANIMAL CRACKERS: 
#Write a function takes a two-word string and returns True if both words begin with same letter:

def animal_crackers(two_word_string):
    x = two_word_string.lower().split()
    # to ensure they're all lower case.
    if x[0][0] == x[1][0]:
        return True
animal_crackers('Big Bird')

#============
#MAKES TWENTY: 
#Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False.

def makes_twenty(int1, int2):
    if (int1 + int2) == 20 or int1 == 20 or int2 == 20:
        return True
    else:
        return False

    #even shorter:
	return (n1+n2) == 20 or n1 == 20 or n2 == 20
	# if they all fail, it will return False

makes_twenty(18, 2)

#========
#SKYLINE: 
#Function takes in a string, turns every second into an upper case and other into a lower case.

def myfunc(x):
    z = []
    # Note the list comprehension and casting i as a string.
    y = [str(i) for i in x]
    for i in range(0, len(y)):
        if i % 2 == 0:
            y[i] = y[i].lower()
            z += y[i]
        else:
            y[i] = y[i].upper()
            z += y[i]
        b = ''.join(z)  # joins each element of z into a string
    print(b)  # the string
    print(z)  # the list

myfunc('whatever')


#=============
#OLD MACDONALD
#Write a function that capitalizes the first and fourth letter of a string.

def myfunc(x):
    z = []
    y = [str(i) for i in x]
    for i in range(0, len(y)):
        if i == 0:
            y[i] = y[i].upper()
            z += y[i]
        if i == 3:
            y[i] = y[i].upper()
            z += y[i]
        b = ''.join(z)
    return(b)

myfunc('macdonald')

#Method 2:
def myfunc(x):
    first_letter = x[0]
    inbetween = x[1:3]
    fourth_letter = name[3]
    rest = x[4:]
    return first_letter.upper() + inbetween + fourth_letter.upper() + rest

#Method 3:
def myfunc(x):
    first_half = x[:3]
    second_half = x[3:]
    return first_half.capitalize() + second_half.capitalize()
    # .capitalize hits on the first specified element

#===========
#MASTER YODA
#Take in a string and return it with the words reversed:

def myfunc(a):
    b = a.split()
    c = ''
    for i in range(len(b) - 1, -1, -1):
		# start at len(b) -1 (b/c index 0);
		# stop at -1 (b/c have to go 1 beyond);
		# step -1 to traverse backward
        word = ''.join(b[i])
        c += word + ' '
    return c
    print(c)

myfunc('we are ready')

#Method 2
def master_yoda(a):
    wordlist = a.split()
    reverse_wordlist = wordlist[::-1]
    return ' '.join(reverse_wordlist)

#=============
#ALMOST THERE: 
#Given an integer n, return True if n is within 10 of either 100 or 200

def myfunc(a):

    if a in range(90, 110):
        return True
    elif a in range(190, 210):
        return True
    else:
        return False

myfunc(209)

#Method 2:
def almost_there(n):

	return (abs(100-n) <= 10) or (abs(200-n) <= 10)

#========
#FIND 33: 
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def myfunc(arr):

    i = 0
    for i in range(len(arr)):
        if arr[i] != 3:
            continue
        elif arr[i] == 3:
            for j in range(i+1, len(arr)):
                if arr[j] != 3:
                    break
                elif arr[j] == 3:
                    return True
    else:
        return False

#Method 2:
def has_33(nums):
	for i in range(0,len(nums)-1):
		if nums[i] == 3 and nums[i+1] == 3:
			return True
	return False

has_33([1,3,5,2,3,3]) 
# you need the -1 if the last one turns out
# to be a 3. From there, the +1 forces the
# error. If the last is not a 3, then the
# issue does not arise.

#Method 3: grabs slices at a time and compares them to 33.

def has_33(nums):

	for i in range(0,len(nums)-1):
		if nums[i:i+2] == [3,3]: 
		# it's i+2 because you have to go one beyond the next 
		# '3'. Also, you are creating a “slice' of two items,
		# with no space between them.			                 
			return True
	return False
has_33([1,3,5,2,3,3])

#=================
#PAPER DOLL: 
#Given a string, return a string where for every character in the original there are three characters

def myfunc(str):
    a = list(str)
    i = 0
    multi = []
    
    for i in range(0,len(a)):
        multi += a[i]
        multi += a[i]
        multi += a[i]  
myfunc('Mississippi')

#Method 2
def paper_doll(string):
	result = ''

	for char in string:
		result += char*3
	return result

=================
BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

def myfunc(int1,int2,int3):

    sum1 = int1 + int2 + int3    
    
    if int1 + int2 + int3 <= 21:
        return sum1
        
    elif int1 == 11 or int2 == 11 or int3 == 11 and sum1 > 21:
        sum2 = sum1 - 10
        return sum2
        
    elif sum1 > 21 or sum2 > 21:
        return 'BUST'
    
myfunc(9,9,11)


   Method #2:

	def blackjack(a,b,c):
		if sum ([a,b,c]) <= 21: #notice the 'sum' keyword
			return sum([a,b,c])
		elif 11 in [a,b,c] and sum([a,b,c]) - 10 <= 21:
		    #you could make it 31, for the 10 you subtract
			return sum([a,b,c]) - 10     
		else: #this is all that's left to happen
			return "BUST”
		
	
===============
SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.

def myfunc(arr):

    sum1 = 0

    for i in range(0,len(arr)):
        sum1 += arr[i]

    sum2 = 0
    
    for i in range(0, len(arr)):
        if arr[i] == 6:
            sum2 += arr[i]
            for i in range(i, len(arr)): 
                if arr[i] != 6:
                    sum2 += arr[i]
                    if arr[i] == 9:
                        break
    
    print(sum1)
    print(sum2)
    result = sum1 - sum2
    return 
    
myfunc([2,1,6,9,11])

  #Method 2: #tested: this does work. The True boolean is a tough concept to work through.

	total = 0
	add = True   # you can think of “add” as built into the for loop.  This provides a very 		         # useful way of manipulating the while loop inside the for loop 
	for num in arr:
		while add:
			if num != 6:
				total += num
				break
#the "break" above pulls you out of the while loop to restart it each time. I think you can do this #because "add" has been established as True. This is clever, because it provides a check on #every number.
			else:
				add = False
# if it's False like above, then the while not add loop below executes:		
		
		while not add:
			if num != 9:
                break

# Above, you are checking each number (but not adding them) each time, with the for loop on the outside propelling things along.

			else:
				add = True
				break

# above (implicitly) if the number is 9, you "turn on" the add again and resume

	return total
		
# when the outer for loop is out of gas, return the total, per the requirement.

# the break statements are only connected to the while loops they are in. 
   

SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order

Note: the commented out section would require direct contiguity between the characters, but that wasn't the requirement.

def spy_game(arr):

    arr2 = []
    
    #for i in range(0, len(arr)):
    #    if arr[i] == 0:
    #        arr2.append(arr[i])
    #        for i in range(i, len(arr)):
    #            if arr[0] != 0:
    #                return False
    
    #for i in range(0, len(arr)):
    #    if arr[i] == 0:
    #        arr2.append(arr[i])
    #        for i in range(i, len(arr)):
    #            if arr[0] != 7:
    #                return False
    
    for i in range(0, len(arr)):
        if arr[i] == 0:
            arr2.append(arr[i])
            
        if arr[i] == 7:
            arr2.append(arr[i])
            
    print(arr2)        
            
    if arr2 == ([0,0,7]):
        return True
    else:
        return False
        
spy_game([1,7,2,0,4,5,0])

   #Method 2:
	
   def spy_game(*nums):
 
	code = [0,0,7,'x']

	for num in nums:
		if num == code[0]:
			code.pop(0)
			
	return len(code) == 1

	# in other words, you are popping off index [0] each time and checking each popped 	# item against code. When you've exhausted it down to one item(i.e., "len(code) == 1"), 	# it will return boolean True as a default if everything previous checked out; 'x' is that 
	# placeholder indicating that everything else was in code was evacuated.

================
COUNTING PRIMES: 
Couldn't do this one, but here's the answer:

def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes


   #Method 2:

	def count_primes(num):
		
	#check for 0 or 1 input
		if num < 2:
			return 0
	
	##################
		#2 or greater
	##################
		primes = [2]
	# Counter going up to input num
		x = 3
	# x is going through every int up to num
		while x <= num:
			for y in range(3,x,2)
				if x%y == 0:
					x += 2
					break

	# note you started on 3. This is good, because you can just add 2 and then 
           # automatically focus on the odds all the way up (evens can't be primes).
           # Also realize you are testing an odd Y against an odd X, courtesy of the embedded
	# for loop.

	# use a for/else statement, shown below:

			else:
				primes.append(x)
				x += 2

	# If you went through the for loop and never broke, then the else statement would   	   execute. 

	   print(primes)
	   return len(primes)

	# directly above, you are modulus testing each 'x' (which is standing in for num) 	
	# against a 'y' option. Computationally, it must be hugely expensive, but it will 	
	# probably work.
