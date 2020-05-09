"""
Decimales para coma flotante
"""
import math
from math import modf

# Constantes
EXCESO = 127
BITSMANTISA = 23


def contarComas(myInt):
    """
    Recibe el binario y devuelve la cantidad de veces que se debe corer la coma
    """
    if myInt != [0, 0, 0, 0] and myInt != [0, 0, 0, 1]:
        cantDigitos = int(math.log10(myInt)) + 1

        cantDigitos = cantDigitos - 1
        return cantDigitos
    else:
        print(f"El valor no puede correr la coma a la izq")


def arrayToString(myList):
    """
    Recibe una Lista con valores int y devuelve un string
    """
    result = ""
    for i in myList:
        result += str(i)
    return int(result)


def BaseTenToBinary(num):
    """
    Recibe un numero entero y lo convierte en binario
    """
    num = int(num)
    binary = []
    digFinal = 0
    if num > 1:
        while num > 1:
            # // vuelca los digitos del decimal
            # print (f"Dividendo: {num}")
            entero = num // 2
            if entero == 1:
                digFinal = 1
            debug1 = num % 2
            # print(f"Modulo: {debug1}")
            binary.append(num % 2)
            if digFinal == 1:
                binary.append(1)
            num = entero
        return arrayToString(reversed(binary))
    else:
        if num == 1:
            binary.append(0)
            binary.append(0)
            binary.append(0)
            binary.append(1)
            return binary
        if num == 0:
            binary.append(0)
            binary.append(0)
            binary.append(0)
            binary.append(0)
            return binary


def exponente(myBinariInteger):
    comas = contarComas(myBinariInteger)
    # print(f"Debug: Cantidad de comas exponente: {comas}")
    Exponente = EXCESO + comas
    # print(f"Exponente decimal: {comas}")
    # print(f"Debug: Exceso: {Exponente}")
    Exponente = BaseTenToBinary(Exponente)
    return Exponente


def canMultMantisa(myNumber):
    """
    Devuelve la cantidad de veces que se deve multiplicar los
    decimales base 10
    """
    LenmyNumber = len(str(myNumber))
    LenmyNumber = LenmyNumber - 1
    cantMult = BITSMANTISA - LenmyNumber
    return cantMult


def decimalToBinary(decimal, NumMantisa):
    """
    Recibe un decimal y lo convierte en binario
    definiendo la cantida de bits
    """
    # Acumuladores
    binary = []
    stop = NumMantisa
    # print(f"Debug-Stop = {stop}")
    # separedNumber = modf(decimal)
    # decimal = separedNumber[0]
    contador = 0
    for i in range(0, stop):
        if decimal != 1:
            decimal2 = decimal * 2
            myBinary = modf(decimal2)
            decimal = myBinary[0]
            # Append to binary number
            binary.append(int(myBinary[1]))
    result = ""
    for i in binary:
        result += str(i)
    return result


def valSigno(myNumber):

    if myNumber > 0:
        return 0
    else:
        1


def decIntPart(myBinary, myBynaryDecimal):
    """
    Recibe el binario entero y devuelve la parte
    que va a la mantisa
    """
    comas = contarComas(myBinary)
    strMyBin = str(myBinary)
    LenMyBin = len(strMyBin)
    strMyBin = strMyBin[1:LenMyBin]
    concatBin = strMyBin + myBynaryDecimal
    # print(f"Debug: myBinary  : {strMyBin}")
    # print(f"BinariDecimal    : {myBynaryDecimal}")
    # print(f"Debug: concatBin : {concatBin}")
    return concatBin


def main():
    print("------------------------------------------")
    print(" Numero racional a punto flotante 32 bits ")
    print("------------------------------------------")
    number = float(input("Ingrese numero: "))
    # coma = int(input("Coma corrida x veces: "))
    separedNumber = modf(number)
    integer = int(separedNumber[1])
    Signo = valSigno(integer)
    if Signo == 0 and number >= 2:
        decimal = separedNumber[0]
        # print(f"Debug Entero:  {integer}")
        # print(f"Debug Decimal: ", separedNumber[0])
        CantDigb10 = int(math.log10(integer)) + 1
        # print(f"Debug CantDigEnteros:  {CantDigb10}")
        Binario = BaseTenToBinary(integer)
        # print(f"Entero a binaro: {Binario}")
        Exponente = exponente(Binario)
        NumMantisa = canMultMantisa(Binario)
        # print(f"NumMantisa: {NumMantisa}")
        Decimales = decimalToBinary(decimal, NumMantisa)
        # print(f"DecimalesInBinary: {Decimales}")
        ParteDecimal = decIntPart(Binario, str(Decimales))
        Mantisa = ParteDecimal
        print("-------------------------------------------------------------------")
        print(f"| Signo: {Signo} | Exponente: {Exponente} | Mantisa: {Mantisa}|")
        print("-------------------------------------------------------------------")
    else:
        print("Por ahora conversion solo trabaja con valores mayores a 2")


main()
