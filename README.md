# EVENTEX

Sistema desenvolvido durante o curso WTTD.

## Como desenvolver

1. Clone o repositório.
2. Crie um virtualenv com python 3.5
3. Ative o virtualenv
4. Instale as dependencias
5. Configure a instância com o .env
6. Execute os testes

```console
git clone git@github.com:victorgabryel/eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requeriments.txt
cp contrib/env_sample .env
python manage.py test
```

## Como fazer o deploy

1. Crie uma instância pro Heroku.
2. Envie as configurações para o Heroku.
3. Defina uma SECRET_KEY segura para a instância.
4. Defina DEBUG=False
5. Configure o serviço de e-mail
6. Envie o código para o heroku

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY='python contrib/secret_gen.py'
heroku config:set DEBUG=FALSE
#configuro o e-mail
git push heroku master --force
```