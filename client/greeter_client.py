import grpc
import time
import os
import logging

# Import the generated protobuf files (assuming they are generated into this directory)
import helloworld_pb2
import helloworld_pb2_grpc

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - CLIENT - %(message)s')

def run():
    # Get server host and port from environment variables set in docker-compose.yml
    server_host = os.getenv('GRPC_SERVER_HOST', 'localhost')
    server_port = os.getenv('GRPC_SERVER_PORT', '50051')
    server_address = f"{server_host}:{server_port}"

    logging.info(f"Connecting to gRPC server at {server_address}")

    # Establish an insecure channel to the server
    with grpc.insecure_channel(server_address) as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        
        # Give the server a moment to finish connecting, though dependencies help
        time.sleep(1)

        client_request_send_time = time.time()
        logging.info(f"Sending 'SayHello' request for 'World' at {client_request_send_time:.4f}s")

        try:
            # Send the request
            response = stub.SayHello(helloworld_pb2.HelloRequest(name='World'))

            client_response_receive_time = time.time()
            total_round_trip_time = client_response_receive_time - client_request_send_time

            logging.info(f"Received 'SayHello' response: '{response.message}' at {client_response_receive_time:.4f}s")
            logging.info(f"Total round-trip time for RPC: {total_round_trip_time*1000:.2f} ms")

        except grpc.RpcError as e:
            logging.error(f"gRPC Error: {e.code()} - {e.details()}")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    # Initial wait to ensure the server container is fully started before the client exits quickly
    time.sleep(2) 
    run()