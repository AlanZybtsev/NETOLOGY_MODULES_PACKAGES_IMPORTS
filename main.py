import sys
import datetime

if __name__ == '__main__':
    from application_ import salary
    from application_.db import people

    now = datetime.datetime.now()
    print(f'Today\'s date - {now.date()}')

    # help('modules')