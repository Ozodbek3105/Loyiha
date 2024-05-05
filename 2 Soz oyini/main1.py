import random

soz = random.choice(["qalam", "olma", "banana", "telefon"])
d = 0
topilgan_harf = ""
topilmagan_harf = ""
print("\n------SOZ TOPISH OYINIGA HUSH KALIBSIZ------\n")
for i in soz:
    print("▮", end='')

if soz == "telefon":
    print("\nodam uchun kerakli apparat ?!")
elif soz == "qalam":
    print("\nrasm chizishda ishlatiladigan buyum ?!\n")
elif soz == "olma" or soz == "banana":
    print("\nmeva turi\n")

while True:

    harf = input("sozni topish uchun qandaydir harf kiriting : ").lower()

    if harf in topilgan_harf or harf in topilmagan_harf:
        print(f"\nsiz bu {harf} harfni kiritgansiz")
    elif harf in soz:
        topilgan_harf += harf
        print("\n", harf, "soz ichida bor")

    else:
        d += 1
        topilmagan_harf += harf
        print(f"\nbu sozda {harf} yoq urunishlar soni {7 - d} ta qoldi")

        if d == 7:
            print("\nurunishlar soni tugadi siz yutqazdingiz")
            break
    topilgan_soz = ""
    for i in soz:
        if i in topilgan_harf:
            topilgan_soz += i
        else:
            topilgan_soz += "▮"
    print(topilgan_soz)
    if "▮" not in topilgan_soz:
        print(f"\n siz yutdingiz")
        break
