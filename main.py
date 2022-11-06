import random


def generate_exclude_e(exclude_e, phi):
    for i in range(2, phi):
        if (phi % i == 0):
            exclude_e.append(i)


def give_e_value(exclude_e, phi):
    while True:
        e = random.randrange(2, phi)
        if e not in exclude_e:
            break
    return e

def give_d_value(phi):
    return random.randrange(2, phi)


def print_public_key(e, n):
    print("Public key: (e=" + str(e) + ", n=" + str(n) + ")")

def print_private_key(d, n):
    print("Private key: (d=" + str(d) + ", n=" + str(n) + ")")

p = 11
q = 3
n = p * q
phi = (p-1)*(q-1)
exclude_e = []

generate_exclude_e(exclude_e, phi)

while True:
    e = give_e_value(exclude_e, phi)
    d = give_d_value(phi)
    if (e * d) - phi == 1:
        break

print_public_key(e, n)
print_private_key(d, n)
print("p: " + str(p) + " q: " + str(q))
print("n: " + str(n))
print("phi: " + str(phi))
print("e: " + str(e))
print("d: ", d)
