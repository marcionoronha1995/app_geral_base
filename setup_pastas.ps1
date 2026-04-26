# Define as pastas que precisam ser criadas
$pastas = @(
    ".github",
    "docs",
    "scripts",
    "src/backend/core",
    "src/backend/services/identity",
    "src/backend/services/tenants",
    "src/backend/services/audit",
    "src/backend/database",
    "src/backend/api",
    "src/frontend/static",
    "src/frontend/templates",
    "tests"
)

# Arquivos base na raiz
$arquivosRaiz = @(".env", ".gitignore", "requirements.txt", "README.md")

Write-Host "--- Iniciando a construção da estrutura de pastas ---" -ForegroundColor Cyan

# Cria as pastas e o arquivo .txt correspondente
foreach ($caminho in $pastas) {
    if (-not (Test-Path $caminho)) {
        New-Item -Path $caminho -ItemType Directory -Force | Out-Null
        
        # Extrai o nome da última pasta para criar o arquivo .txt
        $nomePasta = Split-Path $caminho -Leaf
        $caminhoArquivo = Join-Path $caminho "$nomePasta.txt"
        
        New-Item -Path $caminhoArquivo -ItemType File -Force | Out-Null
        Write-Host "[OK] Pasta criada: $caminho (com arquivo $nomePasta.txt)" -ForegroundColor Green
    }
}

# Cria os arquivos da raiz caso não existam
foreach ($arq in $arquivosRaiz) {
    if (-not (Test-Path $arq)) {
        New-Item -Path $arq -ItemType File -Force | Out-Null
        Write-Host "[OK] Arquivo de raiz criado: $arq" -ForegroundColor Yellow
    }
}

Write-Host "--- Estrutura concluída com sucesso! ---" -ForegroundColor Cyan