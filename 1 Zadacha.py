# Credit card
# def card_h(card):
#     return '*' * len(card[:-4]) + card[-4:]
# Palindrom
# def palindrome(data):
#     data = data.replace(' ','').lower()
#     return 'Палиндром' if data == data[::-1] else 'Не палиндром'

# Zadacha
# class Tomato:
#     states = {0: 'nothing', 1: 'flower', 2: 'green_tomato', 3: 'red_tomato'}
#     def init(self, index):
#         self._index = index
#         self._state = 0
#     def grow(self):
#         self._change_state()
#     def is_ripe(self):
#         if self._state == 3:
#             return True
#         return False
#     def _change_state(self):
#         if self._state < 3:
#             self._state += 1
#         self._print_state()
#     def _print_state(self):
#         print(f'Tomato {self._index} is {Tomato.states[self._state]}')
# class TomatoBush:
#     def init(self, num):
#         self.tomatoes = [Tomato(index) for index in range(0, num)]
#     def grow_all(self):
#         for tomato in self.tomatoes: tomato.grow()
#     def all_are_ripe(self):
#         return all([tomato.is_ripe() for tomato in self.tomatoes])
#     def give_away_all(self): self.tomatoes = []
#
# class Gardener:
#     def init(self, name, plant):
#         self.name = name
#         self._plant = plant
#     def work(self):
#         print('Gardener is working...')
#         self._plant.grow_all()
#         print('Gardener finished')
#     def harvest(self):
#         print('Gardener is harvesting...')
#
#     # Теst
#
#     Gardener.knowledge_base()
#     great_tomato_bush = TomatoBush(4)
#     gardener = Gardener('Emilio', great_tomato_bush)
#     gardener.work()
#     gardener.work()
#     gardener.harvest()
#     gardener.work()
#     gardener.harvest()