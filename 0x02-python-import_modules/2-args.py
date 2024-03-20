#!/usr/bin/python3
from sys import argv


if __name__ == "__main__":
    check_len = len(argv) - 1
    if check_len == 0:
        print('0 arguments.')
    elif check_len == 1:
        print('1 argument:')
        print('1: {}'.format(argv[1]))
    else:
        print('{} arguments:'.format(check_len))
        for k in range(1, len(argv)):
            print('{}: {}'.format(k, argv[k]))
