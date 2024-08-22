import os
import json
import threading
import time

def __get_spinners():
    root = os.path.dirname(__file__)
    loadfile = os.path.join(root, 'spinners.json')
    with open(loadfile, 'r', encoding='utf-8') as lf:
        return json.loads(lf.read())

def load(target, desc:str = '', pos:str = 'start', index:str = 'dots2', args:tuple=()):
    if pos.lower() not in ['start', 'end']:
        raise ValueError(f'Unknown position "{pos}".')
    
    if desc:
        desc = desc + ' '
    
    t = threading.Thread(target = target, args = args)
    t.start()

    spinners = __get_spinners()

    while t.is_alive():
        interval = (spinners[index]['interval'] / 1000)
        frames = spinners[index]['frames']

        for frame in frames:
            if pos.lower() == 'start':
                print('\r' + frame + f' {desc}', flush=True, end='')
            elif pos.lower() == 'end':
                print('\r' + desc + f'{frame} ', flush=True, end='')
            time.sleep(interval)

    print()