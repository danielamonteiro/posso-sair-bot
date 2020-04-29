# posso-sair-bot

Um bot simples que informa se devemos ou não sair de casa sem necessidade durante a quarentena. Bot com o intuito de explorar as possibilidades da API do Twitter.

## Implementações:

 - O bot envia um tweet por dia indicando se podemos ou não sair de casa sem necessidade durante a quarentena, sempre na sequência: um dia um texto, um dia um arquivo de imagem;
 - Os textos que serão enviados devem ser incluídos no arquivo [responses/responses_to_send.txt](https://github.com/danielamonteiro/posso-sair-bot/blob/master/responses/responses_to_send.txt "responses_to_send.txt"), quando a mensagem for enviada, ela será retirada desse arquivo e incluída no arquivo [responses/sent_responses.txt](https://github.com/danielamonteiro/posso-sair-bot/blob/master/responses/sent_responses.txt "sent_responses.txt");
 - As imagens que serão enviadas devem ser incluídas no diretório [images/send](https://github.com/danielamonteiro/posso-sair-bot/tree/master/images/send "send"), quando forem enviadas, elas serão movidas para o diretório [images/sent](https://github.com/danielamonteiro/posso-sair-bot/tree/master/images/sent "sent");
 - Quando der algum erro de envio de algum tweet, quando for enviada a última mensagem de texto do arquivo ou a última imagem do diretório, o bot enviará uma DM para o user id que for informado no arquivo .env (as mensagens enviadas para cada caso deve ser incluída no arquivo de .env);

Para rodar o bot:

    python3 run.py

***Lembrete:*** necesário possuir dados de acesso de api key, api token e etc do twitter e preencher esses dados no arquivo .env antes de rodar.

