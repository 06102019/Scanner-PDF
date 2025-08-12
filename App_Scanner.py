# arquivo: App_Scanner.py

import streamlit as st
import pdfplumber
import pandas as pd
from datetime import datetime, timedelta
import os
import google.generativeai as genai # <-- Importação da biblioteca do Gemini

# --- CONFIGURAÇÃO DA API DO GEMINI ---
# Instrução: Substitua "SUA_CHAVE_DE_API_DO_GEMINI" pela sua chave real.
# Você pode obter sua chave em https://aistudio.google.com/app/apikey
genai.configure(api_key="SUA_CHAVE_DE_API_DO_GEMINI")

# Definição do modelo a ser usado
model = genai.GenerativeModel('gemini-1.5-flash')
# ------------------------------------

st.set_page_config(page_title="SCANNER PDF - Extrator Inteligente", layout="wide")

st.title("SCANNER PDF - Extrator de Informações com IA")

uploaded_file = st.file_uploader("📎 Anexar PDF aqui", type=["pdf"])

# Função para extrair todo o texto do PDF
def extrair_texto_pdf(pdf_file):
    texto_completo = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            texto_completo += page.extract_text()
    return texto_completo

# Extrair texto do PDF
texto_pdf = None
if uploaded_file:
    st.write("📄 Lendo o texto do PDF...")
    texto_pdf = extrair_texto_pdf(uploaded_file)
    st.write("✅ Texto extraído com sucesso!")


# Campo de pergunta para IA
pergunta = st.text_input("💬 Peça à IA para extrair uma informação do documento:")

if pergunta and texto_pdf is not None:
    prompt = f"""
    Você é um assistente de extração de informações de documentos.
    O documento fornecido está abaixo. Sua tarefa é analisar o conteúdo e responder à pergunta do usuário de forma direta e concisa.

    Conteúdo do documento:
    {texto_pdf}

    Pergunta:
    {pergunta}
    """
    
    try:
        # --- CHAMADA À API DO GEMINI ---
        response = model.generate_content(
            prompt,
            generation_config={"temperature": 0.0}
        )
        # -----------------------------
        
        st.subheader("🔎 Resultado da Extração:")
        st.write(response.text)
        
    except Exception as e:
        st.error(f"Ocorreu um erro ao chamar a API do Gemini: {e}")