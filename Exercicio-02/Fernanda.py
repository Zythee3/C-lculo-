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
    def area_sob_curva_demanda(self):
        """
        Calcula a área sob a curva de demanda usando integração numérica, que representa o gasto 
        total dos consumidores ao comprar uma quantidade específica do produto.
        
        Retorna:
            float: Área sob a curva de demanda.
        """
        return integrate.simps(self.quantidades, self.precos)

    precos = [num for num in range(100, 10, -5)]
    quantidades = [num / 100.0 for num in range(40, 400, 20)]

    modelo_elasticidade = ElasticidadeDemanda(precos, quantidades)


    area_curva_demanda = modelo_elasticidade.area_sob_curva_demanda()
    print("Área sob a curva de demanda:", -area_curva_demanda)