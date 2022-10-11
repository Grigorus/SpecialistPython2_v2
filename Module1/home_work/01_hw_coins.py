import random

class Coin:
    def __init__(self):
        self.side = None

    def flip(self) -> None:

        """
        Подбрасывание монетки. # heads-орел/tails-решка
        """

        self.side = 'heads' if random.randint(0, 99) < 50 else 'tails'# random: heads/tails


# Задание:
# 1. Создайте список из n-монеток, n - вводится с клавиатуры
# 2. Подбросьте(flip) все монетки. У каждой монетки в списке вызовите метод .flip()
# 3. Выведите соотношение выпавших орлов и решек в процентах

# Пояснение: когда вы создаете монетку, то она находится в неопределенном состоянии self.side = None, т.е.
# она находится у вас в руке и не выпала ни орлом ни решкой. Монетка "определеяется" со стороной(орел/решка),
# только после того, как вы ее подбрасываете(вызываете метод flip())


n = int(input())
coin_list = []
orel = 0
reshka = 0
for i in range(n):
    current_coin = Coin()
    current_coin.flip()
    if current_coin.side == 'heads':
        orel += 1
    else:
        reshka += 1
    coin_list.append(current_coin)
print(orel/reshka)
