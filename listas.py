lista=[]
pregunta=input("Cuantos elementos quiere que contenga su lista: ")

for i in range(int(pregunta)):
    n=input(f"introduzca el elemento numero {len(lista)} de la lista: ")
    lista.append(float(n))

print(f"esta es la lista agregada:{lista}")
