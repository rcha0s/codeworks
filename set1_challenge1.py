'''
Problem
Convert hex to base64
The string:
49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d

Should produce:

SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
So go ahead and make that happen. You'll need to use this code for the rest of the exercises.

Cryptopals Rule
Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing.
'''


'''
Solution I - using encode/decode
1. Convert hex to ascii(bytes)
2. Convert ascii(bytes) to base64
'''
import base64
#hex_input = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
hex_input = raw_input("Enter hex number:")
ascii_value = hex_input.decode('hex')
result = base64.b64encode(ascii_value)
#if result == "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t":
print "Solution 1 with encode/decode \nAscii/byte value is: %s" % ascii_value
print "Desired output is:", result

'''
Solution II - Using binascii from same conversion
1. unhexlify - hex to bytes
2. b2a_base64 - bytes to base64
'''
print ''
from binascii import unhexlify, b2a_base64
ascii_value2 = unhexlify(hex_input)
result2 = b2a_base64(ascii_value2).split()[0] #b2a_base64 adds new line in the end

#if result2 == "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t":
print "Solution 2 with binascii.unhexlify/b2abase64 \nAscii/byte value is: %s" % ascii_value2
print "Desired output is:", result2
