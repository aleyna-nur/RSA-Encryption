


#Aleyna Nur Kemik tarafından yazılmıştır.
print("""**********************
      RSA Şifreleme
**********************""")



def aralarında_asal(n,fi):
    if (n % fi != 0  and n % fi != 0 ):
        print("{} ile {} aralarında asaldır." .format(n,fi))
        return True
    else:
        return False



def s_değerinin_bulunması(n,fi):

    for i in range(1,fi):
        bölen = n * i
        if bölen % fi == 1:
            #print("s değeri : {}".format(i)) #s değeri gizli tutulur.
            return i



def rsa_şifreleme():
    p, q, n = int(input("p: ")), int(input("q: ")), int(input("n: "))

    for i in range(2,p):
        if p % i == 0:
            print("Lütfen asal bir p sayısı giriniz!")
            return

        for i in range(2,q):
            if q % i == 0:
                print("Lütfen asal bir q sayısı giriniz!")
                return

            for i in range(2,n):
                if n % i == 0:
                    print("Lütfen asal bir n sayısı giriniz!")
                    return


    z = p*q #z ve n sayıları kamusal
    print("z' nin değeri : ",z)
    fi = (p-1)*(q-1)
    print("fi' nin değeri : ",fi)

    print("s'nin değeri : ",s_değerinin_bulunması(n,fi)) # s değeri gizlidir.



    while True:
        try:
            a = int(input("Göndermek istediğiniz değeri giriniz!"))
            break

        except:
            print("Geçerli bir a değeri giriniz!")



    if 0<=a and  a<=(z-1):

        şifrelenmiş_değer_c = a**n % z
        print("a'nın şifrelenmiş hali :",şifrelenmiş_değer_c)
        deşifre_değer_a = şifrelenmiş_değer_c**s_değerinin_bulunması(n,fi) % z
        print("c'nin deşifre hali :",deşifre_değer_a)


rsa_şifreleme()
input("Çıkmak için w basınız!")































