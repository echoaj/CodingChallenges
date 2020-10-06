#codewars.com

'''
In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)
'''

alph_dict = {'A':"1",
             'B':"2",
             'C':"3",
             'D':"4",
             'E':"5",
             'F':"6",
             'G':"7",
             'H':"8",
             'I':"9",
             'J':"10",
             'K':"11",
             'L':"12",
             'M':"13",
             'N':"14",
             'O':"15",
             'P':"16",
             'Q':"17",
             'R':"18",
             'S':"19",
             'T':"20",
             'U':"21",
             'V':"22",
             'W':"23",
             'X':"24",
             'Y':"25",
             'Z':"26"
             }

def alphabet_position(l):
    l = list(l.upper())
    size = len(l)
    for i in range(size):
        if l[i] in alph_dict:
            l[i] = alph_dict.get(l[i]) + ' '
        else:
            l[i] = ''

    l = ''.join(l)
    l = l[:-1]
    return l

print(alphabet_position("This is a Normal string!"))
print(alphabet_position("Â´ÈR2?<¶2q'UcÁ±Ã7°]ÂkÊ|e__o5ÏsB6,31QZ!Í-ÁFn±~%I»­±fZ»gv}r[[/-ÉuB(Î<w{P¤iºBjªy4¤fA"))



'''
def alphabet_positions(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())

print(alphabet_position("This is a Normal string!"))
print(alphabet_positions("Â´ÈR2?<¶2q'UcÁ±Ã7°]ÂkÊ|e__o5ÏsB6,31QZ!Í-ÁFn±~%I»­±fZ»gv}r[[/-ÉuB(Î<w{P¤iºBjªy4¤fA"))
'''