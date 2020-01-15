def encode_str(data):
    buf = bytearray()
    for char in data:
        num = ord(char)

        # Lower case latin letters
        if 97 <= num <= 122:
            buf.append(num - 96)

        # Space
        elif num == 32:
            buf.append(27)

        else:
            raise Exception("Too many bits")

    return buf


def decode_str(data):
    result = ""
    for num in data:
        if num == 27:
            result += " "
        else:
            result += chr(num + 96)
    return result

