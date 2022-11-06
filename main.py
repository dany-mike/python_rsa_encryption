def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


def find_e(e_list, phi):
    for i in range(1, phi):
        if is_prime(i) and (phi % i) != 0:
            e_list.append(i)
    return e_list


def find_d(phi, e):
    for i in range(2, phi):
        if (i * e) % phi == 1:
            return i
    return None


def print_public_key(e, n):
    print("Public key: (e=" + str(e) + ", n=" + str(n) + ")")


def print_private_key(d, n):
    print("Private key: (d=" + str(d) + ", n=" + str(n) + ")")


def cipher(msg, n):
    cipher_msg = []
    for m in msg:
        cipher_msg.append((m ** e) % n)
    return cipher_msg


def decipher(cipher_msg, d):
    decipher_msg = []
    for cm in cipher_msg:
        decipher_msg.append((cm ** d) % n)
    return decipher_msg


def char_to_ASCII(char):
    return ord(char)


def convert_char_msg_to_ASCII_msg(char_msg):
    ascii_msg = []
    for c in char_msg:
        ascii_msg.append(char_to_ASCII(c))
    return ascii_msg


def convert_ASCII_msg_to_char_msg(char_msg):
    ascii_msg = []
    for c in char_msg:
        ascii_msg.append(chr(c))
    return ascii_msg

p = 17
q = 23
n = p * q
phi = (p-1)*(q-1)
e_list = find_e([], phi)
e = e_list[0]

d = find_d(phi, e)

msg = "331 304 077 315 045 304 228 040 315 356"
msgList = msg.split(" ")

msgList = [int(m) for m in msgList]

decMsg = convert_ASCII_msg_to_char_msg(decipher(msgList, d))
finalMsg = "".join(decMsg)

print_public_key(e, n)
print_private_key(d, n)
print("p: " + str(p) + " q: " + str(q))
print("n: " + str(n))
print("phi: " + str(phi))
print("e: " + str(e))
print("d: ", d)
print("decipher: ", str(decMsg))
print(finalMsg)
print(cipher(convert_char_msg_to_ASCII_msg(decMsg), n))
