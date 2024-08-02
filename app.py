from modelos.restaurante import Restaurante
from cardapio.bebida import Bebida
from cardapio.prato import Prato
from cardapio.sobremesa import Sobremesa

restaurante_feijoada = Restaurante('Feijoada', 'Gourmet')
bebida_energetico = Bebida('Baly', 14.90, '2 litros')
prato_sanduiche = Prato('Sanduíche', 14.90, 'Melhor quando é grátis')
sobremesa_brigadeiro = Sobremesa('Brigadeiro', 2.00, 'Doce', '20 gramas')
bebida_energetico.aplicar_desconto()
prato_sanduiche.aplicar_desconto()
sobremesa_brigadeiro.aplicar_desconto()
restaurante_feijoada.adicionar_no_cardapio(bebida_energetico)
restaurante_feijoada.adicionar_no_cardapio(prato_sanduiche)
restaurante_feijoada.adicionar_no_cardapio(sobremesa_brigadeiro)


def main():
    restaurante_feijoada.exibir_cardapio

if __name__ == '__main__':
    main()