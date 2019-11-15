import ply.yacc as yacc
import os
import codecs
import re
from analizadorLexico.py import tokens
from sys import stdin

precedence= (

) # definimos que tokens tienen mayor prioridad 
# derecha o izquierda es por donde vamos a empezar analizar
# mayor prioridad esta al final 
#si estan en el mismo nivel asimo que tienen la misma preferencia 

def p_program(p):
#la gramatica con la que lo definimos es bnf: terminales (tokens que hemos definido en el aLEx) y no terminales 
#no terminales aquellas que generan algo 
#los no terminales seran  los nombres de nuestras funciones 
#p es una produccion por ejemplo si tenemos '''program=block''' program esta en p[0] y block en p[1]
# p[0] = program(p[1],"program( nombre del nodo )") ej
# '''constDecl : empty'''	p[0] = Null() (supongo que asi sera con lamda)
# '''constDecl : CONST constAssignmentList SEMMICOLOM''' mayusculas tokens declarados, cambiar aLex
