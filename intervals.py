from os import system
from random import randint
from sys import argv
from time import sleep


class IntervalsHelper:

    def __init__(self):
        self._notes = ['Do', 'Sol', 'Re', 'La', 'Si']
        self._intervals = [
            '1ra',
            '2da menor',
            '2da mayor',
            '3ra menor',
            '3ra mayor',
            '4ta justa',
            '4ta aumentada',
            '5ta disminuida',
            '5ta justa'
        ]
        self._reset()

    def _reset(self):
        self._current = []
        for n in self._notes:
            for i in self._intervals:
                self._current.append(f' * | {n} {i}')

    def pick_random(self) -> str:
        if not self._current:
            print('Finished! Resetting...')
            sleep(3)
            self._reset()

        length = len(self._current)
        return self._current.pop(randint(0, length - 1))


if __name__ == '__main__':
    try:
        interval: int = int(argv[1])
    except KeyError:
        print('No time interval (int) provided in command line.')
        raise SystemExit()

    practice = IntervalsHelper()
    while True:
        system('clear')
        print(practice.pick_random())
        sleep(interval)
