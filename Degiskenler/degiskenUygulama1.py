"""
Aşağıdaki müşterinin bilgilerini ve satın aldığı bilgilerini değişkenler içerisinde saklayınız.
Toplam ödenen ücret nedir? 
Ödenen miktarın kdv oranı nedir? (%18)

Eyyüb Kantar
0111-111-11-11
info@eyyubkantar.com
Çankırı

Satın Alınan Ürünler

Ürün adı = kablosuz mouse
fiyatı = 550 tl

ürün adı = kablosuz klavye 
fiyatı = 650 tl

ürün adı = dizüstü bilgisayar
fiyatı = 55.000 tl
"""
ad = "Eyyub kantar"
numara = "0111-111-11-11"
mail = "info@eyyubkantar.com"
sehir = "Çankırı"
urun1 = "Kablosuz mouse" 
urun1_fiyat = 550
urun2 = "kablosuz klavye"
urun2_fiyat = 650
urun3 = "dizüstü bilgisayar"
urun3_fiyat = 55000
kdv = 0.18
odenenUcret = urun1_fiyat + urun2_fiyat + urun3_fiyat
sonFiyat = odenenUcret + (odenenUcret * kdv) 
print("adınız = {} /numaranız = {} /mailiniz = {} /sehriniz = {}".format(ad,numara,mail,sehir))
print("Ürünleriniz toplam = " + str(sonFiyat) + " tl tuttu")
