from database.mongohandler import MongoHandler

# comeca aqui: parte de cripto
from aes_pkcs5.algorithms.aes_cbc_pkcs5_padding import AESCBCPKCS5Padding

# b64
key = "@NcRfUjXn2r5u8x/"
output_format = "b64"
iv_parameter = "0011223344556677"
cipher = AESCBCPKCS5Padding(key, output_format, iv_parameter)

handler = MongoHandler()

def menu(email):
        while True:
                print("\n" + "=" * 40)
                print("         MENU DE OPÇÕES")
                print("=" * 40)
                print("1. Ler email")
                print("2. Enviar email")
                print("3. Sair")
                print("=" * 40)

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
        messages = handler.get_messages(email)
        for message in messages:
                content = message.content
                content = cipher.decrypt(content)
                print(content)


def send_email(email):
        receiver = input("Destinatário: ")
        content = input("Mensagem: ")
        content = cipher.encrypt(content)
        messageID = handler.insert_message(email, receiver, content)
        if messageID == True:
                print("Email enviado com sucesso...")


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


