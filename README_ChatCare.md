# 🤖 ChatCare – Chatbot Pós-Cirúrgico

ChatCare é um chatbot feito com Python, Flask e modelos de linguagem natural, que responde dúvidas frequentes de pacientes após cirurgias.  
Utiliza embeddings de frases (Sentence Transformers) para encontrar respostas similares em uma base de dados médica estruturada.

---

## 🧠 Tecnologias utilizadas

- Python 3.10+
- Flask
- Flask-CORS
- Sentence Transformers
- scikit-learn
- pandas
- HTML + JavaScript (front-end)

---

## 🚀 Como rodar o ChatCare localmente

### 1. Clone o repositório

```bash
git clone https://github.com/julianunes2703/ChatCare.git
cd ChatCare
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv
# Ative o ambiente virtual:
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

> Caso o arquivo `requirements.txt` não esteja presente, rode:

```bash
pip install flask flask-cors pandas numpy scikit-learn sentence-transformers
```

---

## 🗂 Estrutura do projeto

```
ChatCare/
├── app.py                      # API Flask que processa perguntas
├── banco.py                    # Gera o arquivo CSV com perguntas/respostas
├── custom_postoperative_faq.csv  # Base de conhecimento do chatbot (gerado)
├── index.html                  # Front-end do chatbot
├── .gitignore
└── README.md                   # (você está aqui)
```

---

## 🧪 Como usar

### 1. Gere a base (opcional, só se quiser editar as perguntas)

```bash
python banco.py
```

Isso gera o arquivo `custom_postoperative_faq.csv`.

---

### 2. Rode a API Flask

```bash
python app.py
```

A API ficará acessível em: http://127.0.0.1:5000

---

### 3. Abra o front-end

1. Instale a extensão **Live Server** no VS Code  
2. Clique com o botão direito em `index.html` → **"Open with Live Server"**

> Isso abrirá algo como `http://127.0.0.1:5500/index.html`

Agora você pode testar digitando perguntas como:

```
Quando posso voltar a trabalhar após cirurgia no joelho?
```

---

## 📦 Requisitos

- Python 3.10+
- Navegador moderno (Chrome, Firefox, Edge)
- VS Code (recomendado) com Live Server

---

## ❗ Observações

- O chatbot **não substitui atendimento médico**. As respostas são baseadas em informações gerais sobre cuidados pós-cirúrgicos.
- Ideal para fins educacionais, testes e demonstrações.

---

## 👩‍💻 Desenvolvido por

- Julia Nunes
- Davi Kunsch
- Lucas Almeida
