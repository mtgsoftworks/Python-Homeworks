çift = []
tek = []
for i in range(0,55):
    x = int(input("Sayı Girin: ")) 
    if x % 2 == 0:
            çift.append(x)
    else:
        tek.append(x)  
             
print("Tek Liste: " + str(tek))
print("Çift Liste: " + str(çift))
print(len(tek))
print(len(çift))