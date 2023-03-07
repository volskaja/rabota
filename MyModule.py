from класс1 import*

text_est = loe_failist('est.txt')
text_rus = loe_failist('rus.txt')


while True:
           print("1-Перевод с эстонского языка на русский")
           print("2-Перевод с русского языка на эстонский")
           print("3-Добавте слово в словарь")
           print("4-Можете исправить ошибку в слове")
           print("5-Проверка знания слов")
           print("6-Закончить работу")
           v=int(input("Выберите действие: "))
           if v==1:
                  print()
                  print("Перевод с эстонского языка на русский")
                  print()
                  text_es = input("Введите слово на эстонском языке: ")
                  text_ru = text_est_v_text_rus(text_es, text_est, text_rus)
                  if text_ru:
                        print("В переводе на русский это", text_ru)
                  else:
                        print("Ошибка")

           elif v==2:
                    print()
                    print("Перевод с русского языка на эстонский")
                    print()
                    text_ru = input("Введите слово на русском языке: ")
                    text_es = rus_na_est(text_ru, text_est, text_rus)
                    if text_es:
                        print("В переводе на эстонский это", text_es)
                    else:
                        print("Ошибка")

           elif v==3:
                    print()
                    print("Добавте слово в словарь")
                    print()
                    n=int(input("Сколько слов вы хотите добавить: "))
                    for i in range(n):
                        text=input("Напишите слово на эстонском: ")
                        text_ap(text, text_est, text_rus)
                        print()
                    laused=loe_failist("est.txt")
                    for line in laused:
                        print(line)
                    print()    
                    laused=loe_failist("rus.txt")
                    for line in laused:
                        print(line)
                    print()

           elif v==4:
                    print()
                    print("Можете исправить ошибку в слове")
                    print()
                    correct_word(text_est, text_rus, text)
                    
                    laused=loe_failist("est.txt")
                    for line in laused:
                        print(line)

           elif v==5:
                print()
                spin2=teadmiste_kontroll(text_rus,text_est)
           else:
               print("Конец")
               break
