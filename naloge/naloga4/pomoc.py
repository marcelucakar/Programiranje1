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

a = []
a.append('a')
a.append('b')
print(len(a))

def preberi_datoteko(ime_dat):
    v = []
    for vrstica in open(ime_dat):
        #st_elementov = vrstica.count(",") + 1  -- ce potrebujemo slucajno kdaj naslednjic st. elementov ki jih ima posamezna vrstica v datoteki
        v.append(vrstica.split(","))
    return v

def filtriran(s, stolpec, vrednost):
    tmp = []    #isto kot "v" pri prejsni funkciji, sam se mi zdi bolj kul uporabit tmp
    for vrstica in s:
        if vrstica[stolpec] == vrednost:
            tmp.append(vrstica)
    return tmp

def izlusci(s, vrednost):
    tmp = []
    for vrstica in s:
        tmp.append(vrstica[vrednost])
    return tmp

neki = preberi_datoteko("kolesa.txt")
print("neki:\n", neki)

print("\n"*3)

tmp = []
tmp = filtriran(preberi_datoteko("zapisnik.txt"), 1, "Ana")
#tmp = izlusci(tmp, "Ana")
koncni_tmp = []
for vrstica in tmp:
    koncni_tmp.append(vrstica[0])
print("tmp:\n",koncni_tmp)