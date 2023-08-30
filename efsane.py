'''
# Liste ve for döngüsü ile çarpım tablosu
tablo = []
for i in range(1, 11):
    satir = []
    for j in range(1, 11):
        carpim = i * j
        satir.append(carpim)
    tablo.append(satir)

# Oluşturulan çarpım tablosunu yazdırma
for satir in tablo:
    for deger in satir:
        print(deger, end="\t")
    print()
    
'''




#The ** operator. To program 25 we do 2 ** 5.
#The built-in pow() function. 23 coded becomes pow(2, 3).
#The math.pow() function. To calculate 35, we do math.pow(3, 5).





a = int(input("Type your first number : "))
b = int(input("Type your second number : "))

if b > a :
    (a,b) = (b,a)
    formula = (a ** (b-1)) % b
    if formula == 1 :
       
       print("Has no common divisor" )
    else :
        print("Has a common divisor")
else :
    
     formula = (a ** (b-1)) % b 


     if formula == 1 :
        
        print("Has no common divisor")
     else :
         print("Has a common divisor")
  




























































































