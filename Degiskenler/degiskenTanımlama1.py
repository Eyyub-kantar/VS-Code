#2000 + 2000 * %18

urunA_fiyat = 4000
urunB_fiyat = 3000
kdvOrani = 0.20
print(urunA_fiyat + (urunA_fiyat*kdvOrani)) # ürün A
print(urunB_fiyat + (urunB_fiyat*kdvOrani)) # ürün B
urunToplami = urunA_fiyat+urunB_fiyat
print(urunToplami + (urunToplami * kdvOrani))