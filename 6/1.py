import fileinput

lines = [line.strip() for line in fileinput.input() ]
lines.append("")
s=set()
p1=0
for line in lines:
    if not line:
        print(s)
        p1 += len(s)
        s = set()
    else:
        for c in line:
            s.add(c)
        
print(p1)