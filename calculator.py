#Step 3
def calgotostring(strinput):
    strinput=strinput.replace("calc ","") 
    arrinput=strinput.split(" ")

    if arrinput[0]=="x":    
        return int(arrinput[1]) * int(arrinput[2])
    elif arrinput[0]=="+":    
        return int(arrinput[1]) + int(arrinput[2])
    elif arrinput[0]=="-":    
        return int(arrinput[1]) - int(arrinput[2])
    elif arrinput[0]=="/":    
        return int(arrinput[1]) / int(arrinput[2])

with open("calclistgoto.txt","r") as f:
    strline=f.read().splitlines()

totalvalue=0
lstcalc=[]
for line in strline: 
    
    if line.startswith("goto calc"):
       totalvalue=calgotostring(line.replace("goto calc ",""))
       if totalvalue in lstcalc:
            print(line)
            break
       lstcalc.append(totalvalue)            
    else:  
        subline=True  
        intline=int(line.replace("goto ",""))  
        if intline in lstcalc:
            print(line)
            break
        lstcalc.append(intline)
        """
        strlineloop=strline[intline]        
        while not strlineloop.startswith("goto calc"):
              intline=int(strlineloop.replace("goto ",""))  
              strlineloop=strline[intline] 
        totalvalue=totalvalue+calgotostring(strlineloop.replace("goto calc ",""))
        """
  

print(lstcalc)

exit()

#Step 2
def calstring(strinput):
    strinput=strinput.replace("calc ","") 
    arrinput=strinput.split(" ")

    if arrinput[0]=="x":    
        return int(arrinput[1]) * int(arrinput[2])
    elif arrinput[0]=="+":    
        return int(arrinput[1]) + int(arrinput[2])
    elif arrinput[0]=="-":    
        return int(arrinput[1]) - int(arrinput[2])
    elif arrinput[0]=="/":    
        return int(arrinput[1]) / int(arrinput[2])

with open("calclist.txt","r") as f:
    strline=f.read().splitlines()

totalvalue=0
for line in strline: 
    #print("Line{}: {}".format(count, line.strip())) 
   # print(line)
    totalvalue=totalvalue+calstring(line)

print(totalvalue)



#print(calstring("calc + 16 7"))
exit()

#Step 1
strinput=input("Please type in the 3 parameters to calculate ")
arrinput=strinput.split(",")

if arrinput[0]=="x":    
    print(int(arrinput[1]) * int(arrinput[2]))
elif arrinput[0]=="+":    
    print(int(arrinput[1]) + int(arrinput[2]))
elif arrinput[0]=="-":    
    print(int(arrinput[1]) - int(arrinput[2]))
elif arrinput[0]=="/":    
    print(int(arrinput[1]) / int(arrinput[2]))



"""
It should accept 3 pieces of input from the user: a string that's one of "x", "+", "
"--", or
"/" (an operation), an integer (parameter A), and another integer (parameter B).
If the user supplied "/", "5", "2", the application should output "2.5".
"""