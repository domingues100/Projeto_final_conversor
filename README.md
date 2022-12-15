# Projeto Final SEL0456 - Conversor de unidades

## Contexto
Projeto criado como trabalho final para disciplina de SEL0456, na qual, foi proposto a criação de um conversor de unidades usando PYTHON+GTK, com auxílio de Glade.

## Grandezas adicionadsa
 - Pressão
 - Massa
 - Moeda
 
## Unidade Moeda
A unidade moeda foi feita utilizando web scraping, ou seja, a cotação é pega da internet. Como a conversão é feita em tempo real (ao digitar o valor ele já é convertido), seria inviável que o web scraping fosse feito em tempo real também, por isso, um arquivo com a cotação foi feito antes e a data da cotação foi adicionada.
Ao digitar o valor é consultada a data, se a cotação no arquivo for do mesmo dia, utiliza os valores presentes, caso contrário, atualiza a cotação e salva novamente no arquivo.
 
##Observações
Algumas bibliotecas precisam ser instaladas para funcionamento 100%.
 - Pandas: pip install pandas;
 - BeautifulSoup: pip install beautifulsoup4;
 - DateTime: pip install DateTime;
 - Talvez outras sejam necessárias.
