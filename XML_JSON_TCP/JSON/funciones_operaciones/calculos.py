import re
import math as m

def suma(op, id = "suma"):
    error = False
    error2 = 0
    num1 = ""
    num2 = ""
    set_ = True 

    for a in op:
        if(a == "+" or a == "-" or a == "*" or a == "/" or a == "x" or a == "^"):
            set_ = False
            error2 += 1 
        
        elif(a.isalpha()):
            error = True
            break
        
        elif(set_):
            num1 += a
        
        elif not set_:
            num2 += a
    
    if(len(num1) == 0 or len(num2) == 0 or error or error2 > 1):
        print("num: ", num1, num2)
        return {"operacion":"Operacion no valida"}

    if(id == "suma"):
        return {"operacion":(str(int(num1) + int(num2)))}
    
    elif(id == "res"):
        return {"operacion":(str(int(num1) - int(num2)))}
    
    elif(id == "mul"):
        return {"operacion":(str(int(num1) * int(num2)))}

    elif(id == "div"):
        return {"operacion":(str(int(num1) / int(num2)))}
    
    elif(id == "pot"):
        return {"operacion":(str(int(num1) ** int(num2)))}
    

def resta(op):
    return suma(op, "res")

def multiplicacion(op):
    return suma(op, "mul")

def division(op):
    return suma(op, "div")

def potencia(op):
    return suma(op, "pot")

def log(op):
    formC = re.compile(r'l[(](\d+)[)]')
    formC2 = re.compile(r'log[(](\d+)[)]')

    if formC.match(op) or formC2.match(op):
        numero = re.search(r'(\d+)', op).group()
    else:
        return {"operacion":"Operacion no valida"} 

    return {"operacion":(str(m.log(int(numero),10)))}