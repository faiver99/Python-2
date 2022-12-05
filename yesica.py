import math
import os

def menu():
    os.system("clear")
    print("""
       Panel de Control 
           Elija el numero del ejercicio que desea revisar.
           1) Ejercicio 1
           2) Ejercicio 2
           3) Ejercicio 3
           4) Ejercicio 4
           5) Ejercicio 5
           6) Ejercicio 6
           7) Ejercicio 7
           8) Ejercicio 8
           9) Ejercicio 9
           10) Ejercicio 10
           11) Ejercicio 11
           12) Ejercicio 12
           13) Salir. 
    """)

    
entrada=True
while(entrada):
    menu()
    opc=float(input("Ingresa una Opcion: "))

    if opc==1:
       lado=int(input("Ingrese la longitud de los lados :"))
       perimetro=(lado+lado+lado+lado+lado+lado)
       print("El perimetro de la figura es :", perimetro)

    if opc==2:
        # ejercicio 2

        valorHora=1000
        horasTrabajas1=int(input("Ingrese las horas trabajadas por el trabajador 1 :"))
        horasTrabajas2=int(input("Ingrese las horas trabajadas por el trabajador 2 :"))
        horasTrabajas3=int(input("Ingrese las horas trabajadas por el trabajador 3 :"))
        horasTrabajas4=int(input("Ingrese las horas trabajadas por el trabajador 4 :"))
        horasTrabajas5=int(input("Ingrese las horas trabajadas por el trabajador 5 :"))
        totalHoras=horasTrabajas1+horasTrabajas2+horasTrabajas3+horasTrabajas4+horasTrabajas5

        valorPagoIndividual1=horasTrabajas1*valorHora
        valorPagoIndividual2=horasTrabajas2*valorHora
        valorPagoIndividual3=horasTrabajas3*valorHora
        valorPagoIndividual4=horasTrabajas4*valorHora
        valorPagoIndividual5=horasTrabajas5*valorHora

        print("Pago obrero 1 =", valorPagoIndividual1)
        print("Pago obrero 2 =", valorPagoIndividual2)
        print("Pago obrero 3 =", valorPagoIndividual3)
        print("Pago obrero 4 =", valorPagoIndividual4)
        print("Pago obrero 5 =", valorPagoIndividual5)


        totalPago=totalHoras*valorHora
        print("Total pago de nomina =",totalPago)


    if opc==3:
        # ejercicio 3
        print("nada")

    if opc==4:
        # ejercicio 4
        numeroDecadas=int(input("Ingrese el numero de decadas que desea pasar a Dias :"))
        dias=365
        numeroDias=numeroDecadas*10*dias

        print("El numero de dias al que equivalen", numeroDecadas, "decadas es =", numeroDias)

    if opc==5:
        #ejercicio 5
        presion=int(input("Ingrese la presion :"))
        volumen=int(input("Ingrese el Volumen :"))
        temperatura=int(input("Ingrese la tempretura :"))
        masa=(presion*volumen)/(0.37*(temperatura+460))
        print("la masa es :", masa)

    if opc==6:
        #ejercicio 6
        edad=int(input("Ingrese la edad :"))
        pulsaciones=(220-edad)/10
        print("El numero de pulsaciones por cada 10 segundos es :", pulsaciones)

    if opc==7:
        #ejercicio 7 Convertir Farenheit a Centigrados
        farenheit=int(input("Ingrese grados farenheit a pasar a grados Centigrados :"))
        centigrados=(5/9)*(farenheit-32)
        print("El equivalente en grados centigrados es :", centigrados)
    if opc==8:
        #ejercicio 8 Convertir Centigrados a Farenheit
        centigrado=int(input("Ingrese grados centigrados pasar a grados farenheit :"))
        farenhey=(9/5)*centigrados+32
        print("El equivalente en grados farenheit es :", farenhey)
    
    if opc==9:
        #ejercicio 9 

        dia1=int(input("Ingresa la temperatura dia 1 :"))
        dia2=int(input("Ingresa la temperatura dia 2 :"))
        dia3=int(input("Ingresa la temperatura dia 3 :"))

        prom=(dia1+dia2+dia3)/3

        if (prom > 35):
            print("Que dias tan calurosos")
        if  (15 < prom and prom < 35):
            print("Que clima tan delicioso")
        if (prom<15):
            print("Que dias tan frios")

    if opc==10:
        #ejercicio 10
        print("nada")

    if opc==11:
        #ejercicio 11
        valorCompra=int(input("Ingrese el valor a pagar :"))
        if (10000 <= valorCompra <= 20000):
            print("El valor total a pagar es :", (valorCompra*(1-0.1)))
        if (20000 < valorCompra <= 50000):
            print("El valor total a pagar es :", (valorCompra*(1-0.3)))   
        if (valorCompra > 50000):
            print("El valor total a pagar es :", (valorCompra*(1-0.5)))

    if opc==12:
        #ejercicio  12
        edad=int(input("Ingrese la edad del deportista :"))
        estatura=int(input("Ingrese la estatura del deportista en centimetros :"))
        peso=int(input("Ingrese el peso del deportista :"))

        if (edad <= 18):
            if (estatura > 180):
                if (peso <= 80):
                    print("El deportista es aceptado")
        else:
            print("El deportista no cumple con los requisitos")         

    if opc not in (1,2,3,4,5,6,7,8,9,10,11,12,13):
        print("Opcion incorrecta")  
        
    

    if opc==13:
        entrada = False
        print("Te esperamos pronto")


print("final de programa")       





