#n1=float(input("ingrese el primer termino para sumar:"))
#n2=float(input("ingrese el segundo termino para sumar:"))

#print(n1+n2)
x=""
while x!="salir":
    pregunta=input(f"ingresa la pregunta ")
    if pregunta=="clima":
        print("el clima esta caluroso")
    elif pregunta=="trafico":
        print("hay demasiado trafico")
    else:
        print("no tengo una respuesta para eso")
    x=pregunta
