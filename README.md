# Scanner-PDF

UNICAR - Extrator Inteligente de Informações
Este é um projeto simples, mas poderoso, que utiliza a IA do Google Gemini e a biblioteca Streamlit para criar um extrator de informações interativo a partir de documentos PDF. O objetivo é transformar documentos estáticos em uma fonte de dados dinâmica, onde os usuários podem fazer perguntas em linguagem natural e obter respostas concisas.

💻 Tecnologias Utilizadas
Python: A linguagem de programação principal.

Streamlit: Framework para a criação rápida e fácil de interfaces de usuário web.

Google Gemini API: A IA generativa que permite a extração e análise inteligente do texto.

PDFPlumber: Biblioteca para extrair texto e dados de documentos PDF.

🚀 Como Usar
Pré-requisitos
Python 3.9+ instalado.

Uma chave da API do Google Gemini. Você pode obtê-la gratuitamente no Google AI Studio.

Instalação
Clone este repositório para sua máquina local:

git clone https://github.com/SEU-USUARIO/unicar-app.git
cd unicar-app

Instale as dependências necessárias:

pip install -r requirements.txt

(Crie um arquivo requirements.txt com as bibliotecas: streamlit, pdfplumber, pandas, google-generativeai)

Execução
Abra o arquivo unicar_app.py e substitua "SUA_CHAVE_DE_API_DO_GEMINI" pela sua chave real.

Execute o aplicativo a partir do terminal:

streamlit run unicar_app.py

Uma nova aba será aberta no seu navegador, onde você poderá fazer o upload de um PDF e interagir com a IA.

💡 Funcionalidades
Upload de PDF: Carregue qualquer arquivo PDF com conteúdo textual.

Extração de Texto: O sistema extrai todo o texto do documento.

Consulta com IA: Faça perguntas sobre o conteúdo do PDF, e a IA buscará a resposta.

Interface Intuitiva: Graças ao Streamlit, a interface é limpa e fácil de usar.
