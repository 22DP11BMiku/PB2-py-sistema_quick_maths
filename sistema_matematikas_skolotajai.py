def atpakal():
    atpakal = input("Vai vēlaties atgriezties uz izvēlni: ")
    print()
    if atpakal == "ja" or atpakal == "jā" or atpakal == "Jā" or atpakal == "Ja":
        lietotajs_izvelas(int(input("Ko vēlaties darīt? \n1. Teorija\n2. Patstāvīgais darbs \n3. Pārbaudes darbs\nJūsu izvēle: ")))
        print()


def teorija_par_temu():
    teorijas_mainigais = open("fails_ar_teoriju.txt", "r", encoding="utf8")
    teorija = teorijas_mainigais.read()
    print(teorija)
    teorijas_mainigais.close()
    atpakal()


def izrekina_atzimi(skaits):
    atzime = round(punkti / skaits * 10)
    if atzime == 0:  # atzīme 0 nevar būt
        atzime = 1
    print(f"Punktu skaits: {punkti}/{skaits}")
    print(f"Atzīme: {atzime}")
    print("\n\n\n\n")


def ievada_jautajumus(skaits):  # izveidoju funkciju skolotajs_tests()
    global punkti, skol_atb, skol_jaut
    print("Tēma : Lineārie vienādojumi")
    skol_jaut = [""] * skaits
    skol_atb = [""] * skaits
    for x in range(skaits):
        skol_jaut[x] = input("Ievadiet jautājumu: ")
        skol_atb[x] = input("Ievadiet pareizo atbildi: ")
    punkti = 0


def default_jautajumi():
    global punkti
    punkti = 0
    masivs_ar_jaut = [["Aprēķini lineāra vienādojuma sakni!\nAtbildi ievadi kā veselu skaitli!\n10g+10=−10", -2],
    ["Nosaki lineāra vienādojuma atrisinājumu!\nJa atbilde nav vesels skaitlis, raksti kā decimāldaļu!\n−2g+7=−13", 10],
    ["Atrodi lineāra vienādojuma sakni!\n0.2g+13=−3", -80],
    ["Atrisini lineāru vienādojumu!\nAtbilde ir vesels skaitlis!,\n(7/8)*x=49", 56]]
    for x in range(4):
        print(f"\n{x+1}.uzdevums\n{masivs_ar_jaut[x][0]}")
        atbilde = int(input("Ievadiet atbildi: g = "))
        if atbilde == masivs_ar_jaut[x][1]:
            print("\nPareizi!\n")
            punkti += 1
        else:
            print(f"\nNepareizi!\nPareizā atbilde: {masivs_ar_jaut[x][1]}\n")
    izrekina_atzimi(4)
    atpakal()


def patstaviga_darba_uzdevumi():
    global uzd_skaits
    izvele_uzd = int(input("\nKā jūs vēlaties aizpildīt patstāvīgā darba uzdevumus:\n1. Ievadīt patstāvīgi\n2. Aizpildīt ar default vērtībām\nJūsu izvēle: "))
    if izvele_uzd == 1:
        uzd_skaits = int(input("\nIevadiet uzdevumu skaitu: "))
        print()
        ievada_jautajumus(uzd_skaits)  # ievada patstāvīgi
        jautajums = input("Vai esiet gatavi pildīt uzdevumus: ")
        print()
        if jautajums == "ja" or jautajums == "jā" or jautajums == "Jā" or jautajums == "Ja":
            atbild_uz_jautajumiem(uzd_skaits)
    elif izvele_uzd == 2:  # uzdevumi default
        default_jautajumi()
    else:  # kļūda, vēlreiz
        print("\nKļūda! Ievadiet vēlreiz.\n")
        patstaviga_darba_uzdevumi()


def parbaudes_darbs():
    global punkti
    punkti = 0
    parbaudes_darba_masivs = [["Nosaki lineāra vienādojuma atrisinājumu!\nJa atbilde nav vesels skaitlis, raksti kā decimāldaļu!\n−2a+9=−13", 11],
    ["Vienādojuma (1/3)*x=12 sakne ir",36 ],
    ["Atrisini lineāru vienādojumu!\nAtbilde ir vesels skaitlis!\n−(7/8)*m=−35", 40],
    ["Vienādojumā kx=−72+k ievieto k vietā tādu skaitli, lai izveidotos vienādojums, kura sakne ir 10.\nZināms, ka k ir vesels skaitlis.\nk vērtība ir", -8]]
    for x in range(4):
        print(f"\n{x+1}.uzdevums\n{parbaudes_darba_masivs[x][0]}")
        atbilde = int(input("Ievadiet atbildi(tikai skaitli):  "))
        if atbilde == parbaudes_darba_masivs[x][1]:
            punkti += 1
    print()
    izrekina_atzimi(4)
    atpakal()


def atbild_uz_jautajumiem(skaits):
    global punkti
    for x in range(skaits):
        # ar cikla for palīdzību izvadu jautājumus pēc kārtas
        print(f"{x+1})", skol_jaut[x])
        audz_atb = input("Atbilde: ")
        if audz_atb == skol_atb[x]:
            punkti += 1
            print(uzd_skaits)
            izrekina_atzimi(uzd_skaits)
            atpakal()


def lietotajs_izvelas(izvele):
    if izvele == 1:
        teorija_par_temu()
    elif izvele == 2:
        patstaviga_darba_uzdevumi()
    elif izvele == 3:
        parbaudes_darbs()
    else:
        print("\nKļūda! Ievadiet vēlreiz.\n")
        lietotajs_izvelas(int(input("Ko vēlaties darīt? \n1. Teorija\n2. Patstāvīgais darbs \n3. Pārbaudes darbs\nJūsu izvēle: ")))


lietotajs_izvelas(int(input("Ko vēlaties darīt? \n1. Teorija\n2. Patstāvīgais darbs \n3. Pārbaudes darbs\nJūsu izvēle: ")))
