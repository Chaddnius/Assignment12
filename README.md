#!/bin/bash

# Cloning the Repository and Setting up Docker on a VM

# 1. Clone the Repository:
#    - Clone the project repository.
#      Replace REPOSITORY_URL with the URL of your project repository.
git clone REPOSITORY_URL

# 2. Install Docker and Docker Compose:
#    - Update the package list.
sudo apt-get update

#    - Install Docker on the VM.
sudo apt-get install docker.io

#    - Install Docker Compose.
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/bin/docker-compose
sudo chmod +x /usr/bin/docker-compose

# 3. Build and Run the Docker Containers:
#    - Navigate to the project directory.
cd assignment-11

#    - Build and run the Docker containers.
docker-compose up -d

# 4. Test the API Endpoints:
#    - Use the provided CLI shell to test the API endpoints.
#      Example commands:
./my_api_cli.py fibonacci 5
./my_api_cli.py is-prime 10
# ... and so on

# 5. Cleanup (Optional):
#    - If needed, stop and remove the Docker containers.
docker-compose down
