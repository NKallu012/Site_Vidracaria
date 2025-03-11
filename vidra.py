"""
Este programa permite aos usuários realizarem orçamentos de espelhos e boxes de vidro
de forma rápida e prática. O usuário pode escolher o tipo de serviço,
configurar os detalhes (tipo de vidro, espessura, kits, etc.) e obter um preço estimado.
"""

# DICIONÁRIOS
vidros = {
    1: {"descricao": "Vidro Incolor", "opcoes": {1: {"descricao": "Vidro Incolor 6mm", "preco": 80.00}, 2: {"descricao": "Vidro Incolor 8mm", "preco": 100.00}, 3: {"descricao": "Vidro Incolor 10mm", "preco": 120.00}}},
    2: {"descricao": "Vidro Pintado", "opcoes": {1: {"descricao": "Vidro Pintado 6mm", "preco": 100.00}, 2: {"descricao": "Vidro Pintado 8mm", "preco": 130.00}, 3: {"descricao": "Vidro Pintado 10mm", "preco": 160.00}}},
    3: {"descricao": "Vidro Jateado", "opcoes": {1: {"descricao": "Vidro Jateado 6mm", "preco": 110.00}, 2: {"descricao": "Vidro Jateado 8mm", "preco": 140.00}, 3: {"descricao": "Vidro Jateado 10mm", "preco": 170.00}}},
    4: {"descricao": "Vidro Fumê", "opcoes": {1: {"descricao": "Vidro Fumê 6mm", "preco": 120.00}, 2: {"descricao": "Vidro Fumê 8mm", "preco": 150.00}, 3: {"descricao": "Vidro Fumê 10mm", "preco": 180.00}}},
    5: {"descricao": "Vidro Verde", "opcoes": {1: {"descricao": "Vidro Verde 6mm", "preco": 130.00}, 2: {"descricao": "Vidro Verde 8mm", "preco": 160.00}, 3: {"descricao": "Vidro Verde 10mm", "preco": 190.00}}},
    6: {"descricao": "Vidro Refletivo", "opcoes": {1: {"descricao": "Vidro Refletivo 6mm", "preco": 150.00}, 2: {"descricao": "Vidro Refletivo 8mm", "preco": 180.00}, 3: {"descricao": "Vidro Refletivo 10mm", "preco": 210.00}}}
}
#   BOX
kitbox_canto = {
    1: {"descricao": "Kit Branco (Canto)", "preco": {1.00: 120, 1.20: 140, 1.33: 153, 1.40: 160, 1.50: 170, 1.80: 200, 2.00: 220, 2.10: 230, 2.20: 240}},     # PREÇO DO KIT POR TAMANHO
    2: {"descricao": "Kit Azul (Canto)", "preco": {1.00: 220, 1.20: 240, 1.33: 253, 1.40: 260, 1.50: 270, 1.80: 300, 2.00: 320, 2.10: 330, 2.20: 340}},                        
    3: {"descricao": "Kit Verde (Canto)", "preco": {1.00: 320, 1.20: 340, 1.33: 353, 1.40: 360, 1.50: 370, 1.80: 400, 2.00: 420, 2.10: 430, 2.20: 440}},      
    4: {"descricao": "Kit Preto (Canto)", "preco": {1.00: 420, 1.20: 440, 1.33: 453, 1.40: 460, 1.50: 470, 1.80: 500, 2.00: 520, 2.10: 530, 2.20: 540}},
    5: {"descricao": "Kit Vermelho (Canto)", "preco": {1.00: 520, 1.20: 540, 1.33: 553, 1.40: 560, 1.50: 570, 1.80: 600, 2.00: 620, 2.10: 630, 2.20: 640}},
}

kitbox_frontal = {
    1: {"descricao": "Kit Branco (Frontal)", "preco": {1.00: 100, 1.20: 120, 1.33: 133, 1.40: 140, 1.50: 150, 1.80: 180, 2.00: 200}},     # PREÇO DO KIT POR TAMANHO
    2: {"descricao": "Kit Azul (Frontal)", "preco": {1.00: 200, 1.20: 220, 1.33: 233, 1.40: 240, 1.50: 250, 1.80: 280, 2.00: 300}},
    3: {"descricao": "Kit Verde (Frontal)", "preco": {1.00: 300, 1.20: 320, 1.33: 333, 1.40: 340, 1.50: 350, 1.80: 380, 2.00: 400}},
    4: {"descricao": "Kit Preto (Frontal)", "preco": {1.00: 400, 1.20: 420, 1.33: 433, 1.40: 440, 1.50: 450, 1.80: 480, 2.00: 500}},
    5: {"descricao": "Kit Vermelho (Frontal)", "preco": {1.00: 500, 1.20: 520, 1.33: 533, 1.40: 540, 1.50: 550, 1.80: 580, 2.00: 600}},
}

tipo_box = {
    1: {"descricao": "Box de Canto", "kits": kitbox_canto},
    2: {"descricao": "Box Frontal", "kits": kitbox_frontal},
}

formato_box = {
    1: {"descricao": "Reto"},         # NÃO ALTERAM O VALOR DO BOX
    2: {"descricao": "Redondo"},
}
#  ESPELHO
espessura_espelho = {
    1: {"descricao": "(3mm)", "preco": 20.00},   # VALOR POR M²
    2: {"descricao": "(4mm)", "preco": 30.00},
    3: {"descricao": "(5mm)", "preco": 40.00},
}

tipos_espelho = {
    1: {"descricao": "Comum sem acabamento", "preco": 50.00},          # VALOR POR M² DE CADA TIPO DE ACABAMENTO
    2: {"descricao": "Comum com acabamento", "preco": 60.00},
    3: {"descricao": "Comum com acabamento bisote", "preco": 70.00},
    4: {"descricao": "Redondo/oval sem acabamento", "preco": 80.00},
    5: {"descricao": "Redondo/oval com acabamento", "preco": 90.00},
    6: {"descricao": "Redondo/oval com acabamento bisote", "preco": 100.00},
}
#  JANELAS
kits_janela = {
    1: {"descricao": "Kit Branco", "opcoes": {1: {"descricao": "Bate e Fecha", "preco": 150}, 2: {"descricao": "Com Chave", "preco": 200}}},
    2: {"descricao": "Kit Preto", "opcoes": {1: {"descricao": "Bate e Fecha", "preco": 160}, 2: {"descricao": "Com Chave", "preco": 210}}},
    3: {"descricao": "Kit Bronze", "opcoes": {1: {"descricao": "Bate e Fecha", "preco": 170}, 2: {"descricao": "Com Chave", "preco": 220}}},
    4: {"descricao": "Kit Fosco", "opcoes": {1: {"descricao": "Bate e Fecha", "preco": 180}, 2: {"descricao": "Com Chave", "preco": 230}}},
}
  
tipos_fecho = {
    1: {"descricao": "Bate e Fecha", "kits": kits_janela},
    2: {"descricao": "Com Chave", "kits": kits_janela},
}    

opcoes_orcamentos = {
    1: {"descricao": "Espelhos", "modelos_espelho": tipos_espelho},
    2: {"descricao": "Box (canto, frontal)", "tipos_box": tipo_box},
    3: {"descricao": "Janelas", "tipos_fecho": tipos_fecho},
}

# FUNÇÕES
def exibir_menu(opcoes, mensagem):
    # EXIBE UM MENU DE OPÇÕES E RETORNA A ESCOLHA DO USUÁRIO
    """
    Exibe um menu de opções e solicita uma escolha do usuário.
    
    Parâmetros:
        opcoes (dict): Dicionário contendo as opções disponíveis.
        mensagem (str): Mensagem para instruir o usuário.
    
    Retorna:
        dict: O item escolhido pelo usuário.
    """
    while True:
        print(mensagem)
        for chave, valor in opcoes.items():
            print(f"{chave} - {valor['descricao']}")
        try:
            escolha = int(input("Digite o número correspondente: "))
            if escolha in opcoes:
                return opcoes[escolha]
            else:
                print(f"Opção inválida! Por favor, digite um número entre {min(opcoes)} e {max(opcoes)}.")
        except ValueError:
            print("Entrada inválida! Por favor, digite um número.")

def exibir_menu_orcamentos(opcoes):
    # EXIBE O MENU DE TIPOS DE ORÇAMENTO E RETORNA A ESCOLHA DO USUÁRIO
    while True:
        print("Escolha o tipo de orçamento:")
        for chave, valor in opcoes.items():
            print(f"{chave} - {valor['descricao']}")
        try:
            escolha = int(input("Digite o número correspondente: "))
            if escolha in opcoes:
                return opcoes[escolha]
            else:
                print(f"Opção inválida! Por favor, digite um número entre {min(opcoes)} e {max(opcoes)}.")
        except ValueError:
            print("Entrada inválida! Por favor, digite um número.")

def obter_largura(larguras_disponiveis, largura_usuario):
    # RETORNA A MENOR LARGURA DISPONÍVEL QUE SEJA MAIOR OU IGUAL À LARGURA DO USUÁRIO
    """
    Retorna a menor largura disponível que seja maior ou igual à informada pelo usuário.
    
    Parâmetros:
        larguras_disponiveis (list): Lista de larguras disponíveis.
        largura_usuario (float): Largura informada pelo usuário.
    
    Retorna:
        float: Largura correspondente mais próxima.
    """
    for medida in sorted(larguras_disponiveis):
        if medida >= largura_usuario:
            return medida
    return max(larguras_disponiveis)

def calcular_preco(altura, largura, preco_vidro, preco_kit):
    # CALCULA O PREÇO FINAL COM BASE NA ALTURA, LARGURA, PREÇO DO VIDRO E PREÇO DO KIT
    """
    Calcula o preço final do produto.
    
    Parâmetros:
        altura (float): Altura do vidro em metros.
        largura (float): Largura do vidro em metros.
        preco_vidro (float): Preço do vidro por metro quadrado.
        preco_kit (float): Preço do kit escolhido.
    
    Retorna:
        float: Valor total do produto.
    """
    area = (altura * largura) + 0.05  # ADICIONA 5CM DO TRANSPASSE DOS VIDROS
    return area * preco_vidro + preco_kit

# LÓGICA PRINCIPAL
opcoes_orcamentos = exibir_menu_orcamentos(opcoes_orcamentos)

if opcoes_orcamentos["descricao"] == "Espelhos":
    # SE O USUÁRIO ESCOLHEU ESPELHOS, EXIBE O MENU DE TIPOS DE ESPELHO
    tipos_espelho = opcoes_orcamentos["modelos_espelho"]
    espelho_escolhido = exibir_menu(tipos_espelho, "Escolha o tipo de espelho:")
    if not espelho_escolhido:
        print("Opção inválida!")
        exit()

    # EXIBE O MENU DE ESPESSURAS DE ESPELHO
    espessura_escolhida = exibir_menu(espessura_espelho, "Escolha a espessura do espelho:")
    if not espessura_escolhida:
        print("Opção inválida!")
        exit()

    # SOLICITA A ALTURA E LARGURA DO ESPELHO AO USUÁRIO
    altura_espelho = float(input("Digite a altura do espelho: "))
    largura_espelho = float(input("Digite a largura do espelho: "))

    # CALCULA O PREÇO FINAL DO ESPELHO
    preco_final = calcular_preco(altura_espelho, largura_espelho, espelho_escolhido["preco"], espessura_escolhida["preco"])
    print(f"\nO valor total do seu espelho é de R${preco_final:.2f}")

elif opcoes_orcamentos["descricao"] == "Box (canto, frontal)":
    # SE O USUÁRIO ESCOLHEU BOX, EXIBE O MENU DE TIPOS DE BOX
    tipo_box = opcoes_orcamentos["tipos_box"]
    tipo_box_escolhido = exibir_menu(tipo_box, "Escolha o tipo de box:")
    if not tipo_box_escolhido:
        print("Opção inválida!")
        exit()

    # EXIBE O MENU DE FORMATOS DE BOX
    formato_box = exibir_menu(formato_box, "Escolha o formato do box:")
    if not formato_box:
        print("Opção inválida!")
        exit()

    # EXIBE O MENU DE TIPOS DE VIDRO
    vidro_escolhido = exibir_menu(vidros, "Escolha o tipo de vidro:")
    if not vidro_escolhido:
        print("Opção inválida!")
        exit()

    # EXIBE O MENU DE CORES DE KIT
    kit_escolhido = exibir_menu(tipo_box_escolhido["kits"], "Escolha a cor do kit:")
    if not kit_escolhido:
        print("Opção inválida!")
        exit()

    # SOLICITA A LARGURA TOTAL DO BOX AO USUÁRIO
    largura_total = float(input("Digite a largura total do box: "))
    if largura_total > 2.20:  # VERIFICA SE O BOX É MAIOR QUE O PADRÃO
        print("\n🚨 **Box fora do padrão** 🚨")
        print("Boxes com largura superior a 2.20 metros requerem um orçamento personalizado.")
        print("Entre em contato conosco pelo telefone (XX) XXXX-XXXX ou pelo email contato@vidracaria.com.")
        exit()

    # OBTÉM A LARGURA APROXIMADA DISPONÍVEL
    larguras_disponiveis = kit_escolhido["preco"].keys()
    largura_aproximada = obter_largura(larguras_disponiveis, largura_total)

    # CALCULA O VALOR TOTAL DO BOX
    valor_total = calcular_preco(
        1.90,
        largura_aproximada,
        vidro_escolhido["preco"],
        kit_escolhido["preco"][largura_aproximada]
    )
    # IMPRIME O VALOR TOTAL
    print(f"\nO valor total do seu box é de R${valor_total:.2f}")

elif opcoes_orcamentos["descricao"] == "Janelas":
    # SE O USUÁRIO ESCOLHEU JANELAS, EXIBE O MENU DE TIPOS DE JANELAS E O FECHO
    tipos_janelas = opcoes_orcamentos["tipos_fecho"]
    janela_escolhida = exibir_menu(tipos_janelas, "Escolha o tipo de janela:")
    if not janela_escolhida:
        print("Opção inválida!")
        exit()

    # EXIBE O MENU DE TIPOS DE VIDRO
    vidro_escolhido = exibir_menu(vidros, "Escolha o tipo de vidro:")
    if not vidro_escolhido:
        print("Opção inválida!")
        exit()

    # EXIBE O MENU DE TIPOS DE KIT

    # SOLICITA A LARGURA E ALTURA DA JANELA AO USUÁRIO
    largura_janela = float(input("Digite a largura da janela: "))
    altura_janela = float(input("Digite a altura da janela: "))

    # OBTÉM A LARGURA APROXIMADA DISPONÍVEL
    larguras_disponiveis = janela_escolhida["preco"].keys()
    largura_aproximada = obter_largura(larguras_disponiveis, largura_janela)

    # CALCULA O VALOR TOTAL DA JANELA
    valor_total = calcular_preco(
        altura_janela,
        largura_aproximada,
        vidro_escolhido["preco"],
        janela_escolhida["preco"][largura_aproximada]
    )
    # IMPRIME O VALOR TOTAL
    print(f"\nO valor total da sua janela é de R${valor_total:.2f}")
