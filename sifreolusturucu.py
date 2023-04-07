import random
sifrekarakterleri = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

sifreuzunluk = int(input("şifreniz kaç karakterli olsun?"))

sifre = ""

for i in range(sifreuzunluk):
    karakter = random.choice(sifrekarakterleri)
    sifre += karakter

print(sifre)
