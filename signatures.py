m = 88
m_real = 88
p = 61
q = 21
n = p * q
e = 13
d = 37
checker = bool()

s = (m ** d) % n
print(s)
if ((s ** e) % n) == m_real:
    checker = True

if checker:
    print("Die Signatur gehört zur jeweiligen Person(valid)")
else:
    print("Diese Signatur gehört nicht zu jeweiligen Person(invalid)")



