lista_estudiantes=[]
notas=[]
nota_promedio=[]
numero_estudiantes=input("Cuantos estudiantes quiere ingresar: ")

for i in range(int(numero_estudiantes)):
    n=input(f"introduzca el nombre del estudiante numero {lista_estudiantes[i]} de la lista: ")
    lista_estudiantes.append((n))

for i2 in range(int(numero_estudiantes)):
    for a in range (3):
        nota_nueva=input(f"Introduzca la nota numero {a+1} del estudiante {i2+1}: ")
        notas.append(float(nota_nueva))
    calculo_nota=((notas[0]+notas[1]+notas[2])/3)
    nota_promedio.append(calculo_nota)
    notas=[]


for i in range(int(numero_estudiantes)):
    print(f"el estudiante {lista_estudiantes[i]} tiene una nota promedio de: {nota_promedio[i]}")

