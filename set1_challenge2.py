'''
Problem:

Fixed XOR
Write a function that takes two equal-length buffers and produces their XOR combination.

If your function works properly, then when you feed it the string:

1c0111001f010100061a024b53535009181c
... after hex decoding, and when XOR'd against:

686974207468652062756c6c277320657965
... should produce:

746865206b696420646f6e277420706c6179

'''

'''
Note:
bool(a) ^ bool(b)
The xor operator on two booleans is logical xor (unlike on ints, where it's bitwise)
'''

'''
Solution I:
XOR operation works on two numbers and it is a bitwise operation. So,
1. Convert hex to int
2. XOR the numbers
3. Return back to hex
'''

#input1 = raw_input("Enter buffer1 in hex:")
#input2 = raw_input("Enter buffer2 in hex:")
#if len(input1) != len(input2):
#	print "Enter equal length buffers"
#	exit(0)
input1 = '1c0111001f010100061a024b53535009181c'
input2 = '686974207468652062756c6c277320657965'
result = int(input1,16)^int(input2,16)
print "XOR output in int is:",result
#print hex(result) - Results in an output as 0x----numbers----L. Using format to remove the extra chars
#Also, string format is different from format built-in function
print "Solution 1 result is: %s" % format(result, '02x')


'''
Solution II:
1. Convert hex string to ascii
2. Convert individual ascii chars to integers
3. XOR them
4. Convert them all back to ascii chars while appending them
5. Convert them back to hex string
'''

asc1 = input1.decode("hex")
asc2 = input2.decode("hex")

#print len(asc1)
#print len(asc2)
final = ""
charlist = []
'''
for i in asc1:
	for j in asc2:
		if asc2.index(j) == asc1.index(i):
			print asc2.index(j), asc1.index(i)
			charlist.append(chr(ord(i)^ord(j)))
'''
# Failed because character positions are not unique! They can be repeated
for i,j in zip(asc1,asc2):
		#print asc2.index(j), asc1.index(i)
		charlist.append(chr(ord(i)^ord(j)))

#print charlist
print "The output string is:", final.join(charlist)
print "Solution 2 result is: %s" % final.join(charlist).encode("hex")
# OR just replace with one line
# print "".join([chr(ord(i)^ord(j)) for i,j in zip(asc1,asc2)])



