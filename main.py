from database.entities import Message, User
from database.mongohandler import MongoHandler

# comeca aqui: parte de cripto
from aes_pkcs5.algorithms.aes_cbc_pkcs5_padding import AESCBCPKCS5Padding

# b64
key = "@NcRfUjXn2r5u8x/"
output_format = "b64"
iv_parameter = "0011223344556677"
cipher = AESCBCPKCS5Padding(key, output_format, iv_parameter)

handler = MongoHandler()

def menu(User):
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
                        read_email(User)
                elif opcao == '2':
                        send_email(User)
                elif opcao == '3':
                        print("Saindo...")
                        break
                else:
                        print("Opção inválida. Tente novamente.")


def read_email(user: User):
        messages = handler.get_messages(user.email)
        for message in messages:
                content = cipher.decrypt(message.content)

                print("\nEnviado por: " + message.sender)
                print(content)


def send_email(user: User):
        receiver = input("Destinatário: ")
        content = input("Mensagem: ")
        content = cipher.encrypt(content)
        message = Message(sender=user.email,receiver=receiver, content=content)
        messageID = handler.insert_message(message)
        if messageID:
                print("Email enviado com sucesso...")


if __name__ == '__main__':
        while True:
                print("\n" + "=" * 40)
                print("         LOGIN")
                print("=" * 40)
                email = input("Insira seu email: ")
                password = input("Insira sua senha: ")

                user = User(email=email, password=password)
                auth = handler.authenticate(user)
                if auth:
                        break
                print(auth)

        menu(user)


