zodis = str(input("Enter you text: "))
# informacijos šaltinis: https://bobbyhadz.com/blog/python-replace-multiple-characters-in-string

# masyvas iš raidžių 
leep_replacements =[
    ('A','4'),('a','@'),('B','8'),('b','|3'),('C','<'),('c','['),('E','3'),('e','€'),('F','7'),('f','|='),('G','9'),('g','6'),('H','#'),('h','[-]'),
    ('I','1'),('i','!'),('J','_|'),('j','_)'),('K','1<'),('k','|<'),('L','|_'),('l','|'),('M','44'),('m','^^'),('N','|\|'),('n','/\/'),('O','0'),('o','()'),
    ('P','|0'),('p','|>'),('Q','O'),('q','kw'),('R','|2'),('r','12'),('S','5'),('s','$'),('T','7'),('t','~|~'),('U','|_|'),('u','[_]'),('V','\/'),('v','\/'),
    ('W','\^/'),('w','2u'),('X','%'),('x','><'),('Y','`/'),('y','\|/'),('Z','5'),('z','7_')
]
for char, replacement in leep_replacements: 
    if char in zodis:
        zodis = zodis.replace(char, replacement)
        
print(zodis)
