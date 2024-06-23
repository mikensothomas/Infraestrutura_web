import grpc
from concurrent import futures
import messenger_pb2
import messenger_pb2_grpc
import psycopg2

DB_HOST = 'banco'
DB_PORT = '5432'
DB_NAME = 'banco_grpc'
DB_USER = 'usuario'
DB_PASSWORD = '12345'

class MessengerServicer(messenger_pb2_grpc.MessengerServicer):
    def SendMessage(self, request, context):
        sender = request.sender
        content = request.content
                
        try:
            conn = psycopg2.connect(
                host=DB_HOST,
                port=DB_PORT,
                dbname=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD
            )
            print("Conexão com o banco de dados estabelecida com sucesso")
        except psycopg2.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return messenger_pb2.Empty()
        
        try:
            with conn.cursor() as cursor:
                print("\n")
                print("==============++++++++++++++++++++++=============")
                print("\n")
                print(f"Mensagem recebida do cliente {sender}: {content}.")
                sql = "INSERT INTO mensagem (nome, mensagens) VALUES (%s, %s)"
                cursor.execute(sql, (sender, content))
                conn.commit()
                print("\n")
                print("==============++++++++++++++++++++++==++++===========")
                print("\n")
                print("Mensagem inserida no banco de dados com sucesso")
        except psycopg2.Error as e:
            print(f"Erro ao inserir mensagem no banco de dados: {e}")
        finally:
            conn.close()
            print("==============++++++++++++++++++++++=============")
        
        return messenger_pb2.Empty()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    messenger_pb2_grpc.add_MessengerServicer_to_server(MessengerServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor conectado na porta 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
