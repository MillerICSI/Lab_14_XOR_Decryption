
EncryptedHex = ['0xc', '0x3b', '0x13', '0x2d', '0x23', '0x2a', '0x2f', '0x16', '0x26', '0x39', '0x36']

KEY = "ABC"

Encrypted_Decimal_Values = []

for i in EncryptedHex:
	Encrypted_Decimal_Values.append(int(i,16))
print(Encrypted_Decimal_Values)

decrypted_values = []

for position, value in enumerate(Encrypted_Decimal_Values):
    decrypted_value = value ^ ord(KEY[position % len(KEY)])
    decrypted_values.append(decrypted_value)

print(decrypted_values)

print()

for i in decrypted_values:
	print(chr(i), end="")
