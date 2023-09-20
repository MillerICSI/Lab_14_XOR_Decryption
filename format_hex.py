hex_string = '2c11130b59130b591b582a1f1b0b1f0c59371d0a09191e1f'
formatted_hex = ['0x' + hex_string[i:i+2] for i in range(0, len(hex_string), 2)]
print(formatted_hex)

