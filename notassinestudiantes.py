lista_estudiantes=[]
notas=[]
nota_promedio=[]
n=""
o=0
#numero_estudiantes=input("Cuantos estudiantes quiere ingresar: ")

while n !="salir":
    n=input(f"introduzca el nombre del estudiante numero {o} de la lista: ")
    o+=1
    if n!="salir":
        lista_estudiantes.append((n))
        for a in range (3):
            nota_nueva=input(f"Introduzca la nota numero {a+1} del estudiante {lista_estudiantes[o-1]}: ")
            notas.append(float(nota_nueva))
        calculo_nota=((notas[0]+notas[1]+notas[2])/3)
        nota_promedio.append(calculo_nota)
        notas=[]


for i in range(len(lista_estudiantes)):
    print(f"el estudiante {lista_estudiantes[i]} tiene una nota promedio de: {nota_promedio[i]}")