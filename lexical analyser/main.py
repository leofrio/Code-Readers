from turtle import goto
from unittest import result 
import types
import pdb
import string 
class State: 
  def __init__(self,stateId):
      self.stateId=stateId 
      self.rule=None 

  def start(self,uInput,pos,loc): 
    return states["E1"].get_rule().execute(uInput,pos,loc)
  def add_rule(self,ruleString): 
    self.rule=Rule(self.stateId,ruleString)   
  def get_rule(self): 
    return self.rule
  def __str__(self): 
    return "stateId:{} rule: {}".format(self.stateId,self.rule)    
  def __repr__(self) -> str:
    return "stateId:{} rule: {}".format(self.stateId,self.rule)  

class Rule: 
  def __init__(self,stateId,ruleString) :
    self.stateId=stateId  
    self.ruleString=ruleString 
    self.loc={"collected":[],"counter":0} 
    self.rule=None
  def execute (self,uInput,pos,loc): 
    self.loc.update({"uInput":uInput ,"pos":pos})
    self.loc.update(loc)  
    self.loc.update({"loc":self.loc,"generic_rule":Rule(self.stateId,"generic rule")})   
    exec(open(self.ruleString).read(),globals(),self.loc)    
    return self.loc["pos"],self.loc
  def goTo(self,stateId,uInput,pos,loc): 
    return states[stateId].get_rule().execute(uInput,pos,loc)
    

  def __str__(self):
    return self.ruleString  
#print(State("a",[]))
states={}
for i in range(0,7):
  idName="E%d" % (i+1)    
  currentState=State(idName)
  states[idName]=currentState
  #print(currentState) 

#settings values 
numbers=list(range(0,10)) 
for i in range(0,10): 
    numbers[i]=str(numbers[i])
letters=list(string.ascii_letters)
reservedWords=["END","LET","GO","TO","OF","READ","PRINT","IF","THEN","ELSE"]   

signs=[";",":","+","*","/","(","..",">","=","<"]
phraseSigns=[":=","GO TO"]

#starting rules
#E1
E1=states["E1"] 
E1.add_rule("./rules/E1.py")
states["E1"]=E1

#E2   
E2=states["E2"]
E2.add_rule("./rules/E2.py")
states["E2"]=E2

#E3  
E3=states["E3"] 
E3.add_rule("./rules/E3.py")
states["E3"]=E3

#E4  
E4=states["E4"]
E4.add_rule("./rules/E4.py")
states["E4"]=E4

#E5 
E5=states["E5"]
E5.add_rule("./rules/E5.py")
states["E5"]=E5

#E6  
E6=states["E6"]
E6.add_rule("./rules/E6.py")
states["E6"]=E6

#E7 

E7=states["E7"]
E7.add_rule("./rules/E7.py")
states["E7"]=E7

#end of setting rules 

#starting program  

uInput=input("please type expression to be evaluated \n")
pos=0 
E1.start(uInput,pos,E1.get_rule().loc)


#if(uInput[pos])

""" f='''
a=5 
b=6 
c=7 
d=[]  
e=[a,b,c]
for i  in e: 
  d.append(i)
print(d)'''
loc={}
print(f)
exec(f,globals(),loc) 
print(loc)
#numbers = [2, 3, 7, 4, 8]
#exec("result = sum(number**2 for number in numbers if number % 2 == 0) \nprint(result)")  """