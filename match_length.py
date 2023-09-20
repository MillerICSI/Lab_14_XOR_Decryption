OriginalText = "MyPlainText"
KEY = "ABC"

print ("Here is the original Text")
print(OriginalText)

print("here is the Key repeated up to the length of the original text")
for position, letter in enumerate(OriginalText):
	x = KEY[position % len(KEY)]
	print(x,end='')

print()
#Everything above this just shows that the key and plaintext are the same length

Encrypted_Values = []

for position, letter in enumerate(OriginalText):
	Letter_In_Key = KEY[position % len(KEY)]
	encrypted_byte = ord(letter) ^ ord(Letter_In_Key)
	Encrypted_Values.append(encrypted_byte)

print ("Here is the encrypted Decimal")
print (Encrypted_Values)

print("Here is the encrypted Hex with the 0x preceding each value")
for i in Encrypted_Values:
	print(hex(i)+" ", end="")
print ()
#Line break for neatness
print("Here is the encrypted Hex without the 0x preceding each value")
for i in Encrypted_Values:
	print(format(i, "x")+" ", end="")
