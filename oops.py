from functools import reduce
class PlayCharacter:
    my_list = [1, 2, 3, 4]
    def __init__(self, name):
        self.name = name
    def run(self):
        print('run')
        return 'done'
    def __str__(self):
        return f'{self.name}'
    def multiply_by_2(item):
        return item*2
    def only_odd(item):
        return item%2 != 0
    print(list(map(multiply_by_2, my_list)))
    print(list(filter(multiply_by_2, my_list)))
    print(list(map(only_odd, my_list)))
    print(list(filter(only_odd, my_list)))
    print(list(map(lambda item: item*3, my_list)))
    print(reduce(lambda acc, item: acc*item, my_list))
player1 = PlayCharacter('siva')
player2 = PlayCharacter('santhi')
player1.attack ='start'
print(player1.attack)
print(str(player1))
print(player1.__str__())



