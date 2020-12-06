import fileinput

lines = [line.strip() for line in fileinput.input() ]
lines.append("")
s=set()
p1=0
new = True
for line in lines:
    if not line:
        print(s)
        p1 += len(s)
        s = set()
        new = True
    else:
        if new:
            s = set([c for c in line])
            new = False
        else:
            s = s.intersection([c for c in line])
        
        
print(p1)