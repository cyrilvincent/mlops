 docker run --rm -p 1234:7860 --gpus all --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 --name whisper-gpu -v /tmp:/tmp -v "${PWD}/cache":/home/user/app/cache whisper-gpu:latest
