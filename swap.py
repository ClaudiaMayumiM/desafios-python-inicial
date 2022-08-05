

''' DESAFIO - 
Recebe uma string como parâmetro e a retorna ao inverso,
onde as letras maiúsculas são retornadas como minúsculas e vice-versa.

Exemplo:

Input: "OLAtudoBEM"

Output: "olaTUDObem"

'''


def swap_case(s):
    
    modified = []
    
    splited = list(s)
    
    for l in splited:
        if l.isupper():
            modified.append(l.lower())
        else:
            modified.append(l.upper())
    
    new_string = "".join(modified)
    
    return new_string


print(swap_case("ClAuDiA"))
