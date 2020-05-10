import math
from math import modf
from os import system, name


# Constantes:
EXCESO = 127
BITSMANTISA = 23

diccHexa = {
    "0000": 0,
    "0001": 1,
    "0010": 2,
    "0011": 3,
    "0100": 4,
    "0101": 5,
    "0110": 6,
    "0111": 7,
    "1000": 8,
    "1001": 9,
    "1010": "A",
    "1011": "B",
    "1100": "C",
    "1101": "D",
    "1110": "E",
    "1111": "F",
}


def FloatToPartInt(num):
    """ Devuelve la parte entera de un numero flotante.
    Parameters:
    num (float): Numero flotante.
    Return: int

    """
    numeroSeparado = modf(num)
    parteEntera = int(numeroSeparado[1])
    return parteEntera


def FloatToPartDeci(num):
    """ Devuelve la parte decimal de un numero flotante.
    Parameters:
    num (float): Numero flotante.
    Return: float

    """
    numeroSeparado = modf(num)
    parteDecimal = numeroSeparado[0]
    return parteDecimal


def analizarNumero(num):
    """ Indica como correr la coma.

    Parameters:
    num (float): Numero flotante.
    Return:
    string: Como correr la coma.

    """
    parteEntera = FloatToPartInt(num)
    if parteEntera == 1:
        return "No se corre coma"
    elif parteEntera < 1:
        return "Coma a la derecha"
    else:
        return "Coma a la izquierda"


def EvaluarSigno(numBase10):
    """ Devuelve el signo.
    Parameters:
    numBase10 (float): Numero flotante.
    Return:
    string: 0 - Positivo ; 1 - Negativo.

    """
    parteEntera = FloatToPartInt(numBase10)
    if parteEntera == 0:
        return 0
    elif parteEntera > 0:
        return "0"
    else:
        return "1"


def ListIntToInt(List):
    """ Recibe una Lista con valores int y retorna un int
    Parameters:
    List (int): Lista compuesta por enteros.
    Return: int

    """
    result = ""
    for i in List:
        result += str(i)
    return int(result)


def baseTenToBinary(numBase10):
    """ Recibe un numero entero y lo convierte en binario.

        Divide el numero por 2 n veces y segun el cociente y el resto
        conforma el numero binario.
    Parameters:
    numBase10 (float): Numero base 10.
    Return:
    int: Numero Base 2 - Binario

    """
    num = FloatToPartInt(numBase10)
    binary = []
    digFinal = 0
    if num == 1:
        return 1111111
    while num > 1:
        # // vuelca los digitos del decimal
        entero = num // 2
        if entero == 1:
            digFinal = 1
        debug1 = num % 2
        binary.append(num % 2)
        if digFinal == 1:
            binary.append(1)
        num = entero
    return ListIntToInt(reversed(binary))


def canMultManIzq(numBin):
    """ Calcula la cantidad que se debe multiplicar la parte decimal base 10.
    Cuando la coma se dezplaza a la izquierda.
    Parameters:
    comaCorrida (string): valor retornado de analizarNumero().
    numBase10 (float): numero base 10.
    Return:
    List(string): {Signo, Exponente, Mantisa}
    """
    LenmyNumber = len(str(numBin))
    LenmyNumber = LenmyNumber - 1
    cantMult = BITSMANTISA - LenmyNumber
    return cantMult


def decimalToBinary(numDecimal, NumMantisa):
    """ Recibe la parte decimal y la convierte en binario.
    Parameters:
    numDecimal (float): Parte decimal del numero base 10.
    NumMantisa (float): Cantidad de veces que se multiplica.
    Return: string : Binario
    """
    binary = []  # Acumulador
    stop = NumMantisa
    contador = 0
    for i in range(0, stop):
        if numDecimal != 1:
            decimal = numDecimal * 2
            myBinary = modf(decimal)
            numDecimal = myBinary[0]
            # Append to binary number
            binary.append(int(myBinary[1]))
    result = ""
    for i in binary:
        result += str(i)
    return result


def contarComasDer(numDecimal):
    """ Recibe la parte decimal y devuelve cuantas
    veces se corre la coma a la derecha.
    Parameters:
    numDecimal (float):.
    Return: int : Lugares que se come la coma a la derecha.

    """
    binary = []
    stop = 0
    x = 0
    while stop < 1:
        decimal = numDecimal * 2
        myBinary = modf(decimal)
        binary.append(int(myBinary[1]))
        numDecimal = myBinary[0]
        stop = myBinary[1]
        x += 1
    result = ""
    # for i in binary:
    #     result += str(i)
    # len(result)
    # return len(result)
    return x


def calcMantisaDer(numDecimal, comas):
    """ Calcula la mantisa para el caso que se corra la coma a la derecha.
    Parameters:
    numDecimal (float): Numero a convertir.
    comas (int): Cantidad de veces que se corrio la coma a la Derecha.
    Return: string: Binario
    """
    multMant = BITSMANTISA + comas
    binario = decimalToBinary(numDecimal, multMant)
    result = binario[comas:multMant]
    return result


def valorAbsoluto(numBase10):
    """ Verifica el signo del numero ingresado y lo devuelve sin signo
    Parameters:
    numBase10 (float): Numero a convertir.
    Return: float
    """
    # Valor absoluto del numero
    numeroPositivo = abs(numBase10)
    # print(f"Debug numeroPositivo: {numeroPositivo}")
    return numeroPositivo


def separarBinario(IEEE754Binario):
    """Recibe el binIEEE y lo separa en bytes.
    Parameters:
    IEEE754Binario (string): binarioIEEE a convertir.
    Return: List(string)
    
    """
    BinHexa = []
    for i in range(0, 32, 4):
        BinHexa.append(IEEE754Binario[i : i + 4])
    # for i in BinHexa:
    #     print(f"{i}", end=" ")
    return BinHexa


def convertirHexa(listBinario):
    """Recibe el una lista de bytes y la devuelve en hexadecimal.
    Parameters:
    listBinario List(string): Listas de bytes.
    Return: List(string): Lista de hexadecimales
    """
    hexadecimal = []

    for b in listBinario:
        if b in diccHexa:
            valor = diccHexa[b]
            hexadecimal.append(valor)
    return hexadecimal


def binIEEEAhexa(binIEEE):
    """Recibe el una lista de hexadecimales y la devuelve un string 
    con valor hexadecimal.
    Parameters:
    binIEEE List(string): Listas de bytes Hexadecimales.
    Return: string: Hexadecimale IEEE754
    """
    listBinario = separarBinario(binIEEE)
    listHexa = convertirHexa(listBinario)
    result = ""
    for i in listHexa:
        result += str(i)
    return result


def ConvertirComaFIzq(numBase10):
    """ Recibe el numero Real y devuelve signo, exponente y mantisa.
    En el caso que la coma se mueva a la izq.
    Parameters:
    numBase10 (float): Numero a convertir.
    Return: List(string) : [0] signo; [1] exponente; [2] mantisa; [3] HexaIEEE754.
    """
    resultado = []
    signo = EvaluarSigno(numBase10)
    numBase10 = valorAbsoluto(numBase10)
    parteEntera = FloatToPartInt(numBase10)
    # print(f"Debug: Parte Entera: {parteEntera}")
    enteroBinario = baseTenToBinary(parteEntera)
    # print(f"Debug: Entero base 2: {enteroBinario}")
    cantDigitos = int(math.log10(enteroBinario)) + 1
    cantDigitos = cantDigitos - 1
    comasIzq = cantDigitos
    # print(f"Debug: Cantidad de comas izq: {comasIzq}")
    exponenteBase10 = EXCESO + comasIzq
    # print(f"Debug: Exponente Base 10: {exponente}")
    exponenteBinario = baseTenToBinary(exponenteBase10)
    # print(f"Debug: ExpoComaIzq Base 2: {exponente}")
    numMantisa = canMultManIzq(enteroBinario)
    # print(f"Debug numMantisa {numMantisa}")
    decimalBase10 = FloatToPartDeci(numBase10)
    # print(f"Debug decimalBase10 {decimalBase10}")
    decimalesBinario = decimalToBinary(decimalBase10, numMantisa)
    # print(f"Debug: decimalesBinario: {decimalesBinario}")
    strMyBin = str(enteroBinario)
    LenMyBin = len(strMyBin)
    # print(f"Debug: LenMyBin: {LenMyBin}")
    strMyBin = strMyBin[1:LenMyBin]
    # print(f"Debug: strMyBin: {strMyBin}")
    mantisa = strMyBin + str(decimalesBinario)
    # print(f"Debug: mantisa Base 2: {mantisa}")
    hexaIEE = binIEEEAhexa(str(signo) + str(exponenteBinario) + str(mantisa))
    resultado.append(signo)
    resultado.append(exponenteBinario)
    resultado.append(mantisa)
    resultado.append(hexaIEE)
    return resultado


def ConvertirComaF(numBase10):
    """ Recibe el numero Real y devuelve signo, exponente y mantisa.
    En el caso que la coma no se mueva por tener valor 1 como entero.
    Parameters:
    numBase10 (float): Numero a convertir.
    Return: List(string) : [0] signo; [1] exponente; [2] mantisa; [3] HexaIEEE754.
    """
    resultado = []
    signo = EvaluarSigno(numBase10)
    numBase10 = valorAbsoluto(numBase10)
    parteEntera = FloatToPartInt(numBase10)
    enteroBinario = baseTenToBinary(parteEntera)
    exponenteBase10 = 127
    exponenteBinario = baseTenToBinary(exponenteBase10)
    exponenteBinario = str(exponenteBinario)  # Dado que tiene un 0 delante
    exponenteBinario = "0" + exponenteBinario
    numMantisa = 23
    decimalBase10 = FloatToPartDeci(numBase10)
    decimalesBinario = decimalToBinary(decimalBase10, numMantisa)
    mantisa = str(decimalesBinario)
    hexaIEE = binIEEEAhexa(str(signo) + str(exponenteBinario) + str(mantisa))
    resultado.append(signo)
    resultado.append(exponenteBinario)
    resultado.append(mantisa)
    resultado.append(hexaIEE)
    return resultado


def ConvertirComaFDer(numBase10):
    """ Recibe el numero Real y devuelve signo, exponente y mantisa.
    En el caso que la coma se mueva a la derecha.
    Parameters:
    numBase10 (float): Numero a convertir.
    Return: List(string) : [0] signo; [1] exponente; [2] mantisa; [3] HexaIEEE754.

    """
    resultado = []
    signo = EvaluarSigno(numBase10)
    numBase10 = valorAbsoluto(numBase10)
    # print(f"valor absoluto: {numBase10}")
    comas = contarComasDer(numBase10)
    exponenteBase10 = EXCESO - comas
    exponenteBinario = baseTenToBinary(exponenteBase10)
    exponenteBinario = str(exponenteBinario)  # Dado que tiene un 0 delante
    exponenteBinario = "0" + exponenteBinario
    numDecimal = FloatToPartDeci(numBase10)
    mantisa = calcMantisaDer(numDecimal, comas)
    hexaIEE = binIEEEAhexa(str(signo) + str(exponenteBinario) + str(mantisa))
    resultado.append(signo)
    resultado.append(exponenteBinario)
    resultado.append(mantisa)
    resultado.append(hexaIEE)
    return resultado


def imprimirResultado(resultado):
    print("\u2554", end="")
    for i in range(66):
        print(
            "\u2550", end="",
        )
    print("\u2557", end="")
    print(
        f"\n\u2551 Signo: {resultado[0]} \u2551 Exponente: {resultado[1]} \u2551 Mantisa: {resultado[2]}\u2551"
    )
    print("\u255A", end="")
    for i in range(66):
        print(
            "\u2550", end="",
        )
    print("\u255D")
    print("\u2554", end="")
    for i in range(66):
        print(
            "\u2550", end="",
        )
    print("\u2557", end="")
    print(
        f"\n\u2551 IEEE754 Hexadecimal: {resultado[3]}                                    \u2551"
    )
    print("\u255A", end="")
    for i in range(66):
        print(
            "\u2550", end="",
        )
    print("\u255D")


def clear():
    # Para  windows
    if name == "nt":
        _ = system("cls")

    # Para mac y linux(here, os.name is 'posix')
    else:
        _ = system("clear")


def continuar():
    continuar = input("Presione y/Y para continuar y presione ENTER\n")
    if continuar == "y" or continuar == "Y":
        main()
    else:
        clear()
        exit(0)


def decidirConversion(comaCorrida, numBase10):
    """ Segun como se deba correr la coma ejecuta las funciones adecuadas.

    Parameters:
    comaCorrida (string): valor retornado de analizarNumero().
    numBase10 (float): numero base 10.
    Return:
    List(string): {Signo, Exponente, Mantisa}

    """
    # print(f"Debug signo: {signo}")
    if comaCorrida == "No se corre coma":
        resultado = ConvertirComaF(numBase10)
        imprimirResultado(resultado)
        continuar()
    elif comaCorrida == "Coma a la derecha":
        resultado = ConvertirComaFDer(numBase10)
        imprimirResultado(resultado)
        continuar()
    elif comaCorrida == "Coma a la izquierda":
        resultado = ConvertirComaFIzq(numBase10)
        imprimirResultado(resultado)
        continuar()


def imprimirBanner():
    """
    Imprime el Banner
    """
    print("\u2554", end="")
    for i in range(66):
        print(
            "\u2550", end="",
        )
    print("\u2557", end="")
    print(
        f"\n\u2551 Conversion Base10 a Flotante Simple IEEE7545          (32bits)   \u2551"
    )
    print("\u255A", end="")
    for i in range(66):
        print(
            "\u2550", end="",
        )
    print("\u255D")


def main():
    clear()
    imprimirBanner()
    numero = float(input(" Ingrese un numero base 10: "))
    comaCorrida = analizarNumero(numero)
    decidirConversion(comaCorrida, numero)
    # print(f"Debug. analizarNumero: {comaCorrida}")


main()
