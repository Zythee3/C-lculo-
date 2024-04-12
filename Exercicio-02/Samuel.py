import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

class ElasticidadeDemanda:
    def __init__(self, precos, quantidades):
        """
        Inicializa a classe ElasticidadeDemanda com os dados de preços e quantidades.
        
        Args:
            precos (list): Lista dos preços dos produtos.
            quantidades (list): Lista das quantidades vendidas correspondentes aos preços.
        """
        self.precos = np.array(precos)
        self.quantidades = np.exp(np.array(quantidades))
    
    def elasticidade_preco_demanda(self):
        """
        Calcula a elasticidade-preço da demanda, que mede a sensibilidade da quantidade demandada 
        em resposta a uma mudança no preço do produto.
        
        Retorna:
            numpy.ndarray: Array contendo as elasticidades-preço da demanda.
        """
        # Calcula a variação percentual na quantidade do produto seguindo a formula (Q2 - Q1) / Q1
        delta_quantidade = (self.quantidades[1:] - self.quantidades[:-1]) / self.quantidades[:-1]

        # Calcula a variação percentual no preço do produto seguindo a formula (P2 - P1) / P1
        delta_preco = (self.precos[1:] - self.precos[:-1]) / self.precos[:-1]
        
        # Calcula a elasticidade-preço da demanda seguindo a formula (Q2 - Q1) / Q1 / (P2 - P1) / P1
        elasticidades = -delta_quantidade / delta_preco

        return elasticidades
    
    def area_sob_curva_demanda(self):
        """
        Calcula a área sob a curva de demanda usando integração numérica, que representa o gasto 
        total dos consumidores ao comprar uma quantidade específica do produto.
        
        Retorna:
            float: Área sob a curva de demanda.
        """
        return integrate.simps(self.quantidades, self.precos)

    
    def plotar_elasticidade_demanda(self):
        """
        Cria o gráfico da elasticidade-preço da demanda em relação ao preço.
        """
        elasticidades = self.elasticidade_preco_demanda()
        plt.plot(self.precos[:-1], elasticidades, marker='o', linestyle='-')
        plt.title('Elasticidade-preço da Demanda')
        plt.xlabel('Preço')
        plt.ylabel('Elasticidade')
        plt.grid(True)
        plt.legend(['Elasticidade-preço da Demanda'])

    def plotar_curva_demanda(self):
        """
        Cria o gráfico da curva de demanda em relação ao preço.
        """
        plt.plot(self.precos, self.quantidades, marker='o', linestyle='-', color='r')
        plt.fill_between(self.precos, self.quantidades, color='r', alpha=0.15)
        plt.title('Curva de Demanda')
        plt.xlabel('Preço')
        plt.ylabel('Quantidade')
        plt.grid(True)
        plt.legend(['Demanda'])


# Dados de exemplo
if __name__ == "__main__":
    # Exemplo de dados de preços e quantidades vendidas
    precos = [num for num in range(100, 10, -5)]
    quantidades = [num / 100.0 for num in range(40, 400, 20)]
    print(quantidades)
    # Cria uma instância da classe ElasticidadeDemanda com os dados de exemplo
    modelo_elasticidade = ElasticidadeDemanda(precos, quantidades)

    # Calcula a área sob a curva de demanda
    area_curva_demanda = modelo_elasticidade.area_sob_curva_demanda()
    print("Área sob a curva de demanda:", -area_curva_demanda)
    print()
    # Plota os dois gráficos juntos
    plt.figure(figsize=(10, 5), facecolor='#DCDCDC')
    plt.subplot(1, 2, 1)  # Subplot para a elasticidade-preço da demanda
    modelo_elasticidade.plotar_elasticidade_demanda()
    plt.subplot(1, 2, 2)  # Subplot para a curva de demanda
    modelo_elasticidade.plotar_curva_demanda()
    
    # Exibe os gráficos

    plt.tight_layout()
    plt.show()
