# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependency file and install dependencies
COPY client/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the generated Protobuf files and the client code
# NOTE: The *.py files must be generated on the host before running docker-compose build
COPY protos/helloworld_pb2*.py /app/
COPY client/greeter_client.py /app/

# The client doesn't need to expose any ports

# Run the client script when the container launches
CMD ["python", "greeter_client.py"]