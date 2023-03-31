meme_sozlugu = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL" : "bir şakaya karşılık cevap",
            "SHEESH" : "onaylamamak",
            "CREEPY" : "korkunç",
            "TO AGGRO" : "agresifleşmek/sinirlenmek"
            }
            
kelime = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if kelime in meme_sozlugu.keys():
    print(meme_sozlugu[kelime])
    
else:
    print("lütfen büyük harf kullanımına dikkat ediniz")
