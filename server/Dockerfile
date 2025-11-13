# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependency file and install dependencies
COPY server/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the generated Protobuf files and the server code
# NOTE: The *.py files must be generated on the host before running docker-compose build
COPY protos/helloworld_pb2*.py /app/
COPY server/greeter_server.py /app/

# Expose the port your gRPC server listens on (e.g., 50051)
EXPOSE 50051

# Run the server script when the container launches
CMD ["python", "greeter_server.py"]