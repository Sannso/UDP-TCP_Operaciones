def menu():
    print("Que operacion desea realizar\n\n"+
    "Para suma: 1"+"\n"+
    "Para resta: 2"+"\n"+
    "Para multipicacion: 3"+"\n"+
    "Para division: 4"+"\n"+
    "Para potenciacion: 5"+"\n"+
    "Para logaritmacion: 6"+"\n"+
    "\n")

    selection = input("Ingrese aqui su opcion: ")

    if(selection.isalnum() and selection >0 and selection <7):
        return selection
    
    else: 
        menu()

