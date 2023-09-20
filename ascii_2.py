
MyPlainText = "ABCDE"
XOR_KEY =     "PASSW"
#Comment two strings of the same length right now

Encrypted_Values = []
#Create an empty Python List

for Position, PlainTextCharacter in enumerate(MyPlainText):
	print(Position, PlainTextCharacter)
	print(Position, XOR_KEY[Position])
	print("Xoring the two above values together and saving the result to a list!")
	encrypted_byte = ord(PlainTextCharacter) ^ ord(XOR_KEY[Position])
	#The first time through the loop this translates to:
	#encrypted_byte = Plain text at position 1 ^ XOR_KEY at Position 1

	Encrypted_Values.append(encrypted_byte)
	#The first time through the loop Encrypted_Values will contain the following
	#Encrypted_Values[RESULT1]
	#The second time through the loop Encrypted_Values will contain the following
	#Encrypted_Values[Result1,Result2]
print("The encrypted Decimal Values when XORing the each of these letters together is:")
print(Encrypted_Values)
#This will print the result of each XOR operation in decimal

#Loop through our encrypted values and print the Hex equivalent on one line.
print("Here are the Hex values:")
for i in Encrypted_Values:
	print(hex(i)+" ", end='')
#Because of the end ='' argument, we need a blank print statement to create a line break
print()

#Loop through the encrypted values and use format() to eliminate the 0x at the beginning of each
print("Here are the hex values with a space between them instead of 0x")
for i in Encrypted_Values:
	print(format(i, 'x')+" ", end='')
