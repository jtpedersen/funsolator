import sys
import re
import os
import random

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



def cpp_file(beast, template, name):
    res = f'#include "{name}.h"\n'
    p = re.compile('FUNSOLATE\("(.*)"\)')
    for line in open(template, 'r'):
        m = p.match(line)
        if m:
            signature = m.group(1)
            res += extract(beast, signature)

    return res

def include_guard(lines, name):
    guard = name + "_" + "".join([random.choice('0123456789abcdef') for x in range(16)])
    res = ""
    res += f'#ifndef {guard}\n'
    res += f'#define {guard}\n'
    res += lines
    res += f'#endif //{guard}\n'
    return res

def header_file(beast, template, name):
    res = ""
    p = re.compile('FUNSOLATE\("(.*)"\)')
    for line in open(template, 'r'):
        m = p.match(line)
        if m:
            signature = m.group(1)
            res += signature + ";\n"
        else:
            res +=line

    return include_guard(res, name)

def process_template(beast, template):
    folder = os.path.join(os.path.dirname(template), "tamed")
    name, _ = os.path.splitext(os.path.basename(template))
    if not os.path.exists(folder):
        os.mkdir(folder)
    with open(os.path.join(folder, f'{name}.cpp'), 'w') as f:
        f.write(cpp_file(beast, template, name))
    with open(os.path.join(folder, f'{name}.h'), 'w') as f:
        f.write(header_file(beast, template, name))


if __name__ == "__main__":
    process_template(sys.argv[1], sys.argv[2])
