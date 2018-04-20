## 1.1 Implement an algorithm to determine if a string has all unique characters
def unuiqueChar(str):
	dict = {}
	for i in range(len(str)-1):
		if str[i] in dict:
			return False
		dict[str[i]] = i
	return True

O(n)
O(n)
## 1.2 Reverse a string
def reverse(str):
	return str[::-1]

## 1.3 Given string *a* and string *b*, write an algorithm to decide if *a* is a permutation of *b*.
def isPermutation(a, b):
	if len(a) != len(b):
		return False
	dict = {}
	for i in range(len(a)):
		if a[i] not in dict:
			dict[a[i]] = 1
		else:
			dict[a[i]] += 1
	for i in range(len(b)):
		if b[i] not in dict or dict[b[i]] < 0:
			return False
		else:
			dict[b[i]] -= 1
	return True

## 1.4 Check if a string is palindrome
def Palindrome(str):
	left = 0
	right = len(str)-1
	
	while left < right:
		if str[left] != str[right]:
			return False
		else:
			left += 1
			right -= 1
	return True

def Parlin2(str):
	return str == str[::-1]


## 1.4.1 Check if a string is palindromable
O(n)
def isPalin(str):
	s = set()
	for i in str:
		if i in s:
			s.remove(i)
		else:
			s.add(i)

	if len(s)>1:
		return False
	else:
		return True






















