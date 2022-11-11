from os import system
from random import randint
from sys import argv
from time import sleep

notes = ['C', 'G', 'D', 'A', 'B']
intervals = [
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


def pick_random():
    n_len = len(notes)
    i_len = len(intervals)
    note = notes[randint(0, n_len - 1)]
    interval = intervals[randint(0, i_len - 1)]
    return f' * | {note} {interval}'


if __name__ == '__main__':
    try:
        interval: int = int(argv[1])
    except KeyError:
        print('No time interval (int) provided in command line.')
        raise SystemExit()
    while True:
        system('clear')
        print(pick_random())
        sleep(interval)
