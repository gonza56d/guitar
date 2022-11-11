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
        self._current_ns = self._notes.copy()
        self._current_is = self._intervals.copy()

    def pick_random(self) -> str:
        if len(self._current_ns) == 0 or len(self._current_is) == 0:
            self._reset()

        n_len = len(self._current_ns)
        i_len = len(self._current_is)
        note = self._current_ns.pop(randint(0, n_len - 1))
        interval = self._current_is.pop(randint(0, i_len - 1))
        return f' * | {note} {interval}'


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
