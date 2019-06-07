# Map-Coloring
CSP map coloring problem. give some color and da daaa

------------------

# Map
```
X: [A, B, C]
A: [X, K]
B: [D, X]
C: [X]
Z: [K]
K: [A, Z]
F: []
D: [B, G]
G: [D]

```
# Colors ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) ![#1589F0](https://placehold.it/15/1589F0/000000?text=+)  
```
colors = ['RED', 'GREEN'] 
```
# Result
```
{('A', True): [('X', 'RED'), ('K', 'RED')],
 ('B', True): [('X', 'RED'), ('D', 'RED')],
 ('C', True): [('X', 'RED')],
 ('D', True): [('B', 'GREEN'), ('G', 'GREEN')],
 ('F', True): ['Any Color'],
 ('G', True): [('D', 'RED')],
 ('K', True): [('A', 'GREEN'), ('Z', 'GREEN')],
 ('X', True): [('B', 'GREEN'), ('A', 'GREEN'), ('C', 'GREEN')],
 ('Z', True): [('K', 'RED')]}
```

# Attention Please :)
### I do not filter it to just show the cities and colors. How do I stop being so goddamn lazy???
