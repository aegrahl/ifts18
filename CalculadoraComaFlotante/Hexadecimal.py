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

IEEE754Binario2 = "01000001001000110011001100110011"


def separarBinario(IEEE754Binario):
    BinHexa = []
    for i in range(0, 32, 4):
        BinHexa.append(IEEE754Binario[i : i + 4])
    # for i in BinHexa:
    #     print(f"{i}", end=" ")
    return BinHexa


def convertirHexa(listBinario):
    hexadecimal = []

    for b in listBinario:
        if b in diccHexa:
            valor = diccHexa[b]
            hexadecimal.append(valor)
    return hexadecimal


def binIEEEAhexa(binIEEE):
    listBinario = separarBinario(binIEEE)
    listHexa = convertirHexa(listBinario)
    result = ""
    for i in listHexa:
        result += str(i)
    return result


binIEEEAhexa(IEEE754Binario2)
