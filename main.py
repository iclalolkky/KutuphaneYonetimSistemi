C_RESET = '\033[0m'
C_CYAN = '\033[96m'
C_GREEN = '\033[92m'
C_YELLOW = '\033[93m'
C_RED = '\033[91m'
C_MAGENTA = '\033[95m'
C_BOLD = '\033[1m'

class Kitap:
    kutuphane_envanteri = []

    def __init__(self, isim, yazar, sayfa_sayisi, tur):
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.tur = tur

    def kitap_ekle(self):
        Kitap.kutuphane_envanteri.append(self)
        print(f"{C_GREEN}{C_BOLD}✓ Kitap başarıyla eklendi.{C_RESET}")


class BasiliKitap(Kitap):
    def __init__(self, isim, yazar, sayfa_sayisi, tur, adet):
        super().__init__(isim, yazar, sayfa_sayisi, tur)
        self.adet = adet

    def odunc_al(self):
        if self.adet > 0:
            self.adet -= 1
            print(f"{C_GREEN}✓ {self.isim} ödünç alındı. Kalan adet: {self.adet}{C_RESET}")
        else:
            print(f"{C_RED}✗ {self.isim} adlı kitap stokta yok.{C_RESET}")

    def iade_et(self):
        self.adet += 1
        print(f"{C_GREEN}✓ {self.isim} iade edildi. Güncel adet: {self.adet}{C_RESET}")


class EKitap(Kitap):
    def __init__(self, isim, yazar, sayfa_sayisi, tur, dosya_boyutu_mb):
        super().__init__(isim, yazar, sayfa_sayisi, tur)
        self.dosya_boyutu_mb = dosya_boyutu_mb


while True:
    print(f"\n{C_CYAN}{C_BOLD}=== KÜTÜPHANE YÖNETİM SİSTEMİ ==={C_RESET}")
    print(f"{C_CYAN}1-{C_RESET} Kitap Ekle")
    print(f"{C_CYAN}2-{C_RESET} Kitapları Listele")
    print(f"{C_CYAN}3-{C_RESET} Kitap Ödünç Al")
    print(f"{C_CYAN}4-{C_RESET} Kitap İade Et")
    print(f"{C_RED}5-{C_RESET} Çıkış")

    secim = input(f"{C_YELLOW}Seçim: {C_RESET}")

    if secim == '1':
        isim = input(f"{C_MAGENTA}Kitap adı: {C_RESET}")
        yazar = input(f"{C_MAGENTA}Yazar: {C_RESET}")
        sayfa_sayisi = input(f"{C_MAGENTA}Sayfa sayısı: {C_RESET}")

        print(f"\n{C_CYAN}Tür Seçimi:{C_RESET}")
        print(f"{C_CYAN}1-{C_RESET} Basılı Kitap")
        print(f"{C_CYAN}2-{C_RESET} E-Kitap")
        tur_secim = input(f"{C_YELLOW}Tür (1 veya 2): {C_RESET}")

        if tur_secim == '1':
            tur = "Basılı Kitap"
            adet = int(input(f"{C_MAGENTA}Adet: {C_RESET}"))
            yeni_kitap = BasiliKitap(isim, yazar, sayfa_sayisi, tur, adet)
            yeni_kitap.kitap_ekle()
        elif tur_secim == '2':
            tur = "E-Kitap"
            boyut = input(f"{C_MAGENTA}Dosya boyutu (MB): {C_RESET}")
            yeni_kitap = EKitap(isim, yazar, sayfa_sayisi, tur, boyut)
            yeni_kitap.kitap_ekle()
        else:
            print(f"{C_RED}✗ Geçersiz tür.{C_RESET}")

    elif secim == '2':
        print(f"\n{C_MAGENTA}{C_BOLD}--- KİTAP LİSTESİ ---{C_RESET}")
        for kitap in Kitap.kutuphane_envanteri:
            print(f"📖 {C_BOLD}{kitap.isim}{C_RESET} | Yazar: {kitap.yazar} | Tür: {kitap.tur}")

    elif secim == '3':
        aranan = input(f"{C_YELLOW}Ödünç almak istediğiniz kitabın adı: {C_RESET}")
        bulundu = False
        for kitap in Kitap.kutuphane_envanteri:
            if kitap.isim == aranan and isinstance(kitap, BasiliKitap):
                kitap.odunc_al()
                bulundu = True
                break
        if not bulundu:
            print(f"{C_RED}✗ Kitap bulunamadı.{C_RESET}")

    elif secim == '4':
        aranan = input(f"{C_YELLOW}İade etmek istediğiniz kitabın adı: {C_RESET}")
        bulundu = False
        for kitap in Kitap.kutuphane_envanteri:
            if kitap.isim == aranan and isinstance(kitap, BasiliKitap):
                kitap.iade_et()
                bulundu = True
                break
        if not bulundu:
            print(f"{C_RED}✗ Kitap bulunamadı.{C_RESET}")

    elif secim == '5':
        print(f"{C_GREEN}{C_BOLD}Sistemden çıkılıyor...{C_RESET}")
        break

    else:
        print(f"{C_RED}✗ Geçersiz seçim. Lütfen tekrar deneyin.{C_RESET}")