import json
import os
from datetime import date, datetime

dosya_adi = "maclar.json"


def verileri_yukle():
    # dosya yoksa boş liste döndür
    if not os.path.exists(dosya_adi):
        return []
    with open(dosya_adi, "r", encoding="utf-8") as f:
        return json.load(f)


def verileri_kaydet(maclar):
    with open(dosya_adi, "w", encoding="utf-8") as f:
        json.dump(maclar, f, indent=2, ensure_ascii=False)


def sayi_sor(soru):
    # sayı girene kadar tekrar sorar
    while True:
        try:
            sayi = int(input(soru))
            if sayi < 0:
                print("Negatif sayı girme, eksiyi ben ekliyorum.")
                continue
            return sayi
        except ValueError:
            print("Geçerli bir sayı gir!")


def istatistik_yazdir(baslik, maclar):
    print("\n--- " + baslik + " ---")

    if len(maclar) == 0:
        print("Hiç maç yok.")
        return

    kazanilan = 0
    kaybedilen = 0
    net_rr = 0

    for mac in maclar:
        if mac["sonuc"] == "K":
            kazanilan += 1
        else:
            kaybedilen += 1
        net_rr += mac["rr"]

    oran = kazanilan / len(maclar) * 100

    print("Toplam maç:", len(maclar))
    print("Kazanılan:", kazanilan)
    print("Kaybedilen:", kaybedilen)
    print(f"Kazanma oranı: %{oran:.1f}")
    print(f"Net RR: {net_rr:+}")


def mac_ekle(maclar):
    sonuc = ""
    while sonuc != "k" and sonuc != "y":
        sonuc = input("Maçı kazandın mı? (k/y): ").lower()

    rr = sayi_sor("Kaç RR? (sadece sayı yaz): ")

    # kaybettiyse eksiye çevir
    if sonuc == "y":
        rr = -rr

    yeni_mac = {
        "tarih": str(date.today()),
        "saat": datetime.now().strftime("%H:%M"),
        "sonuc": sonuc.upper(),
        "rr": rr,
    }
    maclar.append(yeni_mac)
    verileri_kaydet(maclar)
    print(f"Maç eklendi ({rr:+} RR)")


def toplu_ekle(maclar):
    toplam = sayi_sor("Bugün kaç maç oynadın? ")
    kazanilan = sayi_sor("Kaçını kazandın? ")

    if kazanilan > toplam:
        print("Kazanılan maç toplamdan fazla olamaz!")
        return

    kaybedilen = toplam - kazanilan

    for i in range(kazanilan):
        rr = sayi_sor(f"{i + 1}. galibiyet kaç RR? ")
        maclar.append({
            "tarih": str(date.today()),
            "saat": datetime.now().strftime("%H:%M"),
            "sonuc": "K",
            "rr": rr,
        })

    for i in range(kaybedilen):
        rr = sayi_sor(f"{i + 1}. mağlubiyet kaç RR? (sadece sayı): ")
        maclar.append({
            "tarih": str(date.today()),
            "saat": datetime.now().strftime("%H:%M"),
            "sonuc": "Y",
            "rr": -rr,
        })

    verileri_kaydet(maclar)
    print("Maçlar kaydedildi.")


def bugunun_ozeti(maclar):
    bugunku_maclar = []
    for mac in maclar:
        if mac["tarih"] == str(date.today()):
            bugunku_maclar.append(mac)

    istatistik_yazdir("Bugün", bugunku_maclar)


def gecmis(maclar):
    if len(maclar) == 0:
        print("Hiç maç yok.")
        return

    # günlere göre grupla
    gunler = {}
    for mac in maclar:
        tarih = mac["tarih"]
        if tarih not in gunler:
            gunler[tarih] = []
        gunler[tarih].append(mac)

    print("\nTarih        Maç  K  Y  Net RR")
    print("-----------------------------")
    for tarih in sorted(gunler.keys(), reverse=True):
        liste = gunler[tarih]
        k = 0
        net = 0
        for mac in liste:
            if mac["sonuc"] == "K":
                k += 1
            net += mac["rr"]
        y = len(liste) - k
        print(f"{tarih}  {len(liste):>3}  {k}  {y}  {net:+}")


def son_maci_sil(maclar):
    if len(maclar) == 0:
        print("Silinecek maç yok.")
        return

    cevap = input("Son maçı silmek istediğine emin misin? (e/h): ")
    if cevap.lower() == "e":
        maclar.pop()
        verileri_kaydet(maclar)
        print("Son maç silindi.")


def main():
    maclar = verileri_yukle()

    while True:
        print("\n===== RANK TAKİP =====")
        print("1 - Maç ekle")
        print("2 - Bugünü toplu gir")
        print("3 - Bugünün özeti")
        print("4 - Günlük geçmiş")
        print("5 - Genel istatistik")
        print("6 - Son maçı sil")
        print("0 - Çıkış")

        secim = input("Seçim: ")

        if secim == "1":
            mac_ekle(maclar)
        elif secim == "2":
            toplu_ekle(maclar)
        elif secim == "3":
            bugunun_ozeti(maclar)
        elif secim == "4":
            gecmis(maclar)
        elif secim == "5":
            istatistik_yazdir("Genel", maclar)
        elif secim == "6":
            son_maci_sil(maclar)
        elif secim == "0":
            print("Görüşürüz!")
            break
        else:
            print("Geçersiz seçim!")


main()
