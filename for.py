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
    
