import fileinput
import re

lines = [line.strip() for line in fileinput.input()]

block_search = re.compile(r'\([0-9\s+*]+\)')

def special_eval(eqn, new_order=False):
    elements = eqn.split()
    next_operator = ""
    if new_order:
        while "+" in elements:
            i = elements.index("+")
            sub_result = eval( "".join( elements[i-1:i+2] ) )
            elements = elements[:i-1] + [str(sub_result)] + elements[i+2:]
    total = int(elements[0])
    for elem in elements[1:]:
        if elem.isnumeric():
            total = eval(str(total) + next_operator + elem)
        else:
            next_operator = elem
    return total

part = 1 
for fn in [lambda x: special_eval(x), lambda x: special_eval(x, new_order=True)]:
    results = []
    for line in lines:
        while "(" in line:
            s = block_search.search(line)
            if s:
                to_process = s.group(0).strip("()")
                sub_result = str(fn(to_process))
                new_line = line[:s.start()] + sub_result + line[s.end():]
                line = new_line
        result = fn(line)
        results.append(result)
    print(f"Part {part} {sum(results)}")
    part += 1    
