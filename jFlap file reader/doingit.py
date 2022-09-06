from pickle import TRUE
from xml.dom import minidom
#we make this class to have objects which have all the atributes we need for each transition and state
class transition: 
    def __init__(self,t):
        self.fro = t.getElementsByTagName("from")[0].firstChild.data
        self.to =  t.getElementsByTagName("to")[0].firstChild.data
        self.read = t.getElementsByTagName("read")[0].firstChild.data 


        

# here we put the xml or jff file hehe
file = minidom.parse('automaton_leo.jff')

#use getElementsByTagName() to get tag
states = file.getElementsByTagName('state') 
size=len(states)  
transitions=file.getElementsByTagName('transition') 
transElements=[]  
for t in transitions:  
    newClass=transition(t) 
    transElements.append(newClass) 

mainDic={} 
froDic={} 
for i in transElements: #here we create a dictionary of all the transitions each transition has an array of allowed values, we also create a from dictionary to save all the froms and see that if they have regressions,whats the next state they can leave to  
    key = str(i.fro) + "_" + str(i.to)  
    if key in mainDic.keys(): 
        mainDic[key].append(i.read)  
        froDic[int(i.fro)].add(int(i.to))
    else: 
        mainDic[key]=[] 
        mainDic[key].append(i.read)   
        froDic[int(i.fro)]=set()
        froDic[int(i.fro)].add(int(i.to)) 
mainDic=dict(sorted(mainDic.items())) #sorting the dic by key 
print(mainDic)
print(froDic) 

#transform the key in a tupple of the (fro,to) from bewing the from from the file
def numberfy(key): 
    splitted=key.split("_") 
    fro=int(splitted[0]) 
    to=int(splitted[1]) 
    return (fro,to)

def doingit(userInput,adder=0,mainDic=mainDic): 
    failed=False 
    for i in mainDic.keys(): #going through all keys
        splitted=i.split("_") 
        fro=int(splitted[0]) 
        to=int(splitted[1])  
        sub=to-fro  
        a=0 
        if fro > len(userInput)-1: #if the input has a smaller size than the number of states it will get the highest
            fro=len(userInput)-1
        if sub == 1:   #if its a regular sequencial state change ex: q1 -> q1
            if fro+adder < len(userInput):
                if userInput[fro+adder] not in mainDic[i]: #checking if the current character in the userinput its in the array of the state its being tested at, the added is for ajusting after a regression 
                    failed=True 
                    break; 
            else: 
                if userInput[fro] not in mainDic[i]: 
                    failed=True 
                    break; 
        elif sub == 0 :  #if its a regression to the same state ex: q1 -> q1
            if fro == 0: 
                failed=True 
                break
            subfail=False   
            while fro+(adder+a) < len(userInput):  
                hasFuture=False #both hasfuture and doesnot are to check if the char in the word is just another of the regression type [in that case it will run the regression with an incremented adder to get to next char of the userInput] 
                doesnot=False   #or if it has the input to move to the next state if so the adder isnt incremented and the next state can occur, then on the next state. due to the adder not being incremented the next state will check the char correctly
                if userInput[fro+adder] not in mainDic[i]: # checking if it is in the regression array or not
                    if len(froDic[fro]) == 1: 
                        subfail = True 
                        break   
                    else:  
                        doesnot=True;
                        newkeys=[]  # keeps all the keys that have the same from so to check if it can leave the regression and go to thje next state
                        for j in froDic[fro]: 
                            if j != to:  
                                newkey=str(fro) +"_" +str(j)
                                newkeys.append(newkey) 
                        for j in newkeys: 
                            if userInput[fro+(adder-a)] in mainDic[j]:  
                                doesnot=False
                                hasFuture=True
                                break;  
                if not hasFuture and not doesnot:
                    adder +=1 
                elif doesnot: 
                    subfail=True 
                    break; 
                else: 
                    break
            if subfail: 
                failed=True 
                break; 
        else:  #if its an state skip of more than 1(regression or skip) exp: q3 -> q1, q1 -> q4
            if fro+adder > len(userInput)-1: #ajusting for smaller values 
                a=adder
            if userInput[fro+(adder-a)] in mainDic[i]: 
                if fro > to: 
                    #going to a previous state 
                    newDic={}  
                    for j in mainDic.keys(): 
                        currentFro=numberfy(j)[0]
                        if currentFro >= to: 
                            newDic[j] = mainDic[j] 
                    return doingit(userInput,adder+fro,newDic)

                else: 
                    #going to a future state
                    newDic={}  
                    for j in mainDic.keys(): 
                        currentFro=numberfy(j)[0]
                        if currentFro >= to: 
                            newDic[j] = mainDic[j] 
                    return doingit(userInput,adder+fro,newDic) 
        print("got through step ", i)
    if failed: 
        return "the sequence is not on the desired format"  
    if fro + adder < len(userInput)-1: 
        return "the sequence is not on the desired format"
    return "that sequence is on the desired format" 

while True: 
    userInput=input("type the combination to see if its in accordance with the jff file read,type p to exit \n")
    if userInput.lower() == 'p' : 
        break  
    if len(userInput) < size-1: 
        print("sequence is not on the desired format")  
        continue 
    print(doingit(userInput))





