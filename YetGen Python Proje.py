import pandas as pd
import random
import time
df = pd.read_excel('Tarot kart anlamları 2.xlsx')


class TarotFali:
    def __init__(self, df):
        self.df = df

    def rastgele_kart_sec(self, kart_sayisi):
        # Kartları rastgele seç
        return self.df.sample(n=kart_sayisi)

    def kart_cevir_1(self, kart):
        # Kartın ters mi düz mü olduğunu rastgele belirle
        durum = 'TERS' if random.choice([True, False]) else 'DÜZ'
        print(f"\nKart: {kart['KARTIN ADI']} - Durum: {durum}")
        if durum == 'TERS':
            if kategori == 'Genel':
                print(f"Genel: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'TERS')]['GENEL'].values[0]}")
            elif kategori == 'Aşk':
                print(f"Aşk: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'TERS')]['AŞK'].values[0]}")
            elif kategori == 'Kariyer':
                print(f"Kariyer: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'TERS')]['KARİYER'].values[0]}")
        else:
            if kategori == 'Genel':
                print(f"Genel: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'DÜZ')]['GENEL'].values[0]}")
            elif kategori == 'Aşk':
                print(f"Aşk: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'DÜZ')]['AŞK'].values[0]}")
            elif kategori == 'Kariyer':
                print(f"Kariyer: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'DÜZ')]['KARİYER'].values[0]}")
            
    def kart_cevir_3(self, kart, k, durum ):
      if k == 0 :
        # Kartın ters mi düz mü olduğunu rastgele belirle
        print(f"\nKart: {kart['KARTIN ADI']} - Durum: {durum}")
        if durum == 'TERS':
          if kategori == 'Genel':
            print(f"Geçmişte Genel anlamı: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'TERS')]['GENEL'].values[0]}")
          elif kategori == 'Aşk':
            print(f"Geçmişte Aşk anlamı: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'TERS')]['AŞK'].values[0]}")
          elif kategori == 'Kariyer':
            print(f"Geçmişte Kariyer anlamı: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'TERS')]['KARİYER'].values[0]}")
        else:
          if kategori == 'Genel':
            print(f"Geçmişte Genel anlamı: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'DÜZ')]['GENEL'].values[0]}")
          elif kategori == 'Aşk':
            print(f"Geçmişte Aşk anlamı: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'DÜZ')]['AŞK'].values[0]}")
          elif kategori == 'Kariyer':
            print(f"Geçmişte Kariyer anlamı: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'DÜZ')]['KARİYER'].values[0]}")

      if k == 1 :
        # Kartın ters mi düz mü olduğunu rastgele belirle
        print(f"\nKart: {kart['KARTIN ADI']} - Durum: {durum}")
        if durum == 'TERS':
          if kategori == 'Genel':
            print(f"Şimdi Genel anlamı: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'TERS')]['GENEL'].values[0]}")
          elif kategori == 'Aşk':
            print(f"Şimdi Aşk anlamı: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'TERS')]['AŞK'].values[0]}")
          elif kategori == 'Kariyer':
            print(f"Şimdi Kariyer anlamı: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'TERS')]['KARİYER'].values[0]}")
        else:
          if kategori == 'Genel':
            print(f"Şimdi Genel anlamı: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'DÜZ')]['GENEL'].values[0]}")
          elif kategori == 'Aşk':
            print(f"Şimdi Aşk anlamı: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'DÜZ')]['AŞK'].values[0]}")
          elif kategori == 'Kariyer':
            print(f"Şimdi Kariyer anlamı: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'DÜZ')]['KARİYER'].values[0]}")

      if k == 2 :
        # Kartın ters mi düz mü olduğunu rastgele belirle
        print(f"\nKart: {kart['KARTIN ADI']} - Durum: {durum}")
        if durum == 'TERS':
          if kategori == 'Genel':
            print(f"Gelecekte Genel anlamı: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'TERS')]['GENEL'].values[0]}")
          elif kategori == 'Aşk':
            print(f"Gelecekte Aşk anlamı: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'TERS')]['AŞK'].values[0]}")
          elif kategori == 'Kariyer':
            print(f"Gelecekte Kariyer anlamı: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'TERS')]['KARİYER'].values[0]}")
        else:
          if kategori == 'Genel':
            print(f"Gelecekte Genel anlamı: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'DÜZ')]['GENEL'].values[0]}")
          elif kategori == 'Aşk':
            print(f"Gelecekte Aşk anlamı: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'DÜZ')]['AŞK'].values[0]}")
          elif kategori == 'Kariyer':
            print(f"Gelecekte Kariyer anlamı: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'DÜZ')]['KARİYER'].values[0]}")

    def kart_cevir_5(self, kart, k, durum):
      if k == 0 :
        # Kartın ters mi düz mü olduğunu rastgele belirle
        print(f"\nKart: {kart['KARTIN ADI']} - Durum: {durum}")
        if durum == 'TERS':
          if kategori == 'Genel':
            print(f"Uzak Geçmiş / Genel: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'TERS')]['GENEL'].values[0]}")
          elif kategori == 'Aşk':
            print(f"Uzak Geçmiş /  Aşk: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'TERS')]['AŞK'].values[0]}")
          elif kategori == 'Kariyer':
            print(f"Uzak Geçmiş / Kariyer: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'TERS')]['KARİYER'].values[0]}")
        else:
          if kategori == 'Genel':
            print(f"Uzak Geçmiş / Genel: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'DÜZ')]['GENEL'].values[0]}")
          elif kategori == 'Aşk':
            print(f"Uzak Geçmiş /  Aşk: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'DÜZ')]['AŞK'].values[0]}")
          elif kategori == 'Kariyer':
            print(f"Uzak Geçmiş / Kariyer: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'DÜZ')]['KARİYER'].values[0]}")

      if k == 1 :
        # Kartın ters mi düz mü olduğunu rastgele belirle
        print(f"\nKart: {kart['KARTIN ADI']} - Durum: {durum}")
        if durum == 'TERS':
          if kategori == 'Genel':
            print(f"Yakın Geçmiş / Genel: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'TERS')]['GENEL'].values[0]}")
          elif kategori == 'Aşk':
            print(f"Yakın Geçmiş / Aşk: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'TERS')]['AŞK'].values[0]}")
          elif kategori == 'Kariyer':
            print(f"Yakın Geçmiş / Kariyer: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'TERS')]['KARİYER'].values[0]}")
        else:
          if kategori == 'Genel':
            print(f"Yakın Geçmiş / Genel: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'DÜZ')]['GENEL'].values[0]}")
          elif kategori == 'Aşk':
            print(f"Yakın Geçmiş / Aşk: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'DÜZ')]['AŞK'].values[0]}")
          elif kategori == 'Kariyer':
            print(f"Yakın Geçmiş / Kariyer: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'DÜZ')]['KARİYER'].values[0]}")

      if k == 2 :
        # Kartın ters mi düz mü olduğunu rastgele belirle
        print(f"\nKart: {kart['KARTIN ADI']} - Durum: {durum}")
        if durum == 'TERS':
          if kategori == 'Genel':
            print(f"Şimdi / Genel: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'TERS')]['GENEL'].values[0]}")
          elif kategori == 'Aşk':
            print(f"Şimdi / Aşk: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'TERS')]['AŞK'].values[0]}")
          elif kategori == 'Kariyer':
            print(f"Şimdi / Kariyer: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'TERS')]['KARİYER'].values[0]}")
        else:
          if kategori == 'Genel':
            print(f"Şimdi / Genel: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'DÜZ')]['GENEL'].values[0]}")
          elif kategori == 'Aşk':
            print(f"Şimdi / Aşk: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'DÜZ')]['AŞK'].values[0]}")
          elif kategori == 'Kariyer':
            print(f"Şimdi / Kariyer: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'DÜZ')]['KARİYER'].values[0]}")

      if k == 3 :
        # Kartın ters mi düz mü olduğunu rastgele belirle
        print(f"\nKart: {kart['KARTIN ADI']} - Durum: {durum}")
        if durum == 'TERS':
          if kategori == 'Genel':
            print(f"Yakın gelecek / Genel: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'TERS')]['GENEL'].values[0]}")
          elif kategori == 'Aşk':
            print(f"Yakın gelecek / Aşk: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'TERS')]['AŞK'].values[0]}")
          elif kategori == 'Kariyer':
            print(f"Yakın gelecek / Kariyer: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'TERS')]['KARİYER'].values[0]}")
        else:
          if kategori == 'Genel':
            print(f"Yakın gelecek / Genel: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'DÜZ')]['GENEL'].values[0]}")
          elif kategori == 'Aşk':
            print(f"Yakın gelecek / Aşk: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'DÜZ')]['AŞK'].values[0]}")
          elif kategori == 'Kariyer':
            print(f"Yakın gelecek / Kariyer: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'DÜZ')]['KARİYER'].values[0]}")

      if k == 4 :
        # Kartın ters mi düz mü olduğunu rastgele belirle
        print(f"\nKart: {kart['KARTIN ADI']} - Durum: {durum}")
        if durum == 'TERS':
          if kategori == 'Genel':
            print(f"Uzak gelecek / Genel: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'TERS')]['GENEL'].values[0]}")
          elif kategori == 'Aşk':
            print(f"Uzak gelecek / Aşk: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'TERS')]['AŞK'].values[0]}")
          elif kategori == 'Kariyer':
            print(f"Uzak gelecek / Kariyer: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'TERS')]['KARİYER'].values[0]}")
        else:
          if kategori == 'Genel':
            print(f"Uzak gelecek / Genel: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'DÜZ')]['GENEL'].values[0]}")
          elif kategori == 'Aşk':
            print(f"Uzak gelecek / Aşk: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'DÜZ')]['AŞK'].values[0]}")
          elif kategori == 'Kariyer':
            print(f"Uzak gelecek / Kariyer: {self.df[(self.df['KARTIN ADI'] == kart['KARTIN ADI']) & (self.df['DURUM'] == 'DÜZ')]['KARİYER'].values[0]}")
  

    def tarot_fali(self, kart_sayisi):
        secilen_kartlar = self.rastgele_kart_sec(kart_sayisi)
        print("Bir soru düşün ve kartın dediklerine güven!")
        print(f"Karıştırılıyor ve senin için {kart_sayisi} kart çekiliyor...")
        time.sleep(3)
        k= 0
        for _, row in secilen_kartlar.iterrows():
          if kart_sayisi == 1:
            self.kart_cevir_1(row)
          if kart_sayisi == 3:
            durum = 'TERS' if random.choice([True, False]) else 'DÜZ'
            self.kart_cevir_3(row, k, durum)
            k += 1
          if kart_sayisi == 5:
            durum = 'TERS' if random.choice([True, False]) else 'DÜZ'
            self.kart_cevir_5(row,k,durum)
            k += 1

while True:
    try:
        # Kullanıcıdan kart sayısını al
        kart_sayisi = int(input("""
        ***TAROTÇU ABLA'YA HOŞ GELDİNİZ***

              1- Tek kart ---> kısa cevaplı sorular
              3- Üç kart ---> geçmiş/şimdi/gelecek
              5- Beş kart ---> uzak geçmiş/yakın geçmiş/şimdi/yakın gelecek/uzak gelecek

              **çıkmak için 'q' ya basınız
              """))
        
        if kart_sayisi not in [1, 3, 5]:
            raise ValueError(f"{kart_sayisi} tane kart seçilemez, sadece 1, 3 veya 5 kart seçebilirsiniz.")
        
        break  # Geçerli bir kart sayısı girildiğinde döngüden çık
    
    except ValueError as ve:
        print(ve)

while True:
    try:
        # Kullanıcıdan fal konusunu al
        kategori = input("""
        Fal konusunu seçiniz:
              Genel
              Aşk
              Kariyer
                        """).capitalize()
        
        if kategori not in ["Genel", "Aşk", "Kariyer"]:
            raise ValueError("Lütfen sadece 'Genel', 'Aşk' veya 'Kariyer' seçeneklerinden birini giriniz.")
        
        break  # Geçerli bir kategori girildiğinde döngüden çık
    
    except ValueError as ve:
        print(ve)

tarot = TarotFali(df)
tarot.tarot_fali(kart_sayisi)

