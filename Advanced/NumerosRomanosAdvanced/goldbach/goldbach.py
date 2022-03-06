

import time
import os
import random


def primo(n:int)->list:
    value=True
    count=0
    for i in range(1,n+1):
        
        if n%i==0:  
            count+=1
            
        if count>2:
            value=False
            break
            
    return value
    
    
    
def primos(n:int)->list:
    lista=[]
    for i in range(1,n+1):
        num=primo(i)
        
        if num:
            lista.append(i)
            
            
    return(lista)
        
        
        

def goldbach(n:int):
    
    lista=primos(n)
    
    
    text=""
    
    second=[]
    
    value=True
    for i in range(len(lista)):
        
        if value:
            for j in range(len(lista)):
                
            
                if (lista[i]+lista[j])==n:
                    
                    
                    val1=[lista[i],lista[j]]
                    val2=[lista[j],lista[i]]
                    
                    
                    
                    if val1 not in second and val2 not in second:
                        second.append(val1)
                        text+=str(lista[i])+"+"+str(lista[j])+"="+str(n)+"\n"
                    else:
                        value=False
                        
                        
        else:
            break
                
    
    #print(text)
    
    return text



def text_rute(n:int,type_in)->str:
    text=str(n)

    long=len(text)

    text1=type_in+(3-long)*"0"+text+".text"
    
    return text1


def par():
    n=random.randint(2,10000)
    
    while n%2!=0:
        n=random.randint(2,10000)
        
    return n
    

def cases():

    

    
    for i in range(0,2):
        
        
        n=par()
        
        textinput=text_rute(i,"input")
        textoutput=text_rute(i,"output")

    
    
    
    
        #init=time.time()  
        text= goldbach(n) 

        #fin=time.time()

        #print(fin-init)

        print(text)
        
        """
        fileinput = open(textinput, "w")
        fileinput.write(str(n))
        fileinput.close()
        
        fileoutput = open(textoutput, "w")
        fileoutput.write(text)
        fileoutput.close()
        
        """
        
cases()