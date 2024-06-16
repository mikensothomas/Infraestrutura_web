import grpc
from concurrent import futures
import messenger_pb2
import messenger_pb2_grpc

class MessengerServicer(messenger_pb2_grpc.MessengerServicer):
    def SendMessage(self, request, context):
        print(f"Mensagem recebida do cliente {request.sender}: {request.content}")
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
