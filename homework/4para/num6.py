cena = int(input())
while cena != 0:
    if cena % 2 == 0:
        while cena % 2 == 0:
            cena /= 2
    else:
        price = round(cena * 0.85, 2)
    print(f"К оплате: {cena}")
    price = int(input())