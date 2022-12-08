import array as arr
a = arr.array('L', [])

for i in range(20000000):
    a.append(0)

def m_func(i):
    if a[i] == 0:
        if i == 0: return 1
        if i == 1: return 2
        if i == 2: return 3
        if i == 3: return 4
        a[i] = (55692*m_func(i-4) - 9549*m_func(i-3) + 301*m_func(i-2) + 21*m_func(i-1)) % (10**10000)
    
    return a[i]

for i in range(30):
    print(m_func(i))