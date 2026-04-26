# Core Framework - Ecossistema Multi-Tenant v1.0

![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-orange)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Security](https://img.shields.io/badge/Security-Triple%20Lock-red)

O **Core Framework** é uma infraestrutura de microserviços de alta performance projetada para servir como a fundação de todos os softwares do ecossistema. Ele utiliza uma arquitetura híbrida para atender múltiplas empresas (100+) com código único e isolamento total de dados.

## 🏗️ Pilares da Engenharia

### 1. Segurança "Triple Lock" (Tranca Tripla)
Nenhuma execução ocorre sem a validação simultânea de:
* **UUID (ID Único):** Rastreabilidade total da transação.
* **CNPJ:** Identificação da empresa (Tenant) e direcionamento do Banco de Dados.
* **CPF:** Identificação do operador responsável pela ação.

### 2. Integridade de Código
O sistema utiliza **Assinaturas Digitais Assimétricas**. Cada arquivo de função (`1 Arquivo = 1 Função`) possui uma assinatura gerada offline por uma Chave Privada. O **Secure Loader** valida a integridade antes de qualquer processamento.

### 3. Escala Multi-Tenancy
* **Código Único:** Facilidade de manutenção e atualização global.
* **Bancos de Dados Isolados:** Segurança e conformidade legal (LGPD) por cliente.

## 🛠️ Stack Tecnológica

* **Backend:** Python (FastAPI/Flask)
* **Frontend:** HTML5, CSS3, Bootstrap 5
* **Segurança:** Criptografia RSA/ECDSA, Hashing Bcrypt
* **DevOps:** Docker, GitHub Actions

## 📁 Estrutura do Projeto

```text
Projeto_base /
├── .venv/                   # Ambiente virtual Python (Isolamento de bibliotecas)
├── .github/                 # Workflows para automação (GitHub Actions)
├── docs/                    # Documentação técnica e de produto (Markdown/PDF)
├── scripts/                 # Ferramentas de apoio (ex: Script de Assinatura Offline)
│
├── src/                     # Código-fonte (Tudo o que é "vivo" fica aqui)
│   ├── backend/             # O Motor Python
│   │   ├── core/            # Regras de Ouro: Seguranca, Triple Lock, Validador
│   │   ├── services/        # Os 100 Componentes (1 arquivo = 1 função)
│   │   │   ├── auth/        # Login, Cadastro, JWT
│   │   │   ├── financeiro/  # Comissões, Pagamentos
│   │   │   └── logs/        # Escrita na Caixa Preta
│   │   ├── database/        # Orquestrador de Multi-bancos e Migrations
│   │   └── api/             # Rotas de entrada (Endpoints)
│   │
│   └── frontend/            # A Interface (Bootstrap/HTML/CSS)
│       ├── static/          # Arquivos imutáveis (CSS, JS, Imagens)
│       └── templates/       # Páginas dinâmicas (Jinja2/HTML)
│
├── tests/                   # Testes automatizados (Garantia de qualidade)
├── .env                     # Variáveis de ambiente (NÃO VAI PARA O GIT)
├── .gitignore               # O que o Git deve ignorar (Definido anteriormente)
├── requirements.txt         # Lista de bibliotecas do projeto
└── README.md                # Manual de instruções do projeto
