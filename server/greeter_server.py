import grpc
from concurrent import futures
import time
import logging

# Import the generated protobuf files (assuming they are generated into this directory)
import helloworld_pb2
import helloworld_pb2_grpc

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - SERVER - %(message)s')

class GreeterServicer(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        server_request_time = time.time()
        logging.info(f"Received request for '{request.name}' at {server_request_time:.4f}s")

        # Simulate some processing time to demonstrate latency
        processing_delay = 0.05 # 50 milliseconds
        time.sleep(processing_delay)
        server_processed_time = time.time()
        logging.info(f"Finished processing for '{request.name}' after {processing_delay*1000:.1f}ms at {server_processed_time:.4f}s")

        message = f"Hello, {request.name}! (Server processed in {processing_delay*1000:.1f}ms)"
        response = helloworld_pb2.HelloReply(message=message)

        server_response_time = time.time()
        logging.info(f"Sending response for '{request.name}' at {server_response_time:.4f}s")

        return response

def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    logging.info("Started, listening on " + port)
    server.wait_for_termination()

if __name__ == '__main__':
    serve()