# Bot Inicial - Primeira Unidade
 
No arquivo main.py tem a classe Program que contém os métodos para execução dos modulos e embaixo há um exemplo

Módulo 1:
função GetBestWay

Módulo 2:
função GetDistribuction

Módulo 3:
Está apenas com o código prolog no txt, falta levar isso pro python e terminar a função de salário.

# Atualização do Bot - Segunda Unidade
### O bot trabalha a parte de intenções diretamente com o dialogflow;
### A interface de conversação utilizada foi o Telegram;
### O bot tem 2 funcionalidades:
- Recomendação de animes com base no top 1200 animes do site MyAnimeList;
- Jogo da forca com algoritmo genético, você manda o nome de um anime, e ele através de um algoritmo genético vai chegar até o nome do anime e vai informar quantas gerações foram necessárias;

-----
### Dialogflow:
Além de criar todas as interações para que o bot do dialogflow identificasse as conversas também precisei treinar o modelo de entidades do dialogflow pra que ele pudesse reconhecer o nome dos animes, pra isso, utilizei minha própria base que foi coletada, peguei os nomes e adicionei todos eles nas entidades e deixei selecionada a opção de auto treino, ou seja, ele automaticamente vai começar a reconhecer outros nomes.

### Telegram:
Para o telegram não foi necessário fazer nada demais, meu código funciona como um Proxy, de acordo com o webhook que recebo do telegram pego a mensagem e envio como intenção para o dialogflow, após receber eu trato em código mesmo, de acordo com a intenção que foi reconhecida e as entidades que foram reconhecidas no dialogflow.

### Sistema de Recomendação:
O sistema de recomendação não fiz no modelo colaborativo, como eu não tinha os dados de usuários, apenas o nome, rank e sinopse, fiz baseado na sinopse, faço as tratativas e utilizo clusterização para separar os animes de acordo com as suas sinopses, com isso percebi que animes do mesmo gênero geralmente tem sinopses parecidas, mesmo que o enredo seja diferente.

Todos os dados que coletei foram em inglês, portanto as sinopses eu só tinha em inglês, então para informar o usuário to usando a biblioteca do google translate para python para traduzir as sinopses antes de enviar ao usuário.

### Jogo da forca (Hangman Game):
A principio iria utilizar o algoritmo genético para "melhorar" os parâmetros da clusterização, mas validando os score, percebi que as melhorias não foram muito efetivas. Então pensei em utilizar ele como um jogo de forca, onde o usuário informa um anime e o bot utiliza o algoritmo genético para ir de uma palavra totalmente aleatória até chegar no nome do anime informado.
