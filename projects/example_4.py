import sys

durum = True
while True:
    if durum == False:
        a1 = int(input("1.sayı: "))
        a2 = int(input("2.Sayı: "))
        print(f'{a1} + {a2} = {a1 + a2}')   

    while True:
        cav = input("Devam etmek istiyor musunuz (Devam -->e, Çıkış -->q): ")
        if cav.lower() == "e":
            durum = False
            break
        
        elif cav.lower() == "q":
            sys.exit()
            

        else:
            continue
            print("Hatalı Giriş Yaptınız")
        
    

    
    
