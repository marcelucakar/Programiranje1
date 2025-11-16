st_krajev = 0
prejsni_kraj = ""
for beri in open("vremenske-postaje.txt"):
    kraj, datum, velika, mala = beri.split(",")

    if prejsni_kraj != kraj:
        st_krajev += 1
        prejsni_kraj = kraj
print(f"St. krajev: {st_krajev}")