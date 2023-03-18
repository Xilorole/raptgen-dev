# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Conda
RUN apt-get update && \
    apt-get install -y wget && \
    wget -q https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    bash Miniconda3-latest-Linux-x86_64.sh -bfp /usr/local && \
    rm Miniconda3-latest-Linux-x86_64.sh && \
    conda init

# Create a Conda environment with required dependencies
RUN conda env create -f environment.yml

# Activate the Conda environment
SHELL ["conda", "run", "-n", "raptgen", "/bin/bash", "-c"]

# Make port 8000 available for the app
EXPOSE 8000

# Run the app when the container launches
# CMD ["python", "app.py"]