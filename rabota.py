import random 

def loe_failist(fail:str)->list:

    f=open(fail,"r",encoding="utf-8-sig")
    jarjend=[]
    for rida in f:
        jarjend.append(rida.strip())
    f.close()
    return jarjend

def kirjuta_failist(fail:str,jarjend:list):
    f=open(fail,"w",encoding="utf-8-sig")
    for line in jarjend:
        f.write(line+"\n")
    f.close


    
def text_est_v_text_rus(text:str, text_est:list, text_rus:list):
    if text in text_est:
        ind=text_est.index(text)

    return text_rus[ind]
 

def rus_na_est(text:str, text_est:list,  text_rus:list ):
    if text in  text_rus:
        ind =  text_rus.index(text)
        
    return text_est[ind]
  

def text_ap(text:str, text_est:list, text_rus:list):
   

        if text not in  text_est:
            text_est.append(text)
            print()
        j=input("Обозначение этого слова на русском: ")
        text_rus.append(j)
        kirjuta_failist('est.txt', text_est)
        kirjuta_failist('rus.txt', text_rus)
        return  j


def correct_word(text:str,text_est:list,text_rus:list):

    if text in text_rus:
       index = text_rus.index(text)
       text = input("Введите слово для исправления: ")
       new_translation = input(f"Введите новое значение для слова '{text}': ")
       text_est[index] = new_translation
       print("Слово успешно исправлено!")
    
    elif text in text_est:
         index=text_est.index(text)
         text = input("Введите слово для исправления: ")
         new_translation = input(f"Введите новое значение для слова '{text}': ")
         text_rus[index] = new_translation
         print("Слово успешно исправлено!")

    else:
        print("Такого слова нету в словаре")

    



def teadmiste_kontroll(text_rus:list,text_est:list):

    p=0
    kokku=int(input("Mitu küsimust? "))
    for i in range(kokku):
        järjend=random.choice([text_rus,text_est])
        sõna=random.choice(järjend)
        print(f"{sõna} - ",end="")
        tõlke=input()
        if sõna in text_rus:
           i=text_rus.index(sõna)
           tõlke_kontroll=text_est[i]
        elif sõna in text_est:
            i=text_est.index(sõna)
            tõlke_kontroll=text_rus[i]
        if tõlke==tõlke_kontroll:
            p+=1
        if (p/kokku)*100>90:
            hinne=5
        elif (p/kokku)*100>75:
            hinne=4
        elif (p/kokku)*100>60:
            hinne=3
        else:
            hinne="Väga halb"
            print("Õige")
            return hinne
    else:
         print("Vale")
    if (p/kokku)*100>90:
        hinne=5
    elif (p/kokku)*100>75:
        hinne=4
    elif (p/kokku)*100>60:
        hinne=3
    else:
         hinne="Väga halb"
    return hinne
