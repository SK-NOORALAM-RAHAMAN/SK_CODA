i=1
y = 0
c = 0
while(i<=10)  :
    import random

    listt=["s","w","g"]
    com=random.choice(listt)


    you=str(input("\nChoose *Snake* or *Water* or *Gun* as\ns||w||g:"))

    if com==you:
        #print(f"Its a Draw, \nTry again..!\n{com} {you}")
        i+=1 #i count Draw situation else it will run more then 10 times

    elif (you=='s' and com=='w') or (you=='g' and com=='s')\
         or (you == 'w' and com == 'g')  :
        #print(f"you win!!! com:{com} you:{you}"
        i+=1
        y+=1

    elif (com=='s' and you=='w') or (com=='g' and you=='s')\
         or (com == 'w' and you == 'g')  :
        #print(f"COM win !!!com:{com} you:{you}")
        i += 1
        c+=1

    else:
        print("Incorrect Input \n Game Over>>\n")
        break


print(f"*You Finely Win*\n#YOU SCORE:{y}\n#COM SCORE:{c}") if y>c else print\
    (f"*COM  Win*\nBetter Luck Next Time...!!\n#YOU SCORE:{y}\n#COM SCORE:{c}")