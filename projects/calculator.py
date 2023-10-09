print("""------- Hesap Makinesi -------
[1] - Topla
[2] - Çıkar
[3] - Çarp
[4] - Böl
[5] - Üs Al
[6] - Modülasyon
[7] - Çıkış
------------------------------""")
pn = int(input("İşlem Numarası: "))
if(pn == 7):
     exit()

n1 = float(input("1.Sayı: "))
n2 = float(input("2.Sayı: "))

if pn == 1:
    print("Sonuç: " + str(n1 + n2))
elif pn == 2:
    print("Sonuç: " + str(n1 - n2))
elif pn == 3:
     print("Sonuç: " + str(n1 * n2))
elif pn == 4:
     print("Sonuç: " + str(n1 / n2))
elif pn == 5:
     print("Sonuç: " + str(pow(n1,n2)))
elif pn == 6:
    print("Sonuç: " + str(n1 % n2))
else:
     print("Hatalı Giriş Yaptınız")    
