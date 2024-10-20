#code by kamran khurshid
sp =int(input("enter sp: "))
cp= int(input("enter cp: "))
profit= (sp-cp)
loss= (cp-sp)
if profit>0:
    print("increased profit of " ,profit)
    profit_per= profit/cp*100
    print("profit_per=" , profit_per)
elif (profit<0):
    print("increased loss of" , loss)
    loss_per= loss/cp*100
    print("loss_per" ,loss_per)