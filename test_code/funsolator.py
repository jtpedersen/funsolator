import sys
import re

from enum import Enum


class State(Enum):
    PRE = 0
    TRIGGERED = 1
    IN_SCOPE = 2
    OUT_OF_SCOPE = 3

def extract(filename, signature):
    res = ""
    state = State.PRE
    level = 0
    for line in  open(filename, 'r'):
        #print(f'{level}:{state}\t{line.strip()}')

        if signature in line:
            state = State.TRIGGERED
        if state == State.PRE:
            continue

        res += line
        if '{' in line:
            level += 1
            if state == State.TRIGGERED:
                state = State.IN_SCOPE
        if '}' in line:
            level -= 1;

        if state == State.IN_SCOPE and level == 0:
            state = State.OUT_OF_SCOPE;

        if state == State.OUT_OF_SCOPE:
            return res

    return res;



def process_template(beast, template):
    p = re.compile('FUNSOLATE\("(.*)"\)')
    for line in open(template, 'r'):
        m = p.match(line)
        if m:
            signature = m.group(1)
            print(extract(beast, signature))
        else:
            print(line.strip());


if __name__ == "__main__":
    process_template(sys.argv[1], sys.argv[2])
