from database.mongohandler import MongoHandler

# comeca aqui: parte de cripto
from aes_pkcs5.algorithms.aes_cbc_pkcs5_padding import AESCBCPKCS5Padding

# b64
key = "@NcRfUjXn2r5u8x/"
output_format = "b64"
iv_parameter = "0011223344556677"
message = "Hello World"

cipher = AESCBCPKCS5Padding(key, output_format, iv_parameter)
encrypted = cipher.encrypt(message)
assert encrypted == "MhL/V78kC3rcYlnlPg1L4g=="
assert cipher.decrypt(encrypted) == message

# hex
output_format = "hex"
cipher = AESCBCPKCS5Padding(key, output_format, iv_parameter)
encrypted = cipher.encrypt(message)
assert encrypted == "3212ff57bf240b7adc6259e53e0d4be2"
assert cipher.decrypt(encrypted) == message
# comeca aqui: termina aqui

handler = MongoHandler()

def menu(email):
        while True:
                print("\nMenu de Opções:")
                print("1. Ler email")
                print("2. Enviar email")
                print("3. Sair")

                opcao = input("Escolha uma opção (1-3): ")

                if opcao == '1':
                        read_email(email)
                elif opcao == '2':
                        send_email(email)
                elif opcao == '3':
                        print("Saindo...")
                        break
                else:
                        print("Opção inválida. Tente novamente.")


def read_email(email):
        handler.get_messages(email)
        print("Lendo emails...")


def send_email(email):
        print("Enviando email...")


if __name__ == '__main__':
        while True:
                print("\nLogin")
                email = input("Insira seu email: ")
                password = input("Insira sua senha: ")

                auth = handler.authenticate(email, password)
                if auth == True:
                        break
                print(auth)

        menu(email)


