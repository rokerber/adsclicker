# Usa uma imagem Python oficial como base
FROM python:3.9-slim

# Define o diretório de trabalho no container
WORKDIR /app

# Instala as dependências do sistema necessárias para o Chrome e para a nova forma de adicionar chaves
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    curl \
    fonts-liberation \
    libasound2 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdbus-glib-1-2 \
    libdrm2 \
    libgbm1 \
    libglib2.0-0 \
    libgtk-3-0 \
    libnss3 \
    libxcomposite1 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    libxrandr2 \
    libxtst6 \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Adiciona o repositório do Google Chrome usando o método recomendado
# Descarrega a chave GPG e adiciona-a ao keyring, depois adiciona a entrada do repositório
RUN curl -sSL https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/google-chrome.gpg \
    && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-chrome.gpg] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Copia o arquivo de requisitos e instala as dependências do Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Adiciona o utilizador não-root e altera a propriedade da pasta de trabalho
RUN useradd -m -u 1001 appuser
RUN chown -R appuser /app
USER 1001

# Copia o script para o container
COPY auto_clicker.py .

# Define o comando para executar o script quando o container for iniciado
CMD ["python", "auto_clicker.py"]
