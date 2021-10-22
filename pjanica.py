from random import shuffle

class Card:
    """Карты. suits - масти, values - значения карт"""
    
    suits = ["пикей",
             "червей",
             "бубей",
             "треф"]

    values = [None, None, "2", "3", "4", "5", "6",
              "7", "8", "9", "10", "валета", "даму",
              "короля", "туза"]

    def __init__(self, v, s):
        """suit и value - целые числа"""
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        """Сравнение двух объектов Card на меньше"""
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        """Сравнение двух объектов Card на меньше"""
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        """Вывод катры, которую представляет объект Card"""
        v = self.values[self.value] + " " \
            + self.suits[self.suit]
        return v

class Deck:
    """Колода карт"""
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def rm_card(self):
        """Изымает и возвращает карту из колоды"""
        if len(self.cards) == 0:
            return
        return self.cards.pop()

class Player:
    """Игрок"""
    def __init__(self, name):
        self.wins = 0  # количество раундов
        self.card = None  # карта в данный момент
        self.name = name  # имя игрока

class Game:
    """Игра"""
    def __init__(self):
        name1 = input("Имя игрока 1: ")
        name2 = input("Имя игрока 2: ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        w = "{} забирает карты"
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        """открисовка хода игры"""
        d = "{} кладет {}, а {} кладет {}"
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)
        
    def play_game(self):
        """запуск игры"""
        cards = self.deck.cards
        print("Поехали!")
        while len(cards) >= 2:
            m = "Нажмите Х для выхода. Нажмите любую другую клавишу для начала игры."
            response = input(m)
            if response == 'X':
                break
            p1c = self.deck.rm_card()  # карта первому игроку
            p2c = self.deck.rm_card()  # карта второму игроку
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins +=1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)
        win = self._winner(self.p1, self.p2)
        print("Игра окончена. {} выиграл!".format(win))

    def _winner(self, p1, p2):
        """определение победителя"""
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "Ничья!"


game = Game()
game.play_game()
                
