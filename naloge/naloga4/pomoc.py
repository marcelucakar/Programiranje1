def unikati(s):
    s2 = []
    for ime in s:
        if ime not in s2:
            s2.append(ime)
    return s2

def skupnih(s, t):
    skupnih = 0
    s = unikati(s)
    t = unikati(t)
    
    for element in s:
        for e in t:
            if element == e:
                skupnih += 1
    return skupnih

def vseh(s, t):
    i = 0
    skupek = []
    skupek = s + t
    skupek = unikati(skupek)
    print(len(skupek), skupek)
    return len(skupek)

vseh(["Ana", "Berta", "Ana", "Ana", "Cilka"], ["Cilka", "Dani", "Ana", "Ana"])

#unikati(["Ana", "Ana", "Berta", "Cilka", "Ana", "Berta", "Berta", "Berta", "Ema", "Dani", "Cilka"])