import password_functions as psf
qtyOfChars = 0

while True:
    print('-=' * 15)
    print(f"{'GERADOR DE SENHAS':^30}")
    print('-=' * 15)

    while True:
        firstCaps = str(input('Primeira Letra Maiúscula? [S/N] ')).strip().upper()
        if firstCaps in 'SN' and firstCaps != '':
            break
    
    while True:
        specialChars = str(input('Caracteres Especiais? [S/N] ')).strip().upper()
        if specialChars in 'SN' and specialChars != '':
            break
    
    while True:
        numbers = str(input('Com Números? [S/N] ')).strip().upper()
        if numbers in 'SN' and numbers != '':
            break
    
    while True:
        qtyOfChars = int(input('Quantidade de Caracteres (Entre 6 e 12) '))
        if qtyOfChars >= 6 and qtyOfChars <= 12:
            break

    # GERAR SENHA SOMENTE LETRAS SEM MAIÚSCULAS:
    if firstCaps == 'N' and specialChars == 'N' and numbers == 'N':
        print('-=' * 15)
        print(f'SENHA GERADA: {psf.generateOnlyLetters(qtyOfChars)}')

    # GERAR SENHAS SOMENTE LETRAS COM PRIMEIRA LETRA MAIÚSCULA:
    if firstCaps == 'S' and specialChars == 'N' and numbers == 'N':
        print('-=' * 15)
        password =  psf.generateOnlyLetters(qtyOfChars)
        print(f'SENHA GERADA: {psf.generateLettersWithCaps(password)}')

    # GERAR SENHAS COM CARACTERES ESPECIAS SEM MAIÚSCULAS:
    if firstCaps == 'N' and specialChars == 'S' and numbers == 'N':
        print('-=' * 15)
        password = psf.generateOnlyLetters(qtyOfChars)
        password = psf.generateWithSpecialChars(password)
        print(f'SENHA GERADA: {psf.shufflePassword(password)}')

    # GERAR SENHAS COM NÚMEROS SEM MAIÚSCULAS:
    if firstCaps == 'N' and specialChars == 'N' and numbers == 'S':
        print('-=' * 15)
        password = psf.generateOnlyLetters(qtyOfChars)
        password = psf.generateWithNumbers(password)
        print(f'SENHA GERADA: {psf.shufflePassword(password)}')

    # GERAR SENHAS COM PRIMEIRA MAIÚSCULA E CARACTERES ESPECIAIS:
    if firstCaps == 'S' and specialChars == 'S' and numbers == 'N':
        print('-=' * 15)
        password = psf.generateOnlyLetters(qtyOfChars)
        password = psf.generateWithSpecialChars(password)
        password = psf.shufflePassword(password)
        print(f'SENHA GERADA: {psf.generateLettersWithCaps(password)}')

    # GERAR SENHAS COM PRIMEIRA MAIÚSCULA E NÚMEROS:
    if firstCaps == 'S' and specialChars == 'N' and numbers == 'S':
        print('-=' * 15)
        password = psf.generateOnlyLetters(qtyOfChars)
        password = psf.generateWithNumbers(password)
        password = psf.shufflePassword(password)
        print(f'SENHA GERADA: {psf.generateLettersWithCaps(password)}')

    # GERAR SENHAS COM CARACTERES ESPECIAIS E NÚMEROS:
    if firstCaps == 'N' and specialChars == 'S' and numbers == 'S':
        print('-=' * 15)
        password = psf.generateOnlyLetters(qtyOfChars)
        password = psf.generateWithSpecialChars(password)
        password = psf.generateWithNumbers(password)
        print(f'SENHA GERADA: {psf.shufflePassword(password)}')
    
    # GERAR SENHAS COM PRIMEIRA MAIÚSCULA, CARACTERES ESPECIAIS E NÚMEROS:
    if firstCaps == 'S' and specialChars == 'S' and numbers == 'S':
        print('-=' * 15)
        password = psf.generateOnlyLetters(qtyOfChars)
        password = psf.generateWithSpecialChars(password)
        password = psf.generateWithNumbers(password)
        password = psf.generateLettersWithCaps(password)
        print(f'SENHA GERADA: {psf.shufflePassword(password)}')

    # PERGUNTA SE QUER GERAR UMA NOVA SENHA OU SAIR DO SISTEMA:
    print('-=' * 15)
    resp = str(input('Quer gerar outra senha? [S/N] ')).strip().upper()
    while resp not in 'SN' or resp == '':
        resp = str(input('Quer gerar outra senha? [S/N] ')).strip().upper()
    if resp == 'N':
        break
        