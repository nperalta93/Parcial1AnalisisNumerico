def poli(x):
    y=ln(x+2)-sin(x)
    return (y)

def deri(x):
    d=1/(x+2)
    return (d)

print "Método de Newton-Raphson"
x=float(raw_input('Introduzca el valor de inicio'))
erroru=float(raw_input('Introduzca el error'))
raiz=[ ]
raiz.insert(0,0)
i=0
error=1
while abs(error)> erroru:
    x1=x-(poli(x)/deri(x))
    raiz.append(x1)
    i=i+1
    x=x1
    error=(raiz[i]-raiz[i-1])/raiz[i]
    print x
