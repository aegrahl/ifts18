import math
from math import modf

# Constantes:
EXCESO = 127
BITSMANTISA = 23


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
    if parteEntera > 0:
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
    print(f"Debug numeroPositivo: {numeroPositivo}")
    return numeroPositivo


def ConvertirComaFIzq(numBase10):
    """ Recibe el numero Real y devuelve signo, exponente y mantisa.
    En el caso que la coma se mueva a la izq.
    Parameters:
    numBase10 (float): Numero a convertir.
    Return: List(string) : [0] signo; [1] exponente; [2] mantisa.
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
    resultado.append(signo)
    resultado.append(exponenteBinario)
    resultado.append(mantisa)
    return resultado


def ConvertirComaF(numBase10):
    """ Recibe el numero Real y devuelve signo, exponente y mantisa.
    En el caso que la coma no se mueva por tener valor 1 como entero.
    Parameters:
    numBase10 (float): Numero a convertir.
    Return: List(string) : [0] signo; [1] exponente; [2] mantisa.
    """
    resultado = []
    signo = EvaluarSigno(numBase10)
    numBase10 = valorAbsoluto(numBase10)
    parteEntera = FloatToPartInt(numBase10)
    enteroBinario = baseTenToBinary(parteEntera)
    exponenteBase10 = 127
    exponenteBinario = baseTenToBinary(exponenteBase10)
    numMantisa = 23
    decimalBase10 = FloatToPartDeci(numBase10)
    decimalesBinario = decimalToBinary(decimalBase10, numMantisa)
    mantisa = str(decimalesBinario)
    resultado.append(signo)
    resultado.append(exponenteBinario)
    resultado.append(mantisa)
    return resultado


def ConvertirComaFDer(numBase10):
    """ Recibe el numero Real y devuelve signo, exponente y mantisa.
    En el caso que la coma se mueva a la derecha.
    Parameters:
    numBase10 (float): Numero a convertir.
    Return: List(string) : [0] signo; [1] exponente; [2] mantisa.

    """
    resultado = []
    signo = EvaluarSigno(numBase10)
    numBase10 = valorAbsoluto(numBase10)
    comas = contarComasDer(numBase10)
    exponenteBase10 = EXCESO - comas
    exponenteBinario = baseTenToBinary(exponenteBase10)
    numDecimal = FloatToPartDeci(numBase10)
    mantisa = calcMantisaDer(numDecimal, comas)
    resultado.append(signo)
    resultado.append(exponenteBinario)
    resultado.append(mantisa)
    return resultado


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
        numBase10 = V
        resultado = ConvertirComaF(numBase10)
        print(
            f"Signo: {resultado[0]} ; Exponente: {resultado[1]} ; Mantisa: {resultado[2]} "
        )
    elif comaCorrida == "Coma a la derecha":
        resultado = ConvertirComaFDer(numBase10)
        print(
            f"Signo: {resultado[0]} ; Exponente: {resultado[1]} ; Mantisa: {resultado[2]} "
        )
    elif comaCorrida == "Coma a la izquierda":
        resultado = ConvertirComaFIzq(numBase10)
        print(
            f"Signo: {resultado[0]} ; Exponente: {resultado[1]} ; Mantisa: {resultado[2]} "
        )


def imprimirBanner():
    """
    Imprime el Banner
    """
    print(
        "------------------------------------------\nNumero racional a punto flotante 32 bits\n------------------------------------------"
    )


def main():
    imprimirBanner()
    numero = float(input("Ingrese el numero base 10: "))
    comaCorrida = analizarNumero(numero)
    decidirConversion(comaCorrida, numero)
    # print(f"Debug. analizarNumero: {comaCorrida}")


main()

# """ Analiza un numero segun la parte entera.

# Parameters:
# num (float): Numero flotante.

# Return:
# string: Como correr la coma.

# """
