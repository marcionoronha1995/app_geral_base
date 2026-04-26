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
├── .venv/                   # Ambiente virtual (Isolamento total)
├── .github/                 # Automação de testes do Cadastro
├── docs/                    # Especificação do Schema de Usuários
├── scripts/                 # Gerador de Assinatura para novos arquivos .py
│
├── src/                     
│   ├── backend/             
│   │   ├── core/            # O "Secure Loader" que valida as 3 chaves
│   │   ├── services/        # A inteligência do sistema base
│   │   │   ├── identity/    # Cadastro de Usuários (CPF) e Perfis
│   │   │   ├── tenants/     # Cadastro de Empresas (CNPJ) e Configurações
│   │   │   └── audit/       # Gravação da "Caixa Preta" (Logs)
│   │   ├── database/        # Orquestrador que abre o banco via CNPJ
│   │   └── api/             # Endpoints (Ex: /api/v1/cadastrar)
│   │
│   └── frontend/            
│       ├── static/          # CSS do formulário de cadastro (Bootstrap)
│       └── templates/       # HTML de Cadastro, Login e Perfil
│
├── tests/                   # Testes de estresse (Cadastrar 100 empresas)
├── .env                     # Chaves mestras e conexões
├── .gitignore               # Proteção para não subir segredos
├── requirements.txt         # Bibliotecas (Flask/FastAPI, SQLAlchemy, Bcrypt)
└── README.md                # Guia do sistema de Identidade
