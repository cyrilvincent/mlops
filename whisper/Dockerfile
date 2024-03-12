FROM nvcr.io/nvidia/pytorch:23.10-py3

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
 && apt-get install -y --no-install-recommends ffmpeg git \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Set up a new user named "user" with user ID 1000
RUN useradd -m -u 1000 user

# Switch to the "user" user
USER user

# Set home to the user's home directory
ENV HOME=/home/user \
	PATH=/home/user/.local/bin:$PATH

# Set the working directory to the user's home directory
WORKDIR $HOME/app

# install dependencies
RUN pip install --no-cache-dir --upgrade pip

# copy requirements.txt
COPY ./requirements.txt $HOME/app/requirements.txt

# install project requirements
RUN pip install -r requirements.txt

RUN mkdir -p /home/user/app/cache

# copy project
COPY --chown=user . $HOME/app

ENV TRANSFORMERS_CACHE=/home/user/app/cache

# expose port and run server
EXPOSE 7860
CMD ["python", "app.py"] 
