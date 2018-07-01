#!/usr/bin/env python3

import click
import collections
import sys
import time

CHARS = ' ▁▂▃▄▅▆▇█'
UNKNOWN = '▒'


@click.command()
@click.option('-d', '--delimiter', default=',')
@click.option('-h', '--height', default=40, type=int)
def main(delimiter, height):
    data = collections.deque(maxlen=100)
    last_refresh = 0
    for line in sys.stdin:
        cols = line.rstrip().split(delimiter)
        record = tuple(map(float, cols[:3]))
        data.append(record)
        if time.time() < last_refresh + 0.2:
            continue
        ymin = float('+inf')
        ymax = float('-inf')
        for record in data:
            yvalue = record[2]
            ymin = min(ymin, yvalue)
            ymax = max(ymax, yvalue)
        if ymin == ymax:
            ymax = ymin + 0.1
        click.clear()
        for y in range(height-1, -1, -1):
            label = ymin + (ymax - ymin) * y
            print('{:.2f}ms ┤'.format(label/(1000**2)).rjust(16), end='')
            for record in data:
                yvalue = record[2]
                status = record[1]
                if status >= 200 and status < 400:
                    color = 'green'
                elif status >= 400 and status < 500:
                    color = 'yellow'
                else:
                    color = 'red'
                val = 1. * (yvalue - ymin)/(ymax - ymin) * height
                idx = min(max(round(len(CHARS) * (val - y)), 0), len(CHARS)-1)
                char = CHARS[idx]
                if yvalue == 0:
                    char = UNKNOWN
                click.secho(char, nl=False, fg=color)
            print()
        print(' ' * 16, end='')
        for i in range(100):
            print('┬', end='')
        print()
        last_refresh = time.time()


if __name__ == '__main__':
    main()
