# Create a ubuntu base image with python 3 installed.
FROM python:3

# Set the working directory
WORKDIR /opt/app

# copy all the files
COPY . .

# Install the dependencies
RUN apt-get -y update
RUN pip3 install -r requirements.txt

# Expose the required port
EXPOSE 5000

# Run the command
ENTRYPOINT ./entrypoint.sh
