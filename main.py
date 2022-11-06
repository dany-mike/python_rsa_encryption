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
    
p = 11
q = 3
n = p * q
phi = (p-1)*(q-1)
exclude_e = []

generate_exclude_e(exclude_e, phi)

print(exclude_e)

e = give_e_value(exclude_e, phi)

print("p: " + str(p) + " q: " + str(q))
print("n: " + str(n))
print("phi: " + str(phi))
print("e: " + str(e))
