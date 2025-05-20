# Docker Build, Run, and Push Instructions

## Building the Docker Image

1. Navigate to your project directory where the Dockerfile, app.py, and requirements.txt are located:
   ```bash
   cd /path/to/docker_assignment
   ```

2. Build the Docker image with a tag (replace 'yourusername' with your Docker Hub username):
   ```bash
   docker build -t yourusername/hello-world-api:1.0 .
   ```

3. Verify the image was created successfully:
   ```bash
   docker images
   ```
   You should see your image listed with the tag 'yourusername/hello-world-api:1.0'.

## Running the Container Locally

1. Run the container, mapping port 8080 from the container to port 8080 on your host:
   ```bash
   docker run -d -p 8080:8080 yourusername/hello-world-api:1.0
   ```

2. Verify the container is running:
   ```bash
   docker ps
   ```
   You should see your container listed with the port mapping 8080:8080.

3. Test the API by accessing it in your browser or using curl:
   ```bash
   curl http://localhost:8080
   ```
   You should receive a JSON response: `{"message":"Hello, World!","service":"Docker Assignment REST API","status":"success"}`

## Pushing the Image to Docker Hub

1. Log in to Docker Hub from the command line:
   ```bash
   docker login
   ```
   Enter your Docker Hub username and password when prompted.

2. Push the image to Docker Hub:
   ```bash
   docker push yourusername/hello-world-api:1.0
   ```

3. Capture a screenshot or save the log output of the push command for your assignment submission.

4. Verify the image is available on Docker Hub by visiting:
   ```
   https://hub.docker.com/r/yourusername/hello-world-api
   ```

## Additional Commands

- To stop the running container:
  ```bash
  docker stop $(docker ps -q --filter ancestor=yourusername/hello-world-api:1.0)
  ```

- To remove the container:
  ```bash
  docker rm $(docker ps -a -q --filter ancestor=yourusername/hello-world-api:1.0)
  ```

- To remove the image:
  ```bash
  docker rmi yourusername/hello-world-api:1.0
  ```
