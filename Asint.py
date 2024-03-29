import ply.yacc as yacc
import os
import codecs
import re
from aLexSint import tokens
from sys import stdin
import sys


precedence= (
    ('right','PRINT','WHILE','IF', 'RETURN','INPUT'),
    ('right','FUNCTION'),
    ('left','corcheteA','corcheteC'),
    ('right','INT','BOOLEAN','STRING' ),
    ('right','VAR'),
    ('right','igual','asig'),
    ('left','or'),
    ('left','menor'),
    ('left','suma'),
    ('right','id','entero','cadena'),
    ('left','parentA','parentC'),
) 
# definimos que tokens tienen mayor prioridad 
# derecha o izquierda es por donde vamos a empezar analizar
# mayor prioridad esta al final 
#si estan en el mismo nivel asumo que tienen la misma preferencia 

def p_P (p):
    '''P : D P
         | F P
         | SC P
         | empty'''

def p_D (p):
    '''D : VAR T id puntcoma'''

def p_T (p):
    '''T : INT
         | STRING
         | BOOLEAN'''

def p_F (p):
    '''F : FUNCTION T1 id parentA A parentC corcheteA C corcheteC '''

def p_T1 (p):
    '''T1 : T 
          | empty '''

def p_A (p):
    '''A : empty
         | T id A1'''

def p_A1 (p):
    '''A1 : empty
          | coma T id A1''' 
        
def p_C (p):
    '''C : D C
         | SC'''

def p_S (p):
    '''S : id igual E puntcoma
         | id asig E puntcoma
         | PRINT parentA E parentC puntcoma
         | INPUT parentA E parentC puntcoma
         | id parentA L parentC puntcoma
         | RETURN X'''

def p_L (p):
    '''L : empty
         | id L1'''

def p_L1 (p):
    '''L1 : empty
         | coma id L1'''

def p_X (p):
    '''X : E
         | empty'''

def p_SC (p):
    '''SC : WHILE parentA E parentC corcheteA C corcheteC
          | IF parentA E parentC S
          | S '''

def p_E (p):
    '''E : E or G
         | G'''

def p_G (p):
    '''G : G menor U
         | U'''

def p_U (p):
    '''U : U suma V
         | V'''

def p_V (p):
    '''V : id
         | entero
         | cadena
         | parentA E parentC
         | id parentA L parentC'''

def p_empty(p):
	'''empty :'''
	pass

def p_error(p):
	print ("Error de sintaxis ", p.type)  
 

if len (sys.argv) != 2 :
	print ("Hay que pasar 1 solo archivo")
	sys.exit(1)

parser = yacc.yacc()
opened = open(sys.argv[1], "r")
content = opened.read()
opened.close()

for line in content.splitlines():
    print(parser.parse(line))

