import numpy as np

def obter_sistema_linear_e_montar_matriz_aumentada():
    """
    Solicita ao usuário os componentes de um sistema linear (número de variáveis,
    equações, coeficientes e constantes) e constrói a matriz aumentada.
    Retorna a matriz aumentada como uma lista de listas de floats e o número de variáveis.
    """
    print("--- Detalhes do Sistema Linear ---")
    num_variaveis = 0 
    while True:
        try:
            num_variaveis = int(input("Digite o número de variáveis no sistema (ex: se x, y, z, digite 3): "))
            if num_variaveis <= 0:
                print("O número de variáveis deve ser um inteiro positivo. Por favor, tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um inteiro para o número de variáveis.")

    # Define os nomes das variáveis para os prompts de entrada
    nomes_variaveis_prompt = []
    if num_variaveis == 1:
        nomes_variaveis_prompt = ['x']
    elif num_variaveis == 2:
        nomes_variaveis_prompt = ['x', 'y']
    elif num_variaveis == 3:
        nomes_variaveis_prompt = ['x', 'y', 'z']
    else: # Para 0 ou mais de 3 variáveis
        nomes_variaveis_prompt = [f"x{k + 1}" for k in range(num_variaveis)]

    while True:
        try:
            num_equacoes = int(input(f"Digite o número de equações no sistema: "))
            if num_equacoes <= 0:
                print("O número de equações deve ser um inteiro positivo. Por favor, tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um inteiro para o número de equações.")

    matriz_aumentada = []
    print("\nPara cada equação, digite os coeficientes de cada variável e o termo constante.")

    for i in range(num_equacoes): 
        print(f"\n--- Equação {i + 1} ---")
        linha = []
    
        for j in range(num_variaveis): 
            while True:
                try:
                    # Usa o nome da variável definido acima para o prompt
                    nome_var_atual_prompt = nomes_variaveis_prompt[j] if j < len(nomes_variaveis_prompt) else f"var_desconhecida_{j+1}"
                    coeficiente_texto = input(f"  Coeficiente para a variável {nome_var_atual_prompt}: ")
                    coeficiente = float(coeficiente_texto)
                    linha.append(coeficiente)
                    break
                except ValueError:
                    print("  Entrada inválida. Por favor, digite um valor numérico para o coeficiente.")
        
        while True:
            try:
                constante_texto = input(f"  Termo constante para a Equação {i + 1} (lado direito da igualdade): ")
                constante = float(constante_texto)
                linha.append(constante)
                break
            except ValueError:
                print("  Entrada inválida. Por favor, digite um valor numérico para o termo constante.")
        
        matriz_aumentada.append(linha)
        
    print("\n--- Entrada do Sistema Concluída ---")
    return matriz_aumentada, num_variaveis

def exibir_matriz_como_expressoes(matriz_arg, num_variaveis):
    """
    Exibe a matriz (que pode ser aumentada ou RREF) no formato de expressões lineares.
    Usa x, y, z para 3 variáveis, x, y para 2, x para 1, e x1, x2... para outros casos.
    """
    if matriz_arg is None:
        print("Matriz fornecida é None (inválida ou erro anterior), nada para exibir como expressões.")
        return

    matriz_lista = []
    if isinstance(matriz_arg, np.ndarray):
        matriz_lista = matriz_arg.tolist()
    elif isinstance(matriz_arg, list):
        matriz_lista = matriz_arg
    else:
        print("Tipo de matriz não suportado para exibição como expressões.")
        return

    if not matriz_lista:
        print("Matriz vazia, nada para exibir como expressões.")
        return
    if not all(isinstance(r, list) for r in matriz_lista):
        print("Formato de matriz_lista inválido (esperado lista de listas) para exibir como expressões.")
        return

    # Definir nomes das variáveis com base em num_variaveis para a exibição
    nomes_variaveis_exibicao = []
    if num_variaveis == 1:
        nomes_variaveis_exibicao = ['x']
    elif num_variaveis == 2:
        nomes_variaveis_exibicao = ['x', 'y']
    elif num_variaveis == 3:
        nomes_variaveis_exibicao = ['x', 'y', 'z']
    else: 
        nomes_variaveis_exibicao = [f"x{k + 1}" for k in range(num_variaveis)]

    print("\nRepresentação do sistema como expressões lineares:")
    for linha_idx, linha_valores in enumerate(matriz_lista):
        if not isinstance(linha_valores, list):
            print(f"Atenção: Linha {linha_idx+1} não é uma lista e será ignorada.")
            continue

        if len(linha_valores) != num_variaveis + 1:
            print(f"Atenção: Linha {linha_idx+1} tem {len(linha_valores)} elementos, esperado {num_variaveis + 1}. Não pode ser formatada corretamente.")
            print(f"  Linha com problema: {linha_valores}") 
            continue

        termos_lhs = [] 
        for i in range(num_variaveis):
            coeficiente = linha_valores[i]
            if coeficiente == int(coeficiente):
                coef_str = str(int(coeficiente))
            else:
                coef_str = f"{coeficiente:.4g}".rstrip('0').rstrip('.') if '.' in f"{coeficiente:.4g}" else f"{coeficiente:.4g}"
            
            # Usar o nome da variável da lista predefinida para exibição
            nome_var_atual_exibicao = nomes_variaveis_exibicao[i] if i < len(nomes_variaveis_exibicao) else f"var_desconhecida_{i+1}" 
            termos_lhs.append(f"{coef_str}{nome_var_atual_exibicao}")
        
        termo_constante = linha_valores[num_variaveis]
        if termo_constante == int(termo_constante):
            const_str = str(int(termo_constante))
        else:
            const_str = f"{termo_constante:.4g}".rstrip('0').rstrip('.') if '.' in f"{termo_constante:.4g}" else f"{termo_constante:.4g}"

        string_linha = f"[{', '.join(termos_lhs)} | {const_str}]"
        print(string_linha)

# SEU CÓDIGO PLACEHOLDER PARA eliminacao_gauss_jordan
def eliminacao_gauss_jordan(matriz_entrada):
    if not matriz_entrada or not isinstance(matriz_entrada, list): 
        print("Erro: A entrada para Gauss-Jordan deve ser uma lista.")
        return None
    if not all(isinstance(r, list) for r in matriz_entrada): 
        print("Erro: A entrada para Gauss-Jordan deve ser uma lista de listas.")
        return None
    if matriz_entrada and (len(matriz_entrada) > 0 and not matriz_entrada[0]): # Verificação se a primeira linha é vazia
        print("Erro: Linhas na matriz de entrada não podem ser vazias se a matriz não for vazia.")
        return None
    if matriz_entrada and len(matriz_entrada[0]) > 0 and not all(len(r) == len(matriz_entrada[0]) for r in matriz_entrada): 
        print("Erro: Todas as linhas devem ter o mesmo número de colunas.")
        return None
        
    print(f"\n(Gauss-Jordan processaria esta matriz)") 
    matriz_np = np.array(matriz_entrada, dtype=float)
    
    print(f"Matriz recebida por Gauss-Jordan (antes do processamento placeholder):\n{matriz_np}")
    print("(Placeholder: Esta seria a matriz em RREF após Gauss-Jordan)")
    return matriz_np

# SEU CÓDIGO PLACEHOLDER PARA interpretar_frel
def interpretar_frel(matriz_frel):
    if matriz_frel is None: return
    print(f"\n(A interpretação da FREL ocorreria aqui para a matriz):\n{matriz_frel}") 

if __name__ == "__main__":
    print("Passo 1: Insira seu sistema linear para construir a matriz aumentada.")
    dados_retornados = obter_sistema_linear_e_montar_matriz_aumentada()
    
    matriz_aumentada_bruta = None
    num_vars_sistema = 0

    if dados_retornados:
        matriz_aumentada_bruta, num_vars_sistema = dados_retornados

    if matriz_aumentada_bruta:
        print("\nMatriz Aumentada construída (formato numérico):")
        matriz_np_temp = np.array(matriz_aumentada_bruta)
        print(matriz_np_temp)

        if num_vars_sistema > 0: # Só exibe se num_vars_sistema for válido
            exibir_matriz_como_expressoes(matriz_aumentada_bruta, num_vars_sistema)
        else: # Caso num_vars_sistema seja 0, o que não deveria acontecer se a entrada foi válida
            print("Número de variáveis é zero, não é possível exibir expressões de forma significativa.")

        
        print("\nPasso 2: Aplicando eliminação de Gauss-Jordan para obter a Forma Reduzida por Linhas Escalonada (FREL)...")
        resultado_matriz_frel = eliminacao_gauss_jordan(matriz_aumentada_bruta)

        if resultado_matriz_frel is not None: 
            print("\nMatriz na Forma Reduzida por Linhas Escalonada (FREL):")
            print(resultado_matriz_frel)
            
            if num_vars_sistema > 0:
                exibir_matriz_como_expressoes(resultado_matriz_frel, num_vars_sistema)
            else:
                print("Número de variáveis é zero, não é possível exibir expressões da FREL de forma significativa.")
            
            print("\nPasso 3: Interpretando a FREL para encontrar a solução do sistema...")
            interpretar_frel(resultado_matriz_frel)
        else:
            print("Não foi possível processar a matriz usando a eliminação de Gauss-Jordan (resultado foi None).")
    else:
        print("Falha ao obter os dados do sistema. Saindo.")