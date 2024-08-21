# Usando a imagem base do Python
FROM python:3.9-slim

# Definindo o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiando os arquivos de requisitos e instalando as dependências
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiando o código da aplicação
COPY . .

# Expondo a porta que o Flask utilizará
EXPOSE 5000

# Comando para iniciar a aplicação
CMD ["python", "app.py"]
