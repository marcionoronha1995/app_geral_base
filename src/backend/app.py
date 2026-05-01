import os
import sys

from flask import Flask

# Ajusta o caminho para encontrar a pasta 'src' e o 'secure_loader'
# Sobe 2 níveis: de src/backend/ para a raiz app_geral_login
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from src.backend.core.secure_loader import load_secure_environment

app = Flask(__name__)

# Validação de Segurança V8
if load_secure_environment():
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["DEBUG"] = os.getenv("DEBUG") == "True"
else:
    print("❌ ERRO: Não foi possível carregar as configurações de segurança.")
    sys.exit(1)


@app.route("/")
def index():
    return {
        "status": "Online",
        "modulo": "Core Login",
        "tecnologia": "Flask + Python 3.14",
        "ambiente": "Desenvolvimento",
    }


if __name__ == "__main__":
    print("🚀 Servidor V8 Ativo: http://127.0.0.1:5000")
    app.run(host="0.0.0.0", port=5000)
