import ply.lex as lex
import re
import codecs
import os
from sys import stdin

archivo = open ("tokens.txt", "w")
errores = open ("errores.txt", "w")

tablaSimbolos= {}
numID=1
#Esto es pa probar 
reservadas = ['BOOLEAN', 'FUNCTION', 'IF', 'INPUT', 'INT', 'PRINT', 'RETURN', 'STRING', 
				'VAR', 'WHILE'
		]

tokens = reservadas+['entero', 'cadena', 'id', 'asig', 'igual', 'coma', 'puntcoma', 'parentA', 
				'parentC', 'corcheteA', 'corcheteC', 'suma',  'or', 'menor'
		]


t_ignore = ' \t\r'
t_asig= r'&='
t_igual=r'='
t_coma=r','
t_puntcoma=r';'
t_parentA=r'\('
t_parentC=r'\)'
t_corcheteA=r'\{'
t_corcheteC=r'\}'

t_suma=r'\+'
t_or=r'\|\|'
t_menor= r'<'



def t_id(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	if t.value.upper() in reservadas:
		t.value = t.value.upper()
		t.type = t.value
	else:
		if (tablaSimbolos.get(t.value)==None):
			global numID
			tablaSimbolos[t.value]=numID
		#	t.value=numID
			numID+=numID
		#else:
			#t.value=tablaSimbolos.get(t.value)

	return t



def t_entero(t):
	r'\d+'
	t.value = int(t.value)
	if (t.value<=32767):
		return t
	else:
		errores.write("Error del analizador lexico en la linea:" + str(t.lexer.lineno) + " Entero mayor de 32767  "  + "\n")

def t_cadena(t):
	r'("[^"]*")'
	if ((len(t.value)-2)<64):
		return t
	else:
		errores.write("Error del analizador lexico en la linea:" + str(t.lexer.lineno) + " Cadena de longidud incorrecta  "  + "\n")

def t_comentario(t):
	r'/\*(.|\n)*?\*/'
	t.lexer.lineno += t.value.count('\n')
	pass

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)


def t_error(t):
	errores.write("Error del analizador lexico en la linea: " + str(t.lexer.lineno) + " Token ilegal: " + str(t.value) + "\n")
	t.lexer.skip(1)


if __name__=='__main__':
	if len (sys.argv) != 2 :
		print ("Hay que pasar 1 solo archivo")
		sys.exit(1)

	test = sys.argv[1]

	#test='/Users/Loreto/Documents/Universidad /Procesadores de lenguajes/Prueba/p.txt'
	fp = open(test,"r")
	#cadena = fp.read()

	lines = fp.readline()
	analizador = lex.lex()
	while lines != "":

		analizador.input(lines)
		lines= fp.readline()


		while True:
			tok = analizador.token()
			if not tok : break
			if (tok.type=='entero' or tok.type=='cadena' or tok.type=='id'):
				archivo.write("<"+str(tok.type)+","+str(tablaSimbolos.get(tok.value))+">"+"\n")
				print(tok.value)
			else:
				archivo.write("<"+str(tok.type)+","+ " >"+"\n")
				print(tok.value)

				
				
			
	fp.close()
	archivo.close()
	errores.close()
