ciphertext = "2c11130b59130b591b582a1f1b0b1f0c59371d0a09191e1f"
ciphertext_bytes = bytes.fromhex(ciphertext)

# Open the file for reading
with open("wordlist.txt", "r") as file:
    # Read each line from the file and print it
    for line in file:     
    # Use strip() to remove extra whitespace and newline characters
        key = line.strip().encode()
        decrypted = bytearray()

        for i in range(len(ciphertext_bytes)):
            decrypted.append(ciphertext_bytes[i] ^ key[i % len(key)])

        # For each character in the cipher, Xor the corresponding character from the line in the wordlist.
        if all(32 <= byte <= 126 for byte in decrypted):
            print("Trying: " + line)
            print("Decrypted (ASCII):", decrypted.decode())
