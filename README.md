# Projeto Final SEL0456 - Conversor de unidades

## Contexto
Projeto criado como trabalho final para disciplina de SEL0456, na qual, foi proposto a criação de um conversor de unidades usando PYTHON+GTK, com auxílio de Glade.

## Grandezas adicionadas
 - Pressão
 - Massa
 - Moeda
 
## *Unidade Moeda*
A unidade moeda foi feita utilizando web scraping, ou seja, a cotação é pega da internet. Como a conversão é feita em tempo real (ao digitar o valor ele já é convertido), seria inviável que o web scraping fosse feito em tempo real também, por isso, um botão cotação para carregar os valores atuais foi feito. Recomenda-se atualizar a cotação antes de usar a MOEDA. Mas, tomar cuidado ao apertar o botão repetidamente, pode ocasionar ERRO. **Caso ocorra erro ao carregar, clicar novamente,** o web scraping pode encontrar problemas.

Um arquivo com a cotação fica salvo ("df2.csv"). Se não existir, apertando o botão é criado um.
 
## Observações
Algumas bibliotecas precisam ser instaladas para funcionamento 100%.
 - Pandas: pip install pandas;
 - BeautifulSoup: pip install beautifulsoup4;
 - DateTime: pip install DateTime;
 - Talvez outras sejam necessárias.

## Arquivos
 - links.dat contém os links da onde as cotações são retiradas;
 - combo_ex.glade contém a configuração da interface;
 - conversão.py é o script em si;
