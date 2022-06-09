from random import shuffle
class Card():
    """ 创建一张牌 """
    suits = ["红桃","黑桃","方块","梅花"]
    values = [None,None,"2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    def __init__(self,v,s):
        self.value = v
        self.suit = s

    def __lt__(self, other):
        if self.value < other.value:
            return True
        if self.value == other.value:
            if self.suit < other.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        f = self.suits[self.suit] + self.values[self.value]
        return f

class Deck:
    """ 创建一副牌 """
    def __init__(self):
        self.cards = []
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)
    def rm_cards(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()
    def __repr__(self):
        return self.cards

class Play():
    """ 创建游戏玩家 """
    def __init__(self,name):
        self.wins = 0
        self.name = name
class Game():
    """ 创建游戏 """
    def __init__(self):
        self.deck = Deck()
        self.name1 = input("请输如玩家名字：")
        self.name2 = input("请输入玩家名字：")
        self.play1 = Play(self.name1)
        self.play2 = Play(self.name2)
    def win(self,winner):
        w = "{} 完胜！".format(winner)
        print(w)
    def draw(self,play1,p1,play2,p2):
        """ 打印玩家手里的牌 """
        s = "{}抽到{}，{}抽到{}".format(play1,p1,play2,p2)
        print(s)
    def play_game(self):
        """ 开始游戏 """
        cards = self.deck.cards
        print("开始游戏！")
        while len(cards) > 2:
            msg = "q键推出，任意键开始游戏！ "
            response = input(msg)
            if response == "q":
                break
            pl1 = self.deck.rm_cards()
            pl2 = self.deck.rm_cards()
            p1 = self.play1.name
            p2 = self.play2.name
            self.draw(p1,pl1,p2,pl2)
            if pl1 > pl2:
                self.play1.wins += 1
                self.win(self.play1.name)
            else:
                self.play2.wins += 1
                self.win(self.play2.name)

        win = self.winner(self.play1,self.play2)
        print("游戏结束！ {}完胜！".format(win))
    def winner(self,p1,p2):
        """ 比点数 """
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "平局"
game = Game()
game.play_game()



