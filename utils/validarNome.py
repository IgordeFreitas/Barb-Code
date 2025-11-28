import re

def validarNome(nome):
    padrao = r'^[A-Za-zÁ-ÿá-ÿ\s]+$'

    if re.match(padrao, nome):
        return True
    else:
        return False