def unikati(s):
    s2 = []
    for ime in s:
        if ime not in s2:
            s2.append(ime)
    print(s2)
    return s2

unikati(["Ana", "Ana", "Berta", "Cilka", "Ana", "Berta", "Berta", "Berta", "Ema", "Dani", "Cilka"])