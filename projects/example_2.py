n1 = int(input("1.Not: "))
n2 = int(input("2.Not: "))
n3 = int(input("3.Not: "))

ort = (n1 + n2 + n3) / 3

if(100 >= n1 > 0 and 100 >= n2 > 0 and 100>= n3 > 0):
    print("Ortalamanız: " + str(int((ort))) )

    if ort >= 50:
       print("Dersi Geçtiniz")
    else:
       print("Dersten Kaldınız")
else:
    print("Hatalı Değer Girdiniz!")






    
         
          


    

 
    


    

