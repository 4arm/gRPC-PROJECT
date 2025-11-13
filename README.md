<img width="1024" height="1024" alt="Gemini_Generated_Image_z6rwh9z6rwh9z6rw" src="https://github.com/user-attachments/assets/e675ec71-d21d-4768-a5fd-41ca8d6a6c60" /># 🚀 gRPC Service with Docker and Docker Compose

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
![gRPC](https://img.shields.io/badge/gRPC-00ADD8?logo=grpc&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)

A foundational blueprint for building, containerizing, and orchestrating a high-performance **gRPC microservice** with a client, all running in Docker containers.

## ✨ Features

* **gRPC Service:** A simple, high-performance `Greeter` service using a Unary RPC.
* **Containerized:** Both the server and client are fully containerized with **Docker**.
* **Orchestrated:** Uses **Docker Compose** to manage the services, network, and dependencies.
* **Service Discovery:** Demonstrates service-to-service communication using Docker's internal networking.
* **Scalable:** Provides a clean architecture that can be extended with more complex services.

## 🛠️ Technology Stack

| Component | Role |
| :--- | :--- |
| **gRPC** | The RPC framework for efficient service communication. |
| **Protobuf** | Defines the language-agnostic service contract (`.proto`). |
| **Docker** | Builds and runs the server and client images. |
| **Docker Compose** | Orchestrates the multi-container application and networking. |
| **Python** | Language used for server and client implementation (easily swappable). |

## 🏗️ Architecture / How It Works

This project uses **Docker Compose** to create two independent services (`server` and `client`) that communicate over a dedicated bridge network (`grpc-net`).

1.  The **`server`** container starts and listens for gRPC requests on port `50051`.
2.  The **`client`** container starts, connects to the server using the internal service name (`server:50051`), and sends a `HelloRequest`.
3.  The server processes the request and streams back the `HelloReply`.

---
### **[ 📸 INSERT YOUR DIAGRAMS HERE ]**

### <img width="1024" height="1024" alt="Gemini_Generated_Image_z6rwh9z6rwh9z6rw" src="https://github.com/user-attachments/assets/24e42d5a-c64a-4b51-98c7-c0f7681b9ce8" />


To visually explain the architecture, place your diagrams in an `img/` folder and link them here.

Example:
`![Project Architecture Diagram](img/architecture.png)`
---

## 🚀 Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

You must have the following tools installed:
* [Git](https://git-scm.com/)
* [Docker](https://www.docker.com/get-started)
* [Docker Compose](https://docs.docker.com/compose/install/)
* [Python 3.9+](https://www.python.org/) & `pip` (for generating the Protobuf files)

### 1. Clone the Repository

```bash
git clone [YOUR_REPOSITORY_URL_HERE]
cd [YOUR_REPO_NAME]
2. Generate Protobuf Files (CRITICAL STEP)
The .proto file is the contract. Before building the containers, you must compile this contract into your chosen language's source files (in this case, Python).

First, install the gRPC tools:

Bash

pip install grpcio grpcio-tools
Then, run the compiler command from the root of your project:

Bash

python -m grpc_tools.protoc \
    -I./protos \
    --python_out=./server \
    --grpc_python_out=./server \
    ./protos/helloworld.proto

# This generates 'helloworld_pb2.py' and 'helloworld_pb2_grpc.py' inside the 'server/' directory,
# which are required by the Dockerfile.
3. Build and Run with Docker Compose
With the Protobuf files generated, run the entire stack with a single command:

Bash

docker-compose up --build
You will see the log output from both services: the server accepting the connection and the client printing the resulting greeting.

To stop and remove the containers and the network:

Bash

docker-compose down
📁 Project Structure
.
├── server/
│   ├── greeter_server.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── client/
│   ├── greeter_client.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── protos/
│   └── helloworld.proto     
│
├── .gitignore
├── docker-compose.yml       
└── README.md                
🤝 Contribution
Contributions are welcome! Please feel free to open issues or submit pull requests.

📄 License
This project is distributed under the MIT License. See the LICENSE file for more information.
