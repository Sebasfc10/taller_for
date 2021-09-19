# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 15:59:40 2021

@author: jeha2
"""
"""
. El departamento de Seguridad de Transito de Barranquilla, desea saber de
los n autos que entrar a la ciudad, cuantos entran con calcomanía de cada
color. Conociendo el último digito de la placa de cada automóvil se puede
determinar el color de la calcomanía utilizando la siguiente relación:
"""
c = int(input('Ingrese su digito: '))

if c == 1 or c==2:
    print('es amarillo')
if c==3 or c==4:
    print('es rosa')
if c==5 or c==5:
    print('es rojo')
if c==7 or c==8:
    print('es verde')
if c==9 or c==0:
    print('es azul')
    
"""
Un Zoólogo pretende determinar el porcentaje de animales que hay en las
siguiente categorias de edades: 0 a 1 año, de mas de 1 año y menos de 3 y
de 3 o mas años. El zoológico todavía no está seguro del animal que va
estudiar. Si se decide por elefantes solo tomará una muestra de 20 de ellos;
si se decide por jirafas, tomara 15 de muestras y si son chompancés tomará
40.
"""
animal = str(input('Cual animal ingresara? elefante? jirafa? chimpance?: '))
edad = int(input('Ingrese el rango de edad: 0 a 1 año, mas de 1 año y menos de 3 años y de 3 o mas años: '))
p1 = 0
p2 = 0
p3 = 0
if animal == 'elefante':
    if edad >= 0 and edad <= 1:
        p1 = p1 + 1
    if edad > 1 and edad < 3:
        p2 = p2 + 1
    if edad > 3:
        p3 = p3 + 1
    print(f'su promedio es: {(p1/40)*100}')
if animal == 'jirafa':
    if edad >= 0 and edad <= 1:
        p1 = p1 + 1
    if edad > 1 and edad < 3:
        p2 = p2 + 1
    if edad > 3:
        p3 = p3 + 1
    print(f'su promedio es: {(p1/15)*100}')
if animal == 'chimpance':
    if edad >= 0 and edad <= 1:
        p1 = p1 + 1
    if edad > 1 and edad < 3:
        p2 = p2 + 1
    if edad > 3:
        p3 = p3 + 1
    print(f'su promedio es: {(p1/40)*100}')

"""
Una empresa se requiere calcular el salario semanal de cada uno de los n
obreros que laboran en ella. El salario se obtiene de la siguiente forma:
a. Si el obrero trabaja 40 horas o menos se le paga $20 por hora
b. Si trabaja mas de 40 horas se le paga $20 por cada una de
lasprimeras 40 horas y $25 por cada hora extra.
"""

trb = int(input('ingrese el numero de trabajadores: '))
x = 1
while x <= trb:
    h = float(input('escribe el numero de horas: '))
    if h <= 40:
        salario= h * 20
    else:
        he = h - 40
        salario = 40 * 20 + (he * 25)
    print(f'el salario del trabajador {x} es :${salario}')
    x = x + 1

"""
Calcular el promedio de edades de hombres, mujeres y de todo un grupo
de alumnos.
"""

a = int(input('ingresa el numero de alumnos: '))
x = 1
s = 0
while x <= a:
    e = int(input('ingresa tu edad: '))
    s = s + e
    x = x + 1
print(f'el promedio de edades de todo el salon es de : {s/x}')

"""
Encontrar el menor valor de un conjunto de n números dados
"""
    
n = int(input('ingresa el total de numeros a calcular: '))
x = 1
while x  <= n:
    m = int(input('escribe un numero: '))
    if x == 1:
        nm = m
    else:
        if m < nm:
            nm = m
    x = x + 1
    print(f'el numero menor es: {nm}')
    
"""
Cinco miembros de un club contra la obesidad desean saber cuanto han
bajado o subido de peso desde la última vez que se reunieron. Para esto se
debe realizar un ritual de pesaje en donde cada uno se pesa en diez
básculas distintas para así tener el pormedio mas exacto de su peso. si existe diferencia positiva entre este promedio de peso y el peso de la última
vez que se reunieron, significa que subieron de peso. Pero si la diferencia
es negativa, significa que bajaron. Lo que el problema requere es que por
cada persona se imprima un letrero que diga: “SUBIÓ” o “BAJÓ” y la
cantidad de kilos que subió o bajó de peso.
"""
x = 0
z = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = 0
for x in z:
    print(f'persona {x}')
    w = input('ingrese tu peso anterior: ')
    suma = 0
    for a in y:
        peso = input('ingresa el peso:')
        suma = suma + peso
    if suma / 10 == w:
        print(f'la persona {x}, se mantiene en el peso')
    else:
        if suma / 10 > w:
            print(f'la persona {x}, subio')
        else:
            print(f'la persona {x}, bajo')
    print(" ")
    
    
    
    
