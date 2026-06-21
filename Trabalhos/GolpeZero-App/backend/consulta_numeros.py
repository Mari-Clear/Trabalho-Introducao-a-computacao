NUMEROS_SUSPEITOS = [
    "11999999999",
    "21988888888",
    "31977777777"
]
#Exemplos genericos de numeros

def verificar_numero(numero):
    
    if numero in NUMEROS_SUSPEITOS:
        return True

    return False
