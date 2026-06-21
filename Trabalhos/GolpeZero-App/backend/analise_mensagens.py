PALAVRAS_SUSPEITAS = {
    "pix": 20,
    "urgente": 15,
    "senha": 30,
    "clique aqui": 20,
    "banco": 15,
    "código": 25,
    "transferência": 20
}

def analisar_mensagem(mensagem):
    
    risco = 0
    
    mensagem = mensagem.lower()
    
    for palavra, peso in PALAVRAS_SUSPEITAS.items():
        if palavra in mensagem:
            risco += peso

    return risco
