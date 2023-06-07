# Compara o valor de uma ação da bolsa de valores para saber se está abaixo de um valor pré determinado...

## explicação linha a linha:

import yfinance as yf: Importa a biblioteca yfinance e a renomeia para 'yf' para ser mais fácil de usar no código.

from datetime import datetime: Importa a classe datetime da biblioteca datetime.

today = datetime.today().strftime('%Y-%m-%d'): Cria uma variável 'today' que recebe a data de hoje em formato de string no padrão 'ano-mês-dia'.

tickerData = yf.Ticker(tickerSymbol): Cria uma variável 'tickerData' que recebe os dados da ação especificada pelo 'tickerSymbol' com a ajuda da biblioteca yfinance.

tickerDF = tickerData.history(period='1d', start='2010-1-1', end=today): Cria uma variável 'tickerDF' que recebe os dados históricos da ação especificada dentro do período indicado(e mudando a variável 'today' para obter informações do dia atual).

current_price = tickerDF["Close"].iloc[-1]: Cria uma variável 'current_price' que pega o último preço de fechamento da ação contido na coluna 'Close' do DataFrame.

return current_price: Retorna o valor da variável 'current_price' para utilização fora da função.

tickerSymbol = 'PETR4.SA': Define o ticker da ação da Petrobras como 'PETR4.SA' para busca dos dados.

current_price = get_stock_price(tickerSymbol): Cria uma variável 'current_price' que recebe o valor retornado pela função 'get_stock_price()' passando como parâmetro o tickerSymbol da Petrobras.

if current_price < 24:: Inicia a condição em que se o valor da ação é menor que 24 reais.

print(f"O preço atual da ação {tickerSymbol} é {current_price:.2f} e está abaixo de R$24."): Exibe a mensagem "O preço atual da ação PETR4.SA é {current_price:.2f} e está abaixo de R$24." com o valor da ação formatado em duas casas decimais.

else:: Caso o valor da ação seja maior ou igual a 24 reais.

print(f"O preço atual da ação {tickerSymbol} é {current_price:.2f}."): Exibe a mensagem "O preço atual da ação PETR4.SA é {current_price:.2f}." com o valor da ação formatado em duas casas decimais.

# Proximo passo e fazer com que o programa busque pelo nome da empresa

# depois quero receber uma mensagem automatica no meu celular

