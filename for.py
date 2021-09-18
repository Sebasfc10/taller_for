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

        
    