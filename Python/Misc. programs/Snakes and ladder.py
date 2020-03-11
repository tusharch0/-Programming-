class snakesandladder(object):
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.ladd = [4, 24, 48, 67, 86]
        self.lengthladd = [13, 23, 5, 12, 13]
        self.snake = [6, 26, 47, 23, 55, 97]
        self.lengthsnake = [4, 6, 7, 5, 8, 9]

    def dice(self):
        chances = 0
        print("----------------LeTs StArT ThE GaMe----------------\n")
        while self.position <= 104:
            roll = random.choice([1, 2, 3, 4, 5, 6])
            print('roll value: ', roll)
            self.position = roll + self.position
            if self.position > 104:
                self.position = self.position - roll
            if self.position == 104:
                print('completed the game')
                break

            if self.position in self.ladd:
                for n in range(len(self.ladd)):
                    if self.position == self.ladd[n]:
                        self.position = self.position + self.lengthladd[n]
            if self.position in self.snake:
                for n in range(len(self.snake)):
                    if self.position == self.snake[n]:
                        self.position = self.position - self.lengthsnake[n]

            print('Current position of the player : ', self.position, '\n')
            chances += 4/4
        print('ToTal number oF chances : ', chances)


zack = snakesandladder('zack', 0)
zack.dice()
