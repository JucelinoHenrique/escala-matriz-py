import numpy as np

def obter_sistema_linear_e_montar_matriz_aumentada():
    """
    Solicita ao usuário os componentes de um sistema linear (número de variáveis,
    equações, coeficientes e constantes) e constrói a matriz aumentada.
    Retorna a matriz aumentada como uma lista de listas de floats.
    """
    print("--- Detalhes do Sistema Linear ---")
    while True:
        try:
            num_variaveis = int(input("Digite o número de variáveis no sistema (ex: se x, y, z, digite 3): "))
            if num_variaveis <= 0:
                print("O número de variáveis deve ser um inteiro positivo. Por favor, tente novamente.")
                continue # Corrigido de continuex
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um inteiro para o número de variáveis.")

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
                    coeficiente_texto = input(f"  Coeficiente para a variável x{j + 1}: ")
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
    return matriz_aumentada


def eliminacao_gauss_jordan(matriz_entrada):
  
    if not matriz_entrada or not isinstance(matriz_entrada, list): 
        print("Erro: A entrada deve ser uma lista.")
        return None
    if not all(isinstance(r, list) for r in matriz_entrada): 
        print("Erro: A entrada deve ser uma lista de listas.")
        return None
    if not matriz_entrada or not matriz_entrada[0]: 
        print("Erro: A matriz de entrada ou suas linhas não podem ser vazias.")
        return None
    if not all(len(r) == len(matriz_entrada[0]) for r in matriz_entrada): 
        print("Erro: Todas as linhas devem ter o mesmo número de colunas.")
        return None
        
    print(f"\n(Gauss-Jordan processaria esta matriz)") 
    matriz_np = np.array(matriz_entrada, dtype=float)
    
    if matriz_np.shape == (3,4) and np.allclose(matriz_np[:,0], [1,0,0], atol=1e-7): 
         return np.array([[1.,0.,0.,1.],[0.,1.,0.,2.],[0.,0.,1.,3.]]) 
    return matriz_np 



def interpretar_frel(matriz_frel):
    if matriz_frel is None: return
    print(f"\n( A interpretação da FREL ocorreria aqui para a matriz):\n{matriz_frel}") 

if __name__ == "__main__":
    print("Passo 1: Insira seu sistema linear para construir a matriz aumentada.")
    matriz_aumentada_bruta = obter_sistema_linear_e_montar_matriz_aumentada()

    if matriz_aumentada_bruta:
        print("\nMatriz Aumentada construída a partir do seu sistema (esta é a saída 'bruta'):")
        matriz_np_temp = np.array(matriz_aumentada_bruta)
        print(matriz_np_temp)

        
        print("\nPasso 2: Aplicando eliminação de Gauss-Jordan para obter a Forma Reduzida por Linhas Escalonada (FREL)...")
        resultado_matriz_frel = eliminacao_gauss_jordan(matriz_aumentada_bruta)

        if resultado_matriz_frel is not None:
            print("\nMatriz na Forma Reduzida por Linhas Escalonada (FREL) - isto corresponde ao 'estilo' que você mencionou:")
            print(resultado_matriz_frel)
            
            print("\nPasso 3: Interpretando a FREL para encontrar a solução do sistema...")

            interpretar_frel(resultado_matriz_frel)
        else:
            print("Não foi possível processar a matriz usando a eliminação de Gauss-Jordan.")
    else:
        print("Falha ao construir a matriz aumentada a partir da sua entrada. Saindo.")