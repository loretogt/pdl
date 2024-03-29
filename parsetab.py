
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightPRINTWHILEIFRETURNINPUTrightFUNCTIONleftcorcheteAcorcheteCrightINTBOOLEANSTRINGrightVARrightigualasigleftorleftmenorleftsumarightidenterocadenaleftparentAparentCBOOLEAN FUNCTION IF INPUT INT PRINT RETURN STRING VAR WHILE asig cadena coma corcheteA corcheteC entero id igual menor or parentA parentC puntcoma sumaP : D P\n         | F P\n         | SC P\n         | emptyD : VAR T id puntcomaT : INT\n         | STRING\n         | BOOLEANF : FUNCTION T1 id parentA A parentC corcheteA C corcheteC T1 : T \n          | empty A : empty\n         | T id A1A1 : empty\n          | coma T id A1C : D C\n         | SCS : id igual E puntcoma\n         | id asig E puntcoma\n         | PRINT parentA E parentC puntcoma\n         | INPUT parentA E parentC puntcoma\n         | id parentA L parentC puntcoma\n         | RETURN XL : empty\n         | id L1L1 : empty\n         | coma id L1X : E\n         | emptySC : WHILE parentA E parentC corcheteA C corcheteC\n          | IF parentA E parentC S\n          | S E : E or G\n         | GG : G menor U\n         | UU : U suma V\n         | VV : id\n         | entero\n         | cadena\n         | parentA E parentC\n         | id parentA L parentCempty :'
    
_lr_action_items = {'RETURN':([0,3,7,8,10,14,18,19,20,21,22,23,24,25,26,60,61,63,64,69,70,72,74,75,76,77,78,83,84,86,91,93,99,],[3,-44,3,3,-32,3,-34,-39,-41,-36,-38,-23,-28,-29,-40,-42,-35,-37,-33,-19,-18,-5,3,3,-20,-43,-22,-21,-31,3,-30,3,-9,]),'parentA':([1,2,3,4,12,13,15,16,17,19,28,29,39,40,45,47,48,54,],[15,16,17,27,39,40,17,17,17,46,17,17,17,17,17,17,17,71,]),'corcheteA':([58,89,],[75,93,]),'corcheteC':([3,10,18,19,20,21,22,23,24,25,26,60,61,63,64,69,70,76,77,78,83,84,85,87,91,92,97,],[-44,-32,-34,-39,-41,-36,-38,-23,-28,-29,-40,-42,-35,-37,-33,-19,-18,-20,-43,-22,-21,-31,91,-17,-30,-16,99,]),'coma':([50,79,90,100,],[66,66,95,95,]),'menor':([18,19,20,21,22,26,60,61,63,64,77,],[45,-39,-41,-36,-38,-40,-42,-35,-37,45,-43,]),'PRINT':([0,3,7,8,10,14,18,19,20,21,22,23,24,25,26,60,61,63,64,69,70,72,74,75,76,77,78,83,84,86,91,93,99,],[2,-44,2,2,-32,2,-34,-39,-41,-36,-38,-23,-28,-29,-40,-42,-35,-37,-33,-19,-18,-5,2,2,-20,-43,-22,-21,-31,2,-30,2,-9,]),'parentC':([18,19,20,21,22,26,27,42,43,44,46,49,50,51,56,57,60,61,62,63,64,67,68,71,77,79,80,82,88,90,94,96,100,101,],[-34,-39,-41,-36,-38,-40,-44,58,59,60,-44,65,-44,-24,73,74,-42,-35,77,-37,-33,-26,-25,-44,-43,-44,89,-12,-27,-44,-13,-14,-44,-15,]),'id':([0,3,6,7,8,10,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,38,39,40,45,46,47,48,60,61,63,64,66,69,70,72,74,75,76,77,78,81,83,84,86,91,93,98,99,],[4,19,-44,4,4,-32,4,19,19,19,-34,-39,-41,-36,-38,-23,-28,-29,-40,50,19,19,-7,-6,54,-8,-10,-11,55,19,19,19,50,19,19,-42,-35,-37,-33,79,-19,-18,-5,4,4,-20,-43,-22,90,-21,-31,4,-30,4,100,-9,]),'puntcoma':([18,19,20,21,22,26,52,53,55,59,60,61,63,64,65,73,77,],[-34,-39,-41,-36,-38,-40,69,70,72,76,-42,-35,-37,-33,78,83,-43,]),'asig':([4,],[28,]),'igual':([4,],[29,]),'entero':([3,15,16,17,28,29,39,40,45,47,48,],[26,26,26,26,26,26,26,26,26,26,26,]),'FUNCTION':([0,3,7,8,10,14,18,19,20,21,22,23,24,25,26,60,61,63,64,69,70,72,76,77,78,83,84,91,99,],[6,-44,6,6,-32,6,-34,-39,-41,-36,-38,-23,-28,-29,-40,-42,-35,-37,-33,-19,-18,-5,-20,-43,-22,-21,-31,-30,-9,]),'STRING':([6,11,71,95,],[30,30,30,30,]),'VAR':([0,3,7,8,10,14,18,19,20,21,22,23,24,25,26,60,61,63,64,69,70,72,75,76,77,78,83,84,86,91,93,99,],[11,-44,11,11,-32,11,-34,-39,-41,-36,-38,-23,-28,-29,-40,-42,-35,-37,-33,-19,-18,-5,11,-20,-43,-22,-21,-31,11,-30,11,-9,]),'INPUT':([0,3,7,8,10,14,18,19,20,21,22,23,24,25,26,60,61,63,64,69,70,72,74,75,76,77,78,83,84,86,91,93,99,],[12,-44,12,12,-32,12,-34,-39,-41,-36,-38,-23,-28,-29,-40,-42,-35,-37,-33,-19,-18,-5,12,12,-20,-43,-22,-21,-31,12,-30,12,-9,]),'suma':([19,20,21,22,26,60,61,63,77,],[-39,-41,47,-38,-40,-42,47,-37,-43,]),'IF':([0,3,7,8,10,14,18,19,20,21,22,23,24,25,26,60,61,63,64,69,70,72,75,76,77,78,83,84,86,91,93,99,],[13,-44,13,13,-32,13,-34,-39,-41,-36,-38,-23,-28,-29,-40,-42,-35,-37,-33,-19,-18,-5,13,-20,-43,-22,-21,-31,13,-30,13,-9,]),'INT':([6,11,71,95,],[31,31,31,31,]),'WHILE':([0,3,7,8,10,14,18,19,20,21,22,23,24,25,26,60,61,63,64,69,70,72,75,76,77,78,83,84,86,91,93,99,],[1,-44,1,1,-32,1,-34,-39,-41,-36,-38,-23,-28,-29,-40,-42,-35,-37,-33,-19,-18,-5,1,-20,-43,-22,-21,-31,1,-30,1,-9,]),'cadena':([3,15,16,17,28,29,39,40,45,47,48,],[20,20,20,20,20,20,20,20,20,20,20,]),'BOOLEAN':([6,11,71,95,],[33,33,33,33,]),'$end':([0,3,5,7,8,9,10,14,18,19,20,21,22,23,24,25,26,36,37,41,60,61,63,64,69,70,72,76,77,78,83,84,91,99,],[-44,-44,-4,-44,-44,0,-32,-44,-34,-39,-41,-36,-38,-23,-28,-29,-40,-1,-2,-3,-42,-35,-37,-33,-19,-18,-5,-20,-43,-22,-21,-31,-30,-9,]),'or':([18,19,20,21,22,24,26,42,43,44,52,53,56,57,60,61,63,64,77,],[-34,-39,-41,-36,-38,48,-40,48,48,48,48,48,48,48,-42,-35,-37,-33,-43,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'A':([71,],[80,]),'C':([75,86,93,],[85,92,97,]),'E':([3,15,16,17,28,29,39,40,],[24,42,43,44,52,53,56,57,]),'D':([0,7,8,14,75,86,93,],[7,7,7,7,86,86,86,]),'G':([3,15,16,17,28,29,39,40,48,],[18,18,18,18,18,18,18,18,64,]),'F':([0,7,8,14,],[8,8,8,8,]),'L1':([50,79,],[68,88,]),'L':([27,46,],[49,62,]),'T1':([6,],[32,]),'A1':([90,100,],[94,101,]),'P':([0,7,8,14,],[9,36,37,41,]),'S':([0,7,8,14,74,75,86,93,],[10,10,10,10,84,10,10,10,]),'U':([3,15,16,17,28,29,39,40,45,48,],[21,21,21,21,21,21,21,21,61,21,]),'T':([6,11,71,95,],[34,38,81,98,]),'V':([3,15,16,17,28,29,39,40,45,47,48,],[22,22,22,22,22,22,22,22,22,63,22,]),'SC':([0,7,8,14,75,86,93,],[14,14,14,14,87,87,87,]),'X':([3,],[23,]),'empty':([0,3,6,7,8,14,27,46,50,71,79,90,100,],[5,25,35,5,5,5,51,51,67,82,67,96,96,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> P","S'",1,None,None,None),
  ('P -> D P','P',2,'p_P','Asint.py',29),
  ('P -> F P','P',2,'p_P','Asint.py',30),
  ('P -> SC P','P',2,'p_P','Asint.py',31),
  ('P -> empty','P',1,'p_P','Asint.py',32),
  ('D -> VAR T id puntcoma','D',4,'p_D','Asint.py',35),
  ('T -> INT','T',1,'p_T','Asint.py',38),
  ('T -> STRING','T',1,'p_T','Asint.py',39),
  ('T -> BOOLEAN','T',1,'p_T','Asint.py',40),
  ('F -> FUNCTION T1 id parentA A parentC corcheteA C corcheteC','F',9,'p_F','Asint.py',43),
  ('T1 -> T','T1',1,'p_T1','Asint.py',46),
  ('T1 -> empty','T1',1,'p_T1','Asint.py',47),
  ('A -> empty','A',1,'p_A','Asint.py',50),
  ('A -> T id A1','A',3,'p_A','Asint.py',51),
  ('A1 -> empty','A1',1,'p_A1','Asint.py',54),
  ('A1 -> coma T id A1','A1',4,'p_A1','Asint.py',55),
  ('C -> D C','C',2,'p_C','Asint.py',58),
  ('C -> SC','C',1,'p_C','Asint.py',59),
  ('S -> id igual E puntcoma','S',4,'p_S','Asint.py',62),
  ('S -> id asig E puntcoma','S',4,'p_S','Asint.py',63),
  ('S -> PRINT parentA E parentC puntcoma','S',5,'p_S','Asint.py',64),
  ('S -> INPUT parentA E parentC puntcoma','S',5,'p_S','Asint.py',65),
  ('S -> id parentA L parentC puntcoma','S',5,'p_S','Asint.py',66),
  ('S -> RETURN X','S',2,'p_S','Asint.py',67),
  ('L -> empty','L',1,'p_L','Asint.py',70),
  ('L -> id L1','L',2,'p_L','Asint.py',71),
  ('L1 -> empty','L1',1,'p_L1','Asint.py',74),
  ('L1 -> coma id L1','L1',3,'p_L1','Asint.py',75),
  ('X -> E','X',1,'p_X','Asint.py',78),
  ('X -> empty','X',1,'p_X','Asint.py',79),
  ('SC -> WHILE parentA E parentC corcheteA C corcheteC','SC',7,'p_SC','Asint.py',82),
  ('SC -> IF parentA E parentC S','SC',5,'p_SC','Asint.py',83),
  ('SC -> S','SC',1,'p_SC','Asint.py',84),
  ('E -> E or G','E',3,'p_E','Asint.py',87),
  ('E -> G','E',1,'p_E','Asint.py',88),
  ('G -> G menor U','G',3,'p_G','Asint.py',91),
  ('G -> U','G',1,'p_G','Asint.py',92),
  ('U -> U suma V','U',3,'p_U','Asint.py',95),
  ('U -> V','U',1,'p_U','Asint.py',96),
  ('V -> id','V',1,'p_V','Asint.py',99),
  ('V -> entero','V',1,'p_V','Asint.py',100),
  ('V -> cadena','V',1,'p_V','Asint.py',101),
  ('V -> parentA E parentC','V',3,'p_V','Asint.py',102),
  ('V -> id parentA L parentC','V',4,'p_V','Asint.py',103),
  ('empty -> <empty>','empty',0,'p_empty','Asint.py',106),
]
