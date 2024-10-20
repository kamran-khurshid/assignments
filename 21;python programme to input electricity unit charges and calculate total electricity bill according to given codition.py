units= int(input("number of units:"))
if units <= 50:
    amount1= 0.5*units
    after_surcharge_1=amount1 + (20/100*amount1)
    print(after_surcharge_1)
elif units <= 150:
    amount2= 0.75*units -  (0.25*50)
    after_surcharge_2=amount2 + (20/100*amount2)
    print(after_surcharge_2)
elif units <=250:
    amount3 = 1.20*units -(100*0.5 - (50*0.70))
    after_surcharge_3= amount3 + (20/100*amount3)
    print(after_surcharge_3)
elif units > 250:
    amount4= 1.50*units - (0.30*100 - (100*0.75 - (50*1.0)))
    after_surcharge_4= amount4 + (20/100*amount4)
    print(after_surcharge_4)