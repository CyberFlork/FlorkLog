import sys
import os

def exibir_banner():
    print("███████╗██╗      ██████╗ ██████╗ ██╗  ██╗██╗      ██████╗  ██████╗ ")
    print("██╔════╝██║     ██╔═══██╗██╔══██╗██║ ██╔╝██║     ██╔═══██╗██╔════╝ ")
    print("█████╗  ██║     ██║   ██║██████╔╝█████╔╝ ██║     ██║   ██║██║  ███╗")
    print("██╔══╝  ██║     ██║   ██║██╔══██╗██╔═██╗ ██║     ██║   ██║██║   ██║")
    print("██║     ███████╗╚██████╔╝██║  ██║██║  ██╗███████╗╚██████╔╝╚██████╔╝")
    print("╚═╝     ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝ ")
    print("")
    print("        [ Ferramenta de Análise de Logs para Cibersegurança ]\n")

def exibir_ajuda():
    print("--- 📚 GUIA DE AJUDA DO FLORKLOG ---")
    print("Como usar no terminal:")
    print("  python florklog.py <caminho_do_arquivo> <palavra_chave>")
    print("\nExemplos:")
    print("  python florklog.py log.txt erro")
    print("  python florklog.py \"C:\\Logs\\servidor.log\" failed")
    print("\nAtalhos de ajuda:")
    print("  python florklog.py help   -> Mostra este menu de ajuda")
    print("-" * 50)

def main():
    exibir_banner()

    # Se o usuário digitar 'help', 'halp' ou não passar argumentos suficientes
    if len(sys.argv) < 2 or sys.argv[1].lower() in ["help", "halp", "-h", "--help" "ajuda"]:
        exibir_ajuda()
        sys.exit(0)

    caminho = sys.argv[1]

    # Verifica se o arquivo existe
    if not os.path.exists(caminho):
        print(f"[-] Erro: O arquivo '{caminho}' não foi encontrado.")
        print("[!] Digite 'python florklog.py help' para ver como usar.")
        sys.exit(1)

    # Se o usuário passou a palavra-chave direto, usa. Se não, pergunta interativamente!
    if len(sys.argv) >= 3:
        chave = sys.argv[2]
    else:
        chave = input("O que você deseja buscar no log? ").strip()

    print(f"[+] Buscando por '{chave}' em: {caminho}\n")
    print("-" * 50)

    encontrou = False
    try:
        with open(caminho, "r", encoding="utf-8", errors="ignore") as arquivo:
            for linha in arquivo:
                if chave.lower() in linha.lower():
                    print(linha.strip())
                    encontrou = True
        
        print("-" * 50)
        if not encontrou:
            print("[-] Nenhuma ocorrência encontrada para essa palavra.")
        else:
            print("[+] Busca concluída com sucesso.")

    except Exception as e:
        print(f"[-] Erro ao ler o arquivo: {e}")

if __name__ == "__main__":
    main()
