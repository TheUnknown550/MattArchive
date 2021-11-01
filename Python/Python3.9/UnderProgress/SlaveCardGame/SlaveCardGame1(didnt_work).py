import random
Card_list=[]
P1=[]
P2=[]
P3=[]
P4=[]
P5=[]
P1_num=[]
P2_num=[]
P3_num=[]
P4_num=[]
P5_num=[]
Card_lis=[]
def card_converter(n):
        if n==1:
            Card='C_A'
        elif n==2:
            Card='D_A'
        elif n==3:
            Card='H_A'
        elif n==4:
                Card='S_A'
        elif n==5:
            Card='C_2'
        elif n==6:
            Card='D_2'
        elif n==7:
            Card='H_2'
        elif n==8:
            Card='S_2'
        elif n==9:
            Card='C_3'
        elif n==10:
            Card='D_3'
        elif n==11:
            Card='H_3'
        elif n==12:
            Card='S_3'
        elif n==13:
            Card='C_4'
        elif n==14:
            Card='D_4'
        elif n==15:
            Card='H_4'
        elif n==16:
            Card='S_4'
        elif n==17:
            Card='C_5'
        elif n==18:
            Card='D_5'
        elif n==19:
            Card='H_5'
        elif n==20:
            Card='S_5'
        elif n==21:
            Card='C_6'
        elif n==22:
            Card='D_6'
        elif n==23:
            Card='H_6'
        elif n==24:
            Card='S_6'
        elif n==25:
            Card='C_7'
        elif n==26:
            Card='D_7'
        elif n==27:
            Card='H_7'
        elif n==28:
            Card='S_7'
        elif n==29:
            Card='C_8'
        elif n==30:
            Card='D_8'
        elif n==31:
            Card='H_8'
        elif n==32:
            Card='S_8'
        elif n==33:
            Card='C_9'
        elif n==34:
            Card='D_9'
        elif n==35:
            Card='H_9'
        elif n==36:
            Card='S_9'
        elif n==37:
            Card='C_10'
        elif n==38:
            Card='D_10'
        elif n==39:
            Card='H_10'
        elif n==40:
            Card='S_10'
        elif n==41:
            Card='C_J'
        elif n==42:
            Card='D_J'
        elif n==43:
            Card='H_J'
        elif n==44:
            Card='S_J'
        elif n==45:
            Card='C_Q'
        elif n==46:
            Card='D_Q'
        elif n==47:
            Card='H_Q'
        elif n==48:
            Card='S_Q'
        elif n==49:
            Card='C_K'
        elif n==50:
            Card='D_K'
        elif n==51:
            Card='H_K'
        else:
            Card='S_K'
        return Card
input('C=Clubs\nD=Diamonds\nH=Hearts\nS=spades\nK=King\nQ=Queen\nJ=Jack')
i=0
while i<10:
    n = random.randint(1,52)
    if not n in Card_list:
        Card_list.append(n)
        P1_num.append(n)
        c=card_converter(n)
        Card_lis.append(c)
        P1.append(c)
        print(P1,end='\r')
        i+=1
input('')
for i in range(10):
    print('')
i=0
while i<10:
    n = random.randint(1,52)
    if not n in Card_list:
        Card_list.append(n)
        P2_num.append(n)
        ca=card_converter(n)
        Card_lis.append(ca)
        P2.append(ca)
        print(P2,end='\r')
        i+=1
input('')
for i in range(10):
    print('')
i=0
while i<10:
    n = random.randint(1,52)
    if not n in Card_list:
        Card_list.append(n)
        P3_num.append(n)
        car=card_converter(n)
        Card_lis.append(car)
        P3.append(car)
        print(P3,end='\r')
        i+=1
input('')
for i in range(10):
    print('')
i=0
while i<11:
    n = random.randint(1,52)
    if not n in Card_list:
        Card_list.append(n)
        P4_num.append(n)
        card=card_converter(n)
        Card_lis.append(card)
        P4.append(card)
        print(P4,end='\r')
        i+=1
input('')
for i in range(10):
    print('')
i=0
while i<11:
    n = random.randint(1,52)
    if not n in Card_list:
        Card_list.append(n)
        P5_num.append(n)
        cards=card_converter(n)
        Card_lis.append(cards)
        P5.append(cards)
        print(P5,end='\r')
        i+=1
input('')
for i in range(10):
    print('')

Played=input('have you played before: ')
if Played=='Yes' or Played=='Y' or Played=='y':
    King=input('Who is king: ')
    Queen=input('Who is Queen: ')
    K_Slave=input('who is King Slave: ')
    Q_Slave=input('Who is Queen Slave: ')
    if King=='P1':
        P1_num.sort()
        P1.sort()
        K_Win1=P1_num.pop(0)
        K_Win2=P1_num.pop(1)
        K_card=P1.copy()
    elif King =='P2':
        P2_num.sort()
        P2.sort()
        K_Win1=P2_num.pop(0)
        K_Win2=P2_num.pop(1)
        K_card=P2.copy()
    elif King =='P3':
        P3_num.sort()
        P3.sort()
        K_Win1=P3_num.pop(0)
        K_Win2=P3_num.pop(1)
        K_card=P3.copy()
    elif King =='P4':
        P4_num.sort()
        P4.sort()
        K_Win1=P4_num.pop(0)
        K_Win2=P4_num.pop(1)
        K_card=P4.copy()
    else:
        P5_num.sort()
        P5.sort()
        K_Win1=P5_num.pop(0)
        K_Win2=P5_num.pop(1)
        K_card=P5.copy()

    if Queen=='P1':
        P1_num.sort()
        P1.sort()
        Q_Win1=P1_num.pop(0)
        Q_card=P1.copy()
    elif Queen =='P2':
        P2_num.sort()
        P2.sort()
        Q_Win1=P2_num.pop(0)
        Q_card=P2.copy()
    elif Queen =='P3':
        P3_num.sort()
        P3.sort()
        Q_Win1=P3_num.pop(0)
        Q_card=P3.copy()
    elif Queen =='P4':
        P4_num.sort()
        P4.sort()
        Q_Win1=P4_num.pop(0)
        Q_card=P4.copy()
    else:
        P5_num.sort()
        P5.sort()
        Q_Win1=P5_num.pop(0)
        Q_card=P5.copy()

    if K_Slave == 'P1':
        P1_num.sort(reverse=True)
        P1.sort(reverse=True)
        K_Lose1=P1_num.pop(0)
        K_Lose2=P1_num.pop(1)
        KS_card=P1.copy()
    elif K_Slave == 'P2':
        P2_num.sort(reverse=True)
        P2.sort(reverse=True)
        K_Lose1=P2_num.pop(0)
        K_Lose2=P2_num.pop(1)
        KS_card=P2.copy()
    elif K_Slave == 'P3':
        P3_num.sort(reverse=True)
        P3.sort(reverse=True)
        K_Lose1=P3_num.pop(0)
        K_Lose2=P3_num.pop(1)
        KS_card=P3.copy()
    elif K_Slave == 'P4':
        P4_num.sort(reverse=True)
        P4.sort(reverse=True)
        K_Lose1=P4_num.pop(0)
        K_Lose2=P4_num.pop(1)
        KS_card=P4.copy()
    else:
        P5_num.sort(reverse=True)
        P5.sort(reverse=True)
        K_Lose1=P5_num.pop(0)
        K_Lose2=P5_num.pop(1)
        KS_card=P5.copy()
    
    if Q_Slave == 'P1':
        P1_num.sort(reverse=True)
        P1.sort(reverse=True)
        Q_Lose1=P1_num.pop(0)
        QS_card=P1.copy()
    elif Q_Slave == 'P2':
        P2_num.sort(reverse=True)
        P2.sort(reverse=True)
        Q_Lose1=P2_num.pop(0)
        QS_card=P2.copy()
    elif Q_Slave == 'P3':
        P3_num.sort(reverse=True)
        P3.sort(reverse=True)
        Q_Lose1=P3_num.pop(0)
        QS_card=P3.copy()
    elif Q_Slave == 'P4':
        P4_num.sort(reverse=True)
        P4.sort(reverse=True)
        Q_Lose1=P4_num.pop(0)
        QS_card=P4.copy()
    else:
        P5_num.sort(reverse=True)
        P5.sort(reverse=True)
        Q_Lose1=P5_num.pop(0)
        QS_card=P5.copy()

    K_lose1=card_converter(K_Win1)
    K_lose2=card_converter(K_Win2)
    Q_lose=card_converter(Q_Win1)
    K_get1=card_converter(K_Lose1)
    K_get2=card_converter(K_Lose2)
    Q_get=card_converter(Q_Lose1)
    K_card.remove(K_lose1)
    K_card.remove(K_Lose2)
    Q_card.remove(Q_lose)
    KS_card.remove(K_get1)
    KS_card.remove(K_get2)
    QS_card.remove(Q_get)
    K_card.append(K_get1)
    K_card.append(K_get2)
    Q_card.append(Q_get)
    KS_card.append(K_Lose1)
    KS_card.append(K_Lose2)
    QS_card.append(Q_lose)

    if King=='P1':
        P1=K_card.copy()
    elif King =='P2':
        P2=K_card.copy()
    elif King =='P3':
        P3=K_card.copy()
    elif King =='P4':
        P4=K_card.copy()
    else:
        P5=K_card.copy()

    if Queen=='P1':
        P1=Q_card.copy()
    elif Queen =='P2':
        P2=Q_card.copy()
    elif Queen =='P3':
        P3=Q_card.copy()
    elif Queen =='P4':
        P4=Q_card.copy()
    else:
        P5=Q_card.copy()

    if K_Slave == 'P1':
        P1=KS_card.copy()
    elif K_Slave == 'P2':
        P2=KS_card.copy()
    elif K_Slave == 'P3':
        P3=KS_card.copy()
    elif K_Slave == 'P4':
        P4=KS_card.copy()
    else:
        P5=KS_card.copy()

    
    if Q_Slave == 'P1':
        P1=QS_card.copy()
    elif Q_Slave == 'P2':
        P2=QS_card.copy()
    elif Q_Slave == 'P3':
        P3=QS_card.copy()
    elif Q_Slave == 'P4':
        P4=QS_card.copy()
    else:
        P5=QS_card.copy()

print('check your cards')
print(P1)
input('')
for i in range(10):
    print('')    
print(P2)
input('')
for i in range(10):
    print('')    
print(P3)
input('')
for i in range(10):
    print('')    
print(P4)
input('')
for i in range(10):
    print('')
print(P5)
input('')
for i in range(10):
    print('')    
P5_C=0
P5_T=None
while True:
    while True:
        P1_T=input('P1 turns: ')
        P1_C=Card_lis.count(P1_T)
        if P1_T in P1 and P1_C > P5_C:
            P1.remove(P1_T)
            print(P1_T)
            P2_T=input('P2 turns: ')
            P2_C=Card_lis.count(P2_T)
            if P2_T in P2 and P2_C > P1_C:
                P2.remove(P2_T)
                print(P2_T)
                P3_T=input('P3 turns: ')
                P3_C=Card_lis.count(P3_T)
                if P3_T in P3 and P3_C > P2_C:
                    P3.remove(P3_T)
                    print(P3_T)
                    P4_T=input('P4 turns: ')
                    P4_C=Card_lis.count(P4_T)
                    if P4_T in P4 and P4_C > P3_C:
                        P4.remove(P4_T)
                        print(P4_T)
                        P5_T=input('P5 turns: ')
                        P5_C=Card_lis.count(P5_T)
                        if P5_T in P5 and P5_C > P4_C:
                            P5.remove(P5_T)
                            print(P5_T)
                        elif P5_T in P5:
                            print('this card is not higher than', P4_T)
                        elif P5_T =='pass' or len(P5)==0:
                            break
                        else:
                            print('card is not in deck plz pick another card')
                    elif P4_T in P4:
                        print('this card is not higher than ', P3_T)
                    elif P4_T =='pass' or len(P4)==0:
                        break
                    else:
                        print('card is not in deck plz pick another card')
                elif P3_T in P3:
                    print('Tjis card is not higher than ', P2_T)
                elif P3_T =='pass' or len(P3)==0:
                    break
                else:
                    print('card is not in deck plz pick another card')
            elif P2_T in P2:
                print('this card is not higher than ', P1_T)
            elif P2_T =='pass' or len(P2)==0:
                break
            else:
                print('card is not in deck plz pick another card')
        elif P1_T in P1:
            print('this card is not higher than ',P5_T)
        elif P1_T =='pass' or len(P1)==0:
            break
        else:
            print('card is not in deck plz pick another card')

    if len(P1)==0:
        print('Player 1 Wins')
        break

    elif len(P2)==0:
        print('player 2 wins')
        break
    
    elif len(P3)==0:
        print('player 3 wins')
        break
    
    elif len(P4)==0:
        print('Player 3 wins')
        break

    elif len(P5)==0:
        print('player 5 wins')
        break

    elif P1_T=='pass' and P2_T == 'pass' and P3_T =='pass':
        P4_T=input('P4 turns: ')
        P4_C=Card_lis.count(P4_T)
        if P4_T in P4 and P4_C > P5_C:
            P4.remove(P4_T)
            print(P4_T)
            P5_T=input('P5 turns: ')
            P5_C=Card_lis.count(P5_T)
            if P5_T in P5 and P5_C > P4_C:
                P5.remove(P5_T)
                print(P5_T)
            elif P5_T in P5:
                print('this card is not higher than', P4_T)
            elif P5_T =='pass' or len(P5)==0:
                break
            else:
                print('card is not in deck plz pick another card')
        elif P4_T in P4:
            print('this card is not higher than ', P5_T)
        elif P4_T =='pass' or len(P4)==0:
            break
        else:
            print('card is not in deck plz pick another card')

    elif P1_T=='pass' and P2_T == 'pass' and P4_T =='pass':
        P5_T=input('P5 turns: ')
        P5_C=Card_lis.count(P4_T)
        if P5_T in P4 and P5_C > P3_C:
            P5.remove(P5_T)
            print(P5_T)
            P3_T=input('P3 turns: ')
            P3_C=Card_lis.count(P3_T)
            if P3_T in P3 and P3_C > P5_C:
                P3.remove(P3_T)
                print(P3_T)
            elif P3_T in P3:
                print('this card is not higher than', P5_T)
            elif P3_T =='pass' or len(P3)==0:
                break
            else:
                print('card is not in deck plz pick another card')
        elif P5_T in P5:
            print('this card is not higher than ', P3_T)
        elif P5_T =='pass' or len(P5)==0:
            break
        else:
            print('card is not in deck plz pick another card')

    elif P1_T=='pass' and P2_T == 'pass' and P5_T =='pass':
        P3_T=input('P3 turns: ')
        P3_C=Card_lis.count(P3_T)
        if P3_T in P3 and P3_C > P4_C:
            P3.remove(P3_T)
            print(P3_T)
            P4_T=input('P4 turns: ')
            P4_C=Card_lis.count(P4_T)
            if P4_T in P4 and P4_C > P3_C:
                P4.remove(P4_T)
                print(P4_T)
            elif P4_T in P4:
                print('this card is not higher than', P3_T)
            elif P4_T =='pass' or len(P4)==0:
                break
            else:
                print('card is not in deck plz pick another card')
        elif P3_T in P3:
            print('this card is not higher than ', P4_T)
        elif P3_T =='pass' or len(P3)==0:
            break
        else:
            print('card is not in deck plz pick another card')

    elif P1_T=='pass' and P3_T == 'pass' and P5_T =='pass':
        P2_T=input('P2 turns: ')
        P2_C=Card_lis.count(P2_T)
        if P2_T in P2 and P2_C > P4_C:
            P2.remove(P2_T)
            print(P2_T)
            P4_T=input('P4 turns: ')
            P4_C=Card_lis.count(P4_T)
            if P4_T in P4 and P4_C > P3_C:
                P4.remove(P4_T)
                print(P4_T)
            elif P4_T in P4:
                print('this card is not higher than', P2_T)
            elif P4_T =='pass' or len(P4)==0:
                break
            else:
                print('card is not in deck plz pick another card')
        elif P2_T in P2:
            print('this card is not higher than ', P4_T)
        elif P2_T =='pass' or len(P2)==0:
            break
        else:
            print('card is not in deck plz pick another card')

    elif P1_T=='pass' and P3_T == 'pass' and P4_T =='pass':
        P5_T=input('P5 turns: ')
        P5_C=Card_lis.count(P5_T)
        if P5_T in P5 and P5_C > P2_C:
            P5.remove(P5_T)
            print(P5_T)
            P2_T=input('P2 turns: ')
            P2_C=Card_lis.count(P2_T)
            if P2_T in P2 and P2_C > P5_C:
                P2.remove(P2_T)
                print(P2_T)
            elif P2_T in P2:
                print('this card is not higher than', P5_T)
            elif P2_T =='pass' or len(P2)==0:
                break
            else:
                print('card is not in deck plz pick another card')
        elif P5_T in P5:
            print('this card is not higher than ', P2_T)
        elif P5_T =='pass' or len(P5)==0:
            break
        else:
            print('card is not in deck plz pick another card')
        
    elif P1_T=='pass' and P4_T == 'pass' and P5_T =='pass':
        P2_T=input('P2 turns: ')
        P2_C=Card_lis.count(P2_T)
        if P2_T in P2 and P2_C > P3_C:
            P2.remove(P2_T)
            print(P2_T)
            P3_T=input('P3 turns: ')
            P3_C=Card_lis.count(P3_T)
            if P3_T in P3 and P3_C > P2_C:
                P3.remove(P3_T)
                print(P3_T)
            elif P3_T in P3:
                print('this card is not higher than', P2_T)
            elif P3_T =='pass' or len(P3)==0:
                break
            else:
                print('card is not in deck plz pick another card')
        elif P2_T in P2:
            print('this card is not higher than ', P3_T)
        elif P2_T =='pass' or len(P2)==0:
            break
        else:
            print('card is not in deck plz pick another card')

    elif P2_T=='pass' and P3_T == 'pass' and P4_T =='pass':
        P5_T=input('P5 turns: ')
        P5_C=Card_lis.count(P4_T)
        if P5_T in P4 and P5_C > P1_C:
            P5.remove(P5_T)
            print(P5_T)
            P1_T=input('P1 turns: ')
            P1_C=Card_lis.count(P1_T)
            if P1_T in P1 and P1_C > P5_C:
                P1.remove(P1_T)
                print(P1_T)
            elif P1_T in P1:
                print('this card is not higher than', P5_T)
            elif P1_T =='pass' or len(P1)==0:
                break
            else:
                print('card is not in deck plz pick another card')
        elif P5_T in P5:
            print('this card is not higher than ', P1_T)
        elif P5_T =='pass' or len(P5)==0:
            break
        else:
            print('card is not in deck plz pick another card')

    elif P3_T=='pass' and P4_T == 'pass' and P5_T =='pass':
        P1_T=input('P1 turns: ')
        P1_C=Card_lis.count(P1_T)
        if P1_T in P1 and P1_C > P2_C:
            P1.remove(P1_T)
            print(P1_T)
            P2_T=input('P2 turns: ')
            P2_C=Card_lis.count(P2_T)
            if P2_T in P2 and P2_C > P1_C:
                P2.remove(P2_T)
                print(P2_T)
            elif P2_T in P2:
                print('this card is not higher than', P1_T)
            elif P2_T =='pass' or len(P2)==0:
                break
            else:
                print('card is not in deck plz pick another card')
        elif P1_T in P1:
            print('this card is not higher than ', P2_T)
        elif P1_T =='pass' or len(P1)==0:
            break
        else:
            print('card is not in deck plz pick another card')

    elif P2_T=='pass' and P4_T == 'pass' and P5_T =='pass':
        P1_T=input('P1 turns: ')
        P1_C=Card_lis.count(P1_T)
        if P1_T in P1 and P1_C > P2_C:
            P1.remove(P1_T)
            print(P1_T)
            P3_T=input('P3 turns: ')
            P3_C=Card_lis.count(P3_T)
            if P3_T in P3 and P3_C > P1_C:
                P3.remove(P3_T)
                print(P3_T)
            elif P3_T in P3:
                print('this card is not higher than', P1_T)
            elif P3_T =='pass' or len(P3)==0:
                break
            else:
                print('card is not in deck plz pick another card')
        elif P1_T in P1:
            print('this card is not higher than ', P3_T)
        elif P1_T =='pass' or len(P1)==0:
            break
        else:
            print('card is not in deck plz pick another card')

    elif P2_T=='pass' and P3_T == 'pass' and P5_T =='pass':
        P1_T=input('P1 turns: ')
        P1_C=Card_lis.count(P1_T)
        if P1_T in P1 and P1_C > P2_C:
            P1.remove(P1_T)
            print(P1_T)
            P4_T=input('P4 turns: ')
            P4_C=Card_lis.count(P4_T)
            if P4_T in P4 and P4_C > P1_C:
                P4.remove(P4_T)
                print(P4_T)
            elif P4_T in P4:
                print('this card is not higher than', P1_T)
            elif P4_T =='pass' or len(P4)==0:
                break
            else:
                print('card is not in deck plz pick another card')
        elif P1_T in P1:
            print('this card is not higher than ', P4_T)
        elif P1_T =='pass' or len(P1)==0:
            break
        else:
            print('card is not in deck plz pick another card')


    elif P1_T=='pass' and P2_T == 'pass':
        while True:
            P3_T=input('P3 turns: ')
            P3_C=Card_lis.count(P3_T)
            if P3_T in P3 and P3_C > P5_C:
                P3.remove(P3_T)
                print(P3_T)
                P4_T=input('P4 turns: ')
                P4_C=Card_lis.count(P4_T)
                if P4_T in P5 and P4_C > P3_C:
                    P4.remove(P4_T)
                    print(P4_T)                        
                    P5_T=input('P5 turns: ')
                    P5_C=Card_lis.count(P5_T)
                    if P5_T in P5 and P5_C > P4_C:
                        P5.remove(P5_T)
                        print(P5_T)
                    elif P5_T in P5:
                        print('this card is not higher than', P4_T)
                    elif P5_T =='pass' or len(P5)==0:
                        break
                    else:
                        print('card is not in deck plz pick another card')
                elif P4_T in P4:
                    print('this card is not higher than ', P3_T)
                elif P4_T =='pass' or len(P4)==0:
                    break
                else:
                    print('card is not in deck plz pick another card')
            elif P3_T in P3:
                print('Tjis card is not higher than ', P5_T)
            elif P3_T =='pass' or len(P3)==0:
                break
            else:
                print('card is not in deck plz pick another card')

    elif P1_T=='pass' and P3_T == 'pass':
        while True:
            P4_T=input('P4 turns: ')
            P4_C=Card_lis.count(P4_T)
            if P4_T in P4 and P4_C > P2_C:
                P3.remove(P4_T)
                print(P4_T)
                P5_T=input('P5 turns: ')
                P5_C=Card_lis.count(P5_T)
                if P5_T in P5 and P5_C > P4_C:
                    P5.remove(P5_T)
                    print(P5_T)                        
                    P2_T=input('P2 turns: ')
                    P2_C=Card_lis.count(P2_T)
                    if P2_T in P2 and P2_C > P5_C:
                        P2.remove(P2_T)
                        print(P2_T)
                    elif P2_T in P2:
                        print('this card is not higher than', P5_T)
                    elif P2_T =='pass' or len(P2)==0:
                        break
                    else:
                        print('card is not in deck plz pick another card')
                elif P5_T in P5:
                    print('this card is not higher than ', P4_T)
                elif P5_T =='pass' or len(P5)==0:
                    break
                else:
                    print('card is not in deck plz pick another card')
            elif P4_T in P4:
                print('Tjis card is not higher than ', P2_T)
            elif P4_T =='pass' or len(P4)==0:
                break
            else:
                print('card is not in deck plz pick another card')

    elif P1_T=='pass' and P4_T == 'pass':
        while True:
            P5_T=input('P5 turns: ')
            P5_C=Card_lis.count(P5_T)
            if P5_T in P5 and P5_C > P3_C:
                P5.remove(P5_T)
                print(P5_T)
                P2_T=input('P2 turns: ')
                P2_C=Card_lis.count(P2_T)
                if P2_T in P2 and P2_C > P5_C:
                    P2.remove(P2_T)
                    print(P2_T)                        
                    P3_T=input('P3 turns: ')
                    P3_C=Card_lis.count(P3_T)
                    if P3_T in P3 and P3_C > P2_C:
                        P3.remove(P3_T)
                        print(P3_T)
                    elif P3_T in P3:
                        print('this card is not higher than', P2_T)
                    elif P3_T =='pass' or len(P3)==0:
                        break
                    else:
                        print('card is not in deck plz pick another card')
                elif P2_T in P2:
                    print('this card is not higher than ', P5_T)
                elif P2_T =='pass' or len(P2)==0:
                    break
                else:
                    print('card is not in deck plz pick another card')
            elif P5_T in P5:
                print('Tjis card is not higher than ', P3_T)
            elif P5_T =='pass' or len(P5)==0:
                break
            else:
                print('card is not in deck plz pick another card')

    elif P1_T=='pass' and P5_T == 'pass':
        while True:
            P2_T=input('P2 turns: ')
            P2_C=Card_lis.count(P2_T)
            if P2_T in P2 and P2_C > P4_C:
                P2.remove(P2_T)
                print(P2_T)
                P3_T=input('P3 turns: ')
                P3_C=Card_lis.count(P3_T)
                if P3_T in P3 and P3_C > P2_C:
                    P3.remove(P3_T)
                    print(P3_T)                        
                    P4_T=input('P4 turns: ')
                    P4_C=Card_lis.count(P4_T)
                    if P4_T in P4 and P4_C > P3_C:
                        P4.remove(P4_T)
                        print(P4_T)
                    elif P4_T in P4:
                        print('this card is not higher than', P3_T)
                    elif P4_T =='pass' or len(P4)==0:
                        break
                    else:
                        print('card is not in deck plz pick another card')
                elif P3_T in P3:
                    print('this card is not higher than ', P2_T)
                elif P3_T =='pass' or len(P3)==0:
                    break
                else:
                    print('card is not in deck plz pick another card')
            elif P2_T in P2:
                print('Tjis card is not higher than ', P4_T)
            elif P2_T =='pass' or len(P2)==0:
                break
            else:
                print('card is not in deck plz pick another card')
        
    elif P2_T=='pass' and P3_T == 'pass':
        while True:
            P4_T=input('P4 turns: ')
            P4_C=Card_lis.count(P1_T)
            if P4_T in P4 and P4_C > P1_C:
                P4.remove(P4_T)
                print(P4_T)
                P5_T=input('P5 turns: ')
                P5_C=Card_lis.count(P5_T)
                if P5_T in P5 and P5_C > P4_C:
                    P5.remove(P5_T)
                    print(P5_T)                        
                    P1_T=input('P1 turns: ')
                    P2_C=Card_lis.count(P2_T)
                    if P1_T in P1 and P1_C > P5_C:
                        P5.remove(P1_T)
                        print(P1_T)
                    elif P1_T in P1:
                        print('this card is not higher than', P5_T)
                    elif P1_T =='pass' or len(P1)==0:
                        break
                    else:
                        print('card is not in deck plz pick another card')
                elif P5_T in P5:
                    print('this card is not higher than ', P4_T)
                elif P5_T =='pass' or len(P5)==0:
                    break
                else:
                    print('card is not in deck plz pick another card')
            elif P4_T in P4:
                print('Tjis card is not higher than ', P1_T)
            elif P4_T =='pass' or len(P4)==0:
                break
            else:
                print('card is not in deck plz pick another card')

    if P2_T=='pass' and P4_T == 'pass':
        while True:
            P5_T=input('P5 turns: ')
            P5_C=Card_lis.count(P5_T)
            if P5_T in P5 and P5_C > P2_C:
                P5.remove(P5_T)
                print(P5_T)
                P1_T=input('P1 turns: ')
                P1_C=Card_lis.count(P1_T)
                if P1_T in P1 and P1_C > P5_C:
                    P1.remove(P1_T)
                    print(P1_T)                        
                    P3_T=input('P3 turns: ')
                    P3_C=Card_lis.count(P3_T)
                    if P3_T in P3 and P3_C > P1_C:
                        P3.remove(P3_T)
                        print(P3_T)
                    elif P3_T in P3:
                        print('this card is not higher than', P1_T)
                    elif P3_T =='pass' or len(P3)==0:
                        break
                    else:
                        print('card is not in deck plz pick another card')
                elif P2_T in P2:
                    print('this card is not higher than ', P5_T)
                elif P2_T =='pass' or len(P2)==0:
                    break
                else:
                    print('card is not in deck plz pick another card')
            elif P5_T in P5:
                print('Tjis card is not higher than ', P3_T)
            elif P5_T =='pass' or len(P5)==0:
                break
            else:
                print('card is not in deck plz pick another card')

    if P2_T=='pass' and P5_T == 'pass':
        while True:
            P1_T=input('P1 turns: ')
            P1_C=Card_lis.count(P1_T)
            if P1_T in P2 and P1_C > P4_C:
                P1.remove(P1_T)
                print(P1_T)
                P3_T=input('P3 turns: ')
                P3_C=Card_lis.count(P3_T)
                if P3_T in P3 and P3_C > P1_C:
                    P3.remove(P3_T)
                    print(P3_T)                        
                    P4_T=input('P4 turns: ')
                    P4_C=Card_lis.count(P4_T)
                    if P4_T in P4 and P4_C > P3_C:
                        P4.remove(P4_T)
                        print(P4_T)
                    elif P4_T in P4:
                        print('this card is not higher than', P3_T)
                    elif P4_T =='pass' or len(P4)==0:
                        break
                    else:
                        print('card is not in deck plz pick another card')
                elif P3_T in P3:
                    print('this card is not higher than ', P1_T)
                elif P3_T =='pass' or len(P3)==0:
                    break
                else:
                    print('card is not in deck plz pick another card')
            elif P1_T in P1:
                print('Tjis card is not higher than ', P4_T)
            elif P1_T =='pass' or len(P1)==0:
                break
            else:
                print('card is not in deck plz pick another card')

    if P3_T=='pass' and P4_T == 'pass':
        while True:
            P5_T=input('P5 turns: ')
            P5_C=Card_lis.count(P5_T)
            if P5_T in P5 and P5_C > P2_C:
                P5.remove(P5_T)
                print(P5_T)
                P1_T=input('P1 turns: ')
                P1_C=Card_lis.count(P1_T)
                if P1_T in P1 and P1_C > P5_C:
                    P1.remove(P1_T)
                    print(P1_T)                        
                    P2_T=input('P2 turns: ')
                    P2_C=Card_lis.count(P2_T)
                    if P2_T in P2 and P2_C > P1_C:
                        P2.remove(P2_T)
                        print(P2_T)
                    elif P2_T in P2:
                        print('this card is not higher than', P1_T)
                    elif P2_T =='pass' or len(P2)==0:
                        break
                    else:
                        print('card is not in deck plz pick another card')
                elif P1_T in P1:
                    print('this card is not higher than ', P5_T)
                elif P1_T =='pass' or len(P2)==0:
                    break
                else:
                    print('card is not in deck plz pick another card')
            elif P5_T in P5:
                print('Tjis card is not higher than ', P2_T)
            elif P5_T =='pass' or len(P5)==0:
                break
            else:
                print('card is not in deck plz pick another card')

    if P3_T=='pass' and P5_T == 'pass':
        while True:
            P1_T=input('P1 turns: ')
            P1_C=Card_lis.count(P1_T)
            if P1_T in P1 and P1_C > P4_C:
                P1.remove(P1_T)
                print(P1_T)
                P2_T=input('P2 turns: ')
                P2_C=Card_lis.count(P2_T)
                if P2_T in P2 and P2_C > P1_C:
                    P2.remove(P2_T)
                    print(P2_T)                        
                    P4_T=input('P4 turns: ')
                    P4_C=Card_lis.count(P4_T)
                    if P4_T in P4 and P4_C > P2_C:
                        P4.remove(P4_T)
                        print(P4_T)
                    elif P4_T in P4:
                        print('this card is not higher than', P2_T)
                    elif P4_T =='pass' or len(P4)==0:
                        break
                    else:
                        print('card is not in deck plz pick another card')
                elif P2_T in P2:
                    print('this card is not higher than ', P1_T)
                elif P2_T =='pass' or len(P2)==0:
                    break
                else:
                    print('card is not in deck plz pick another card')
            elif P1_T in P1:
                print('Tjis card is not higher than ', P4_T)
            elif P1_T =='pass' or len(P1)==0:
                break
            else:
                print('card is not in deck plz pick another card')

    if P4_T=='pass' and P5_T == 'pass':
        while True:
            P1_T=input('P1 turns: ')
            P1_C=Card_lis.count(P1_T)
            if P1_T in P1 and P1_C > P3_C:
                P1.remove(P1_T)
                print(P1_T)
                P2_T=input('P2 turns: ')
                P2_C=Card_lis.count(P2_T)
                if P2_T in P2 and P2_C > P1_C:
                    P2.remove(P2_T)
                    print(P2_T)                        
                    P3_T=input('P3 turns: ')
                    P3_C=Card_lis.count(P3_T)
                    if P3_T in P3 and P3_C > P2_C:
                        P3.remove(P3_T)
                        print(P3_T)
                    elif P3_T in P3:
                        print('this card is not higher than', P2_T)
                    elif P3_T =='pass' or len(P3)==0:
                        break
                    else:
                        print('card is not in deck plz pick another card')
                elif P2_T in P2:
                    print('this card is not higher than ', P1_T)
                elif P2_T =='pass' or len(P2)==0:
                    break
                else:
                    print('card is not in deck plz pick another card')
            elif P1_T in P1:
                print('Tjis card is not higher than ', P3_T)
            elif P1_T =='pass' or len(P1)==0:
                break
            else:
                print('card is not in deck plz pick another card')

    elif P1_T == 'pass':
        while True:
            P2_T=input('Its P2 turn: ')
            P2_C=Card_lis.count(P2_T)
            if P2_T in P2 and P2_C > P1_C:
                P2.remove(P2_T)
                print(P2_T)
                P3_T=input('P3 turns: ')
                P3_C=Card_lis.count(P3_T)
                if P3_T in P3 and P3_C > P2_C:
                    P3.remove(P3_T)
                    print(P3_T)
                    P4_T=input('P4 turns: ')
                    P4_C=Card_lis.count(P4_T)
                    if P4_T in P4 and P4_C > P3_C:
                        P4.remove(P4_T)
                        print(P4_T)
                        P5_T=input('P5 turns: ')
                        P5_C=Card_lis.count(P5_T)
                        if P5_T in P5 and P5_C > P4_C:
                            P5.remove(P5_T)
                            print(P5_T)
                        elif P5_T in P5:
                            print('this card is not higher than', P4_T)
                        elif P5_T =='pass' or len(P5)==0:
                            break
                        else:
                            print('card is not in deck plz pick another card')
                    elif P4_T in P4:
                        print('this card is not higher than ', P3_T)
                    elif P4_T =='pass' or len(P4)==0:
                        break
                    else:
                        print('card is not in deck plz pick another card')
                elif P3_T in P3:
                    print('Tjis card is not higher than ', P2_T)
                elif P3_T =='pass' or len(P3)==0:
                    break
                else:
                    print('card is not in deck plz pick another card')
            elif P2_T in P2:
                print('this card is not higher than ', P5_T)
            elif P2_T =='pass' or len(P2)==0:
                break
            else:
                print('card is not in deck plz pick another card')

    elif P2_T == 'pass':
        while True:
            P3_T=input('Its P3 turn: ')
            P3_C=Card_lis.count(P3_T)
            if P3_T in P3 and P3_C > P1_C:
                P3.remove(P3_T)
                print(P3_T)
                P4_T=input('P4 turns: ')
                P4_C=Card_lis.count(P4_T)
                if P4_T in P4 and P4_C > P3_C:
                    P3.remove(P4_T)
                    print(P4_T)
                    P5_T=input('P5 turns: ')
                    P5_C=Card_lis.count(P5_T)
                    if P5_T in P5 and P5_C > P4_C:
                        P5.remove(P5_T)
                        print(P5_T)
                        P1_T=input('P1 turns: ')
                        P1_C=Card_lis.count(P1_T)
                        if P1_T in P1 and P1_C > P5_C:
                            P1.remove(P1_T)
                            print(P1_T)
                        elif P1_T in P1:
                            print('this card is not higher than', P5_T)
                        elif P1_T =='pass' or len(P1)==0:
                            break
                        else:
                            print('card is not in deck plz pick another card')
                    elif P5_T in P5:
                        print('this card is not higher than ', P4_T)
                    elif P5_T =='pass' or len(P5)==0:
                        break
                    else:
                        print('card is not in deck plz pick another card')
                elif P4_T in P4:
                    print('Tjis card is not higher than ', P3_T)
                elif P4_T =='pass' or len(P4)==0:
                    break
                else:
                    print('card is not in deck plz pick another card')
            elif P3_T in P3:
                print('this card is not higher than ', P1_T)
            elif P3_T =='pass' or len(P3)==0:
                break
            else:
                print('card is not in deck plz pick another card')

    elif P3_T == 'pass':
        while True:
            P4_T=input('Its P4 turn: ')
            P4_C=Card_lis.count(P4_T)
            if P4_T in P4 and P4_C > P2_C:
                P4.remove(P4_T)
                print(P4_T)
                P5_T=input('P5 turns: ')
                P5_C=Card_lis.count(P5_T)
                if P5_T in P5 and P5_C > P4_C:
                    P5.remove(P5_T)
                    print(P5_T)
                    P1_T=input('P1 turns: ')
                    P1_C=Card_lis.count(P1_T)
                    if P1_T in P1 and P1_C > P5_C:
                        P4.remove(P1_T)
                        print(P1_T)
                        P2_T=input('P2 turns: ')
                        P2_C=Card_lis.count(P2_T)
                        if P2_T in P2 and P2_C > P1_C:
                            P2.remove(P2_T)
                            print(P2_T)
                        elif P2_T in P2:
                            print('this card is not higher than', P2_T)
                        elif P2_T =='pass' or len(P2)==0:
                            break
                        else:
                            print('card is not in deck plz pick another card')
                    elif P1_T in P1:
                        print('this card is not higher than ', P5_T)
                    elif P1_T =='pass' or len(P1)==0:
                        break
                    else:
                        print('card is not in deck plz pick another card')
                elif P5_T in P5:
                    print('Tjis card is not higher than ', P4_T)
                elif P5_T =='pass' or len(P5)==0:
                    break
                else:
                    print('card is not in deck plz pick another card')
            elif P4_T in P4:
                print('this card is not higher than ', P2_T)
            elif P2_T =='pass' or len(P4)==0:
                break
            else:
                print('card is not in deck plz pick another card')
            
    elif P4_T == 'pass':
        while True:
            P5_T=input('Its P5 turn: ')
            P5_C=Card_lis.count(P5_T)
            if P5_T in P5 and P5_C > P3_C:
                P5.remove(P5_T)
                print(P5_T)
                P1_T=input('P1 turns: ')
                P1_C=Card_lis.count(P1_T)
                if P1_T in P1 and P1_C > P5_C:
                    P1.remove(P1_T)
                    print(P1_T)
                    P2_T=input('P2 turns: ')
                    P2_C=Card_lis.count(P2_T)
                    if P2_T in P2 and P2_C > P1_C:
                        P2.remove(P2_T)
                        print(P2_T)
                        P3_T=input('P3 turns: ')
                        P3_C=Card_lis.count(P3_T)
                        if P3_T in P3 and P3_C > P2_C:
                            P3.remove(P3_T)
                            print(P3_T)
                        elif P3_T in P3:
                            print('this card is not higher than', P2_T)
                        elif P3_T =='pass' or len(P3)==0:
                            break
                        else:
                            print('card is not in deck plz pick another card')
                    elif P2_T in P2:
                        print('this card is not higher than ', P1_T)
                    elif P2_T =='pass' or len(P2)==0:
                        break
                    else:
                        print('card is not in deck plz pick another card')
                elif P1_T in P1:
                    print('Tjis card is not higher than ', P1_T)
                elif P1_T =='pass' or len(P1)==0:
                    break
                else:
                    print('card is not in deck plz pick another card')
            elif P5_T in P5:
                print('this card is not higher than ', P3_T)
            elif P5_T =='pass' or len(P5)==0:
                break
            else:
                print('card is not in deck plz pick another card')

    elif P5_T == 'pass':
        while True:
            P1_T=input('Its P1 turn: ')
            P1_C=Card_lis.count(P1_T)
            if P1_T in P1 and P1_C > P4_C:
                P1.remove(P1_T)
                print(P1_T)
                P2_T=input('P2 turns: ')
                P2_C=Card_lis.count(P2_T)
                if P2_T in P2 and P2_C > P1_C:
                    P2.remove(P2_T)
                    print(P2_T)
                    P3_T=input('P3 turns: ')
                    P3_C=Card_lis.count(P3_T)
                    if P3_T in P3 and P3_C > P2_C:
                        P3.remove(P3_T)
                        print(P3_T)
                        P4_T=input('P4 turns: ')
                        P4_C=Card_lis.count(P4_T)
                        if P4_T in P4 and P4_C > P3_C:
                            P4.remove(P4_T)
                            print(P4_T)
                        elif P4_T in P4:
                            print('this card is not higher than', P3_T)
                        elif P4_T =='pass' or len(P4)==0:
                            break
                        else:
                            print('card is not in deck plz pick another card')
                    elif P3_T in P3:
                        print('this card is not higher than ', P2_T)
                    elif P3_T =='pass' or len(P3)==0:
                        break
                    else:
                        print('card is not in deck plz pick another card')
                elif P2_T in P2:
                    print('Tjis card is not higher than ', P1_T)
                elif P2_T =='pass' or len(P2)==0:
                    break
                else:
                    print('card is not in deck plz pick another card')
            elif P1_T in P1:
                print('this card is not higher than ', P4_T)
            elif P1_T =='pass'or len(P1)==0:
                break
            else:
                print('card is not in deck plz pick another card')