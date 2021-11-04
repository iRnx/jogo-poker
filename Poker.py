from random import shuffle

naipe = '♥♦♣♠'
cartas = 'AKQJT98765432'
cartas_deck = list()
guarda_cartas = list()
numero_jogadores = 9
for c in naipe:
    for v in cartas:
        cartas_deck.append(c + v)
shuffle(cartas_deck)
for c in range(0, numero_jogadores):
    guarda_cartas.append(cartas_deck.pop(0)), guarda_cartas.append(cartas_deck.pop(0))

x = 0
for c in range(0, numero_jogadores):
    print(f'Player{c + 1}: {guarda_cartas[x]} {guarda_cartas[x + 1]}')
    x = x + 2

mesa = list()
for c in range(1, 6):
    mesa.append(cartas_deck.pop(0))
print(f'{" " * 7}Mesa: {mesa[0]} {mesa[1]} {mesa[2]} {mesa[3]} {mesa[4]}')
