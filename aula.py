print ("Soma ou Subtracao")
op = int (input ("1-Soma 2-Subtracao"))
a = int (input ("Primeiro operando"))
b = int (input ("Segundo operando"))
res = 0
if op == 1:
    res = a + b
else:
    res = a - b

print (res)
