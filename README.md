# API SERVERLESS GRAPHQL

Repositorio que incluye la implementación para consumo de servicios con GraphQL

## Prerequisitos

Instalar **Flask**

```bash
pip install Flask flask_cors
```

Instalar herramientas para integración de **GraphQL**
```bash
pip install Flask-GraphQL
pip install graphene-mongo
pip install mongomock
```

Instalar **boto3**
```bash
pip install boto3
```

Para hacer deploy en AWS, mediante el framework [serverless](https://serverless.com/)

```bash
npm install -g serverless
```

Configura credenciales de AWS

```bash
serverless config credentials --provider aws --key YOUR_KEY_ID --secret YOUR_SECRET_KEY --profile PROFILE
```

Instala plugins de serverless

```bash
sls plugin install -n serverless-wsgi

sls plugin install -n serverless-python-requirements

npm install serverless-deployment-bucket
```

## Deploy

#### Local Deployment
```bash
sls wsgi serve
```

#### AWS Deployment
```bash
sls deploy --aws-profile YOUR_PROFILE
```


