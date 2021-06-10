import sys
from random import randint


class Game:
    figures = ('Paper', 'Scissors', 'Stone')
    results = []
    player_score = 0
    computer_score = 0

    def get_random_figure(self):
        figure = self.figures[randint(0, len(self.figures) - 1)]
        return figure

    def chose_figure(self):
        i = 1
        for figure in self.figures:
            print(str(i) + '. ' + figure)
            i += 1
        x = int(input('Choose figure id: '))
        return self.figures[x - 1]

    def star_game(self):
        while True:
            self.chose_game_option()

    def play(self):
        player_figure = self.chose_figure()
        computer_figure = self.get_random_figure()
        print('Fight!!! \n')
        print(f'Your: {player_figure} vs {computer_figure} : Computer \n')
        self.who_win_turn()

    def show_results(self):
        print('Your score:' + str(self.player_score))
        print('Computer score: ' + str(self.computer_score) + '\n')

    def who_win_game(self):
        winner = ''

        for score in self.results:
            if score == 0:
                self.player_score += 1
            elif score == 1:
                self.computer_score += 1

        if self.player_score > self.computer_score:
            winner = 'You Won!!! Congratulations!!!'
        elif self.computer_score > self.player_score:
            winner = 'You Loose!!! :( Try next time.'
        elif self.player_score == self.computer_score:
            winner = 'It\'s Draw.'

        print(winner)

    def who_win_turn(self):
        return ''

    def chose_game_option(self):
        print('1. Play')
        print('2. Show results')
        print('3. Exit')
        x = int(input('\n' + 'Your choice is: '))
        if x == 1:
            self.play()
        elif x == 2:
            self.show_results()
        elif x == 3:
            sys.exit(self.who_win_game())
