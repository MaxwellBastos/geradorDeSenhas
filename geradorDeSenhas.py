import random, string

while True:
    tm = int(input('Informe quantos caracteres você quer (quanto maior mais seguro): '))
    chars =string.ascii_letters +string.digits + '$!@#-&*%ç+?'
    rnd = random.SystemRandom()

    print(''.join(rnd.choice(chars) for i in range(tm)))

    ds = input('Deseja gerar outra senha? S/N ').strip().upper()
    if ds == 'N':
        break




