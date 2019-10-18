import ply.lex as lex
import re
import codecs
import os
import sys

archivo = open ("tokens.txt", "w")
errores = open ("errores.txt", "w")


reservadas = ['BOOLEAN', 'FUNCTION', 'IF', 'INPUT', 'INT', 'PRINT', 'RETURN', 'STRING', 
				'VAR', 'WHILE'
		]

tokens = reservadas+['entero', 'cadena', 'id', 'asig', 'igual', 'coma', 'puntcoma', 'parentA', 
				'parentC', 'corcheteA', 'corcheteC', 'suma',  'or', 'menor'
		]


t_ignore = '\t '
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
		#reservadas.get(t.value,'ID')
		t.type = t.value

	return t

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)


def t_entero(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_comentario(t):
	r'/\*(.|\n)*?\*/'
	t.lexer.lineno += t.value.count('\n')
	pass

def t_cadena(t):
	r'("[^"]*")'
   	return t

def t_error(t):
	print "caracter ilegal '%s'" % t.value[0]
	print "linea '%s'" % t.lexer.lineno
	errores.write("Error del analizador lexico en la linea:" + str(t.lexer.lineno) + " Token ilegal: " + str(t.value[0]) + "\n")
	t.lexer.skip(1)


if len (sys.argv) != 2 :
    print "Hay que pasar 1 solo archivo"

test = sys.argv[1]

#test='/Users/Loreto/Documents/Universidad /Procesadores de lenguajes/Prueba/p.txt'
fp = codecs.open(test,"r","utf-8")
cadena = fp.read()
fp.close()

analizador = lex.lex()
analizador.input(cadena)


while True:
	tok = analizador.token()
	if not tok : break
	if (tok.type=='entero' or tok.type=='cadena' or tok.type=='id'):
		print ("<"+str(tok.type)+","+str(tok.value)+">"+"\n")
		archivo.write("<"+str(tok.type)+","+str(tok.value)+">"+"\n")
	else:
		print ("<"+str(tok.type)+","+ " >"+"\n")
		archivo.write("<"+str(tok.type)+","+ " >"+"\n")

archivo.close()
errores.close()
