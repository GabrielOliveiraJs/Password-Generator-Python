from random import randint
alphabetArray = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbersArray = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
specialCharsArray = ['@', '#', '$', '%', '&']

# FUNÇÃO PARA EMBARALHAR A SENHA:
def shufflePassword(password):
    passwordLen = len(password)
    shuffledPass = ''
    aux = ''
    rand = []
    n = 0
    i = 0

    while i < passwordLen:
        n = randint(0, passwordLen - 1)

        if n not in rand:
            rand.append(n)
            i += 1

    for i in range(0, passwordLen):
        aux += password[int(rand[i])]
        shuffledPass += aux[i]
    password = shuffledPass
    return password

# FUNÇÃO PARA GERAR UM ARRAY DE LETRAS ALEATÓRIO:
def generateOnlyLetters(qtyOfChars):
    password = ''
    i = 0
    while i < qtyOfChars:
        n = randint(0, len(alphabetArray) - 1)
        password += alphabetArray[n]
        i += 1
    return password

# FUNÇÃO PARA TRANSFORMAR A PRIMEIRA LETRA DA SENHA EM MAIÚSCULA:
def generateLettersWithCaps(password):
    for i, c in enumerate(password):
        if c in alphabetArray:
            password = password[:i] + password[i:].capitalize()
            break
    return password

# FUNÇÃO PARA ADICIONAR CARACTERES ESPECIAIS NA SENHA:
def generateWithSpecialChars(password):
    qtyOfChars = 0
    passwordLen = len(password)

    if passwordLen == 6 or passwordLen == 7:
        qtyOfChars = 1
    elif passwordLen == 8 or passwordLen == 9:
        qtyOfChars = 2
    elif passwordLen == 10 or passwordLen == 11:
        qtyOfChars = 3
    elif passwordLen == 12:
        qtyOfChars = 4

    chars = ''
    i = 0
    while i < qtyOfChars:
        n = randint(0, len(specialCharsArray) - 1)
        chars += specialCharsArray[n]
        i += 1
    password += chars
    password = password[qtyOfChars:]
    return password

# FUNÇÃO PARA ADICIONAR NÚMEROS NA SENHA:
def generateWithNumbers(password):
    qtyOfNumbers = 0
    passwordLen = len(password)

    if passwordLen == 6 or passwordLen == 7 or passwordLen == 8:
        qtyOfNumbers = 1
    elif passwordLen == 9 or passwordLen == 10 or passwordLen == 11:
        qtyOfNumbers = 2
    elif passwordLen == 12:
        qtyOfNumbers = 3

    numbs = ''
    i = 0
    while i < qtyOfNumbers:
        n = randint(0, len(numbersArray) - 1)
        numbs += numbersArray[n]
        i += 1
    password += numbs
    password = password[qtyOfNumbers:]
    return password
