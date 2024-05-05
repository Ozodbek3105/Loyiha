import random

users = {
    "ozod": {"password": "123", "point": 0},
    "begzod": {"password": "321", "point": 10},
    "anvar": {"password": "321", "point": 5}
}

sozlar = {"tiger": "yolbars", "lion": "sher", "cat": "mushuk", "dog": "it", "goat": "echki", "car": "moshina",
          "pencil": "ruchka", "pen": "qalam"}


def my_sort(value):
    return users[value]["point"]


def show_result():
    global users
    print("\nNATIJALAR\n")
    ismlar = sorted(users.keys(), key=my_sort, reverse=True)

    for ism in ismlar:
        print(ism, "  ", users[ism]["point"])


def register():
    global users
    while True:
        login_kirit = input("login kiriting iltimos:")
        if login_kirit not in users.keys():
            break
        else:
            print("bu login bazada bor. boshqa login kiriting:")
    while True:
        parol = input("parol kiriting:")
        if len(parol) >= 4:
            break
        else:
            print("parol uzunligi 3 dan katta bolsin")
    users.update({login_kirit: {"password": parol, "point": 0}})
    sub_menu(login_kirit)


def login():
    ism = input("kirish uchun loginni kiriting:")
    paroli = input("kirish uchun parolni kiriting:")
    for kalit, qiymat in users.items():
        if kalit == ism and qiymat["password"] == paroli:
            sub_menu(ism)
            break
    else:
        print("login yoki parol xato")


def play(login):
    global sozlar, users
    t = users[login]
    urunishlar = 5
    while True:
        urunishlar -= 1
        inglizcha = random.choice(list(sozlar.keys()))
        # uzbekcha=random.choice(list(sozlar.values()))
        sozni_top = input(f"{inglizcha} bu uzbekchada nima deyiladi:")
        if sozlar[inglizcha] == sozni_top:
            t["point"] += 10
            print("\n Togri", urunishlar)
        else:

            print("\nXATO !!! ", urunishlar)

        if urunishlar == 0:
            break


def sub_menu(login):
    while True:
        try:
            b = int(input(
                f"\n{login}, oyinga hush kelibsiz\nbittasini tallang:\n\t1. oyinni boshlash\n\t2. natijalarni korish\n\t3. chiqish\n"))
            if int(b) not in range(1, 4):
                raise ValueError
        except ValueError:
            print("oraliqdagi sonni kiriting !!!")
            continue
        if b == 1:
            play(login)
        elif b == 2:
            show_result()
        else:
            break


def menu(habar, royxat):
    while True:
        a = None
        try:
            a = int(input(f"{habar}"))
            if int(a) not in royxat:
                raise ValueError
            else:
                return int(a)
        except ValueError:
            print("faqat royxatdagi xabarni kiriting")


while True:

    habar = """________ Learn English words ________ 
		1. O'yin natijalari
		2. Ro'yxatdan o'tish
		3. Kirish
		4. Chiqish\n"""
    tanlov = menu(habar, range(1, 5))

    if tanlov == 1:
        show_result()
    elif tanlov == 2:
        register()
    elif tanlov == 3:
        login()
    else:
        break

v = {"ozod": {"password": "123", "point": 0}}
print(v["ozod"]["point"])

