lista_estudiantes=[]
calculo_nota=0
notas=[]
nota_promedio=[]
numero_estudiantes=input("Cuantos estudiantes quiere ingresar: ")

for i in range(int(numero_estudiantes)):
    n=input(f"introduzca el nombre del estudiante numero {len(lista_estudiantes)+1} de la lista: ")
    lista_estudiantes.append((n))

for i in range(int(numero_estudiantes)):
    for a in range (3):
        nota_nueva=input(f"Introduzca la nota numero {a+1} del estudiante {i+1}: ")
        notas.append(float(nota_nueva))
    calculo_nota=((notas[0]+notas[1]+notas[2])/3)
    nota_promedio.append(calculo_nota)
    notas=[]


for i in range(int(numero_estudiantes)):
    print(f"el estudiante {lista_estudiantes[i]} tiene una nota promedio de: {nota_promedio[i]}")

