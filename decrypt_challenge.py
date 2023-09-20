ciphertext = "37001e00070f001a1c0601071b01035d55371b1a500f1418114f03081918110b50131d0b54091909140254373f35552d1c0e1c0b1000130a51473a00541b1f47170713081515550f1a0b5005101a000a024701061d01171454"
ciphertext_bytes = bytes.fromhex(ciphertext)

# Open the file for reading
with open("challenge_wordlist.txt", "r") as file:
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
