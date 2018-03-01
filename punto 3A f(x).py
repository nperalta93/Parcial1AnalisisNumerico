def poli(x):
    y=ln(x+2)-sin(x)
    return (y)

print "Método de la secante"

x1=float(raw_input('Introduzca el valor de x1: '))
x0=float(raw_input('Introduzca el valor de x0: '))
erroru=float(raw_input('Introduzca el error: '))
raiz=[]
raiz.insert(0,0)
i=0
error=1
while abs(error) > erroru:
    x2=x1-(poli(x1)*(x1-x0))/(poli(x1)-poli(x0))
    raiz.append(x2)
    x0=x1
    x1=x2
    i=i+1
    error=(raiz[i]-raiz[i-1])/raiz[i]
    print x2
