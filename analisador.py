#Análise realizada para pautar os principais motivos da desistência de cerca de 26% dos clientes da empresa.

# Importando a base de dados

import pandas as pd
import plotly.express as px
tabela = pd.read_csv('telecom_users.csv')

# Visualizar a base de dados:

print(tabela)

# Entender  as informações disponíveis e reconhecer possíveis erros na base.

print(tabela.info())

# Eliminar informações desnecessárias:

tabela = tabela.drop("Unnamed: 0", axis=1) # Essa linha elimina a coluna "Unnamed: 0", onde a coluna a ser eliminada é definido pelo seu nome e o axis = 1.

# -> Na coluna TotalGasto seus valores estão reconhecidos de forma errada, portanto realizar correção:

tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce") # O parâmetro 'errors' força qualquer informção que seja diferente de um número a se tornar um NaN

# -> Eliminar linhas onde qualquer informação seja vazia e elminar as colunas onde toda as suas informações seja igual a vazio.

tabela = tabela.dropna(how='all', axis=1) # Essa linha elimina a coluna que possuir todos(all) os campos vazios.
tabela = tabela.dropna(how='any', axis=0) # Essa linha elimina a linha que possuir algum(any) campo vazio.

print(tabela.info())

# Desobrir como estão os cancelamentos dos clientes

print(tabela['Churn'].value_counts())
print(tabela['Churn'].value_counts(normalize=True).map("{:.1%}".format)) # Essa linha trás os valores em porcetagem.

### Nota-se qua após o tratamento restaram apenas 5974 linhas sem nem um valor vazio, facilitando assim a análise.

# Criar os gráficos para analisá-los colocando todas as colunas em relação a coluna de Churn(Desistência).

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="Churn", text_auto=True)
grafico.show()


'''

Com base na análise feita observando as informações em realção as desistenências, foi identificado alguns fatores:
- Clientes que possuem contrato mensal tem uma maior probabilidade de cancelar.
    -> Para solução seria necessário a criação promoções para que os clientes contratem planos anuais.
- Clintes com família maiores possuem uma menor probabilidade de cancelar em relação a famílias menores.
    -> Para solucionar seria necessário a criação de planos de acordo com o tamanho da família.
- Notou-se a taxa de desistência é maior nos primeiros meses de contrato. Podendo levar em conta vários fatores:
    -> A primeira experiência do cliente na operadora pode ser ruim
    -> Talvez a captação de clientes tá trazendo clientes desqualificados
    -> Para tentar solucionar pode ser criado um incentivo pro cliente permanecer por mais tempo.
- Com a análise notou-se que quanto maior for o número de serviços disponíveis menor é probabilidade de desistência do cliente.
    -> Solução: Agregar a maior quantidade de serviços possíveis aos planos.
- Notou-se que grande parte dos clientes que realizam pagamento por boleto desistem.
    -> Solução: gerar promoções para pagamentos realizados por transferências, pix e cartão de crédito.

'''

