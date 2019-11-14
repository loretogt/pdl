import ply.lex as lex
import re
import codecs
import os
import sys
from os import remove

archivo = open ("tokens.txt", "w")
errores = open ("errores.txt", "w")
ts= open("tabla_simbolos.txt","w")
tslocal= open("tslocal.txt","w")

tablaSimbolos= {}
tablaSimboloslocal={}
numID=1
numIDlocal=1
dec = False #saber si estamos en modo declaracion 
func= False  #si estamos declarando una funcion 
funcargs= False 
tLocal= False

tipo= 'entero'
desplaz=0
ndesplaz=0
nTabla=1

tipoparam=[]
nombrefun=None
tiporetorno=None
nparam=0


ts.write("TABLA PRINCIPAL #"+ str(nTabla) + '\n')
nTabla+=1

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

t_parentC=r'\)'

t_suma=r'\+'
t_or=r'\|\|'
t_menor= r'<'

def t_puntcoma(t):
	r';'
	declaracion= False
	return t

def t_parentA(t):
	r'\('
	global func, nTabla, tLocal, funcargs, nombrefun
	if func== True:
		tLocal=True
		tslocal.write("\n TABLA de la FUNCION "+ str(nombrefun) +" #"+ str(nTabla) + '\n')
		nombrefun=None
		nTabla+=1
		func=False
		funcargs=True
	return t
def t_corcheteA(t):
	r'\{'
	global funcargs
	funcargs= False
	return t
def t_corcheteC(t):
	r'\}'
	global tLocal, nparam, tiporetorno
	if tLocal==True: # Si nos encontamos dentro de la declaracion de una funcion salimos de ella, retornamos a la ts global
		#anadimos la informacion de la funcion 
		ts.write("+ numParam: "+ str(nparam) + '\n')
		for i in range(len(tipoparam)):
			ts.write("+ TipoParam"+ str(i)+ ": "+ str(tipoparam[i]) + '\n')
		ts.write("+ tiporetorno: "+ str(tiporetorno) + '\n')
		tLocal=False
		tiporetorno=None
		del tipoparam [:]
		tablaSimboloslocal.clear()
		numIDlocal=1
		nparam=0
	return t

def t_id(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	global dec, ndesplaz,numID, desplaz, tipo, func, tiporetorno,  nparam, tipoparam
	if t.value.upper() in reservadas:
		t.value = t.value.upper()
		if (t.value == 'VAR'): #entramos en asignacion	
			dec =True
		if (dec == True):
			if (t.value == 'BOOLEAN'):
				tipo ='logico'
				ndesplaz+=2
			elif(t.value== 'STRING'):
				tipo= 'cadena'
				ndesplaz+=128
			else:
				ndesplaz+=2
		if (func==True and t.value!='FUNCTION'):
			tiporetorno=tipo
		if (funcargs==True and (t.value == 'BOOLEAN' or t.value== 'STRING' or t.value== 'INT')):
			tipoparam.append(tipo)
			nparam+=1
		if (t.value=='FUNCTION'):
			func=True
			tipo= 'funcion'

		t.type = t.value
	else:
		if tLocal==True: #estamos dentro de la declaracion de funciones 
			if (tablaSimboloslocal.get(t.value)==None): #si la variable no esta en la tabla local 
				if (tablaSimbolos.get(t.value)==None): #miro si esta en la tabla global, sino esta la meto en la local 
					global numIDlocal
					tablaSimboloslocal[t.value]=numIDlocal
					val=t.value
					t.value=numIDlocal
					numIDlocal+=1
					tslocal.write("* LEXEMA: "+ str(val)+ '\n' + 
						"+tipo: " + str(tipo)+ '\n'+
						"+despl: "+ str(desplaz) +'\n' )

				else:
					t.value=tablaSimbolos.get(t.value)
			else:
				t.value=tablaSimboloslocal.get(t.value)

			
		else: #estamos en la tabla global 
			if (func==True):
				nombrefun = t.value
			if (tablaSimbolos.get(t.value)==None):
				tablaSimbolos[t.value]=numID
				val=t.value
				t.value=numID
				numID+=1
				if (func == True):
					ts.write("* LEXEMA: "+ str(val)+ '\n' + 
						"+tipo: " + str(tipo)+ '\n' )
				else:
					ts.write("* LEXEMA: "+ str(val)+ '\n' + 
						"+tipo:" + str(tipo)+ '\n'+
						"+despl: "+ str(desplaz) +'\n' )
				
				dec= False #volvemos a los valores por defecto
				tipo='entero' 
				desplaz=ndesplaz
			else:
				t.value=tablaSimbolos.get(t.value)

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
	#print "caracter ilegal '%s'" % t.value[0]
	#print "linea '%s'" % t.lexer.lineno
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
		#print ("<"+str(tok.type)+","+str(tok.value)+">"+"\n")
		archivo.write("<"+str(tok.type)+","+str(tok.value)+">"+"\n")
	else:
		#print ("<"+str(tok.type)+","+ " >"+"\n")
		archivo.write("<"+str(tok.type)+","+ " >"+"\n")


tslocal.close()
tslocal= open("tslocal.txt","r") #concatenamos el fichero que contien las ts locales con la global y eliminamos el local 
for i in tslocal:
	ts.write(i)
remove("tslocal.txt")
tslocal.close()
archivo.close()
errores.close()
ts.close()