def e2(): #Programa Caja Registradora
    from colorama import Style,init,Fore
    init()
    s=False
    subt=0
    t=0
    print(Style.BRIGHT+Style.RESET_ALL+Fore.GREEN)
    while(not s):
        cp=int(input("Insertar codigo del producto(10 digitos): "))
        if(cp > 9999999999):
            print("No ingreso correctamente el codigo del producto")
        if(cp < 1000000000 and cp > 1):
            print("No ingreso correctamente el codigo del producto")
        if(cp >= 1000000000 and cp <= 9999999999):
            pr=float(input("Insertar precio del producto: "))
            if(pr > 9999):
                print("Error al introducir el precio")
                return e2()
            if(pr < 0):
                print("Error al introducir el precio")
                return e2()
            alm=cp,pr
            subt=subt+pr
            print("----------------------------------")
            print(cp,pr)
            iv=subt*.15
            t=subt+iv
            print("Presiona 0 para salir")
        if(cp==0):
            print(Style.BRIGHT+Style.RESET_ALL+Fore.WHITE)
            print("el subtotal es: ",subt,"pesos")
            print(Style.BRIGHT+Style.RESET_ALL+Fore.YELLOW)
            print("el iva es del 16%: ",iv,"pesos")
            print(Style.BRIGHT+Style.RESET_ALL+Fore.RED)
            print("el total es: ",t,"pesos")
            s=True
e2()
input()