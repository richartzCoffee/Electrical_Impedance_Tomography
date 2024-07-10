#!/bin/bash

# Verifica se o ambiente virtual já existe
if [ ! -d "venv" ]; then
    echo "Criando ambiente virtual..."
    python3 -m venv venv
fi

# Ativa o ambiente virtual
echo "Ativando ambiente virtual..."
source venv/bin/activate

# Instala as dependências
echo "Instalando dependências..."
pip install -r requirements.txt

export QT_DEBUG_PLUGINS=1
export QT_QPA_PLATFORM_PLUGIN_PATH=./venv/lib/python3.10/site-packages/cv2/qt/plugins


# Inicia a aplicação (substitua com o comando correto para iniciar sua aplicação)
echo "Iniciando aplicação..."
python aplication.py
