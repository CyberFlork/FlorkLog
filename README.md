# 🛡️ FlorkLog

> Uma ferramenta de linha de comando (CLI) leve, rápida e simples desenvolvida em Python para analistas de cibersegurança buscarem, filtrarem e analisarem arquivos de log com eficiência.

---

## 🚀 Funcionalidades

- **Busca Rápida via CLI:** Analise rapidamente arquivos de log grandes (como logs do VirtualBox, logs de autenticação do sistema, servidores web, etc.) diretamente pelo seu terminal.
- **Filtro Inteligente:** Ignora diferenças entre letras maiúsculas e minúsculas (*case-insensitive*) para garantir que você não perca nenhum evento crítico.
- **Guia de Ajuda Integrado:** Menu de ajuda interativo (`help` / `halp`) para facilitar o uso e orientar novos usuários.
- **Tratamento Robusto de Erros:** Ignora corrupções de codificação (*encoding*) ou caracteres inválidos com segurança, evitando que a ferramenta feche no meio de uma investigação.

---

## 📋 Requisitos

- Python 3.x (Não requer nenhuma biblioteca externa, utiliza apenas módulos padrão do Python como `sys` e `os`).

---
