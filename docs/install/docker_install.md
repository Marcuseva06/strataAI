## Docker Installation

### Use default StrataAI image

```bash
# Step 1: Download StrataAI official image and prepare config2.yaml
docker pull StrataAI/StrataAI:latest
mkdir -p /opt/StrataAI/{config,workspace}
docker run --rm StrataAI/StrataAI:latest cat /app/StrataAI/config/config2.yaml > /opt/StrataAI/config/config2.yaml
vim /opt/StrataAI/config/config2.yaml # Change the config

# Step 2: Run StrataAI demo with container
docker run --rm \
    --privileged \
    -v /opt/StrataAI/config/config2.yaml:/app/StrataAI/config/config2.yaml \
    -v /opt/StrataAI/workspace:/app/StrataAI/workspace \
    StrataAI/StrataAI:latest \
    StrataAI "Write a cli snake game"

# You can also start a container and execute commands in it
docker run --name StrataAI -d \
    --privileged \
    -v /opt/StrataAI/config/config2.yaml:/app/StrataAI/config/config2.yaml \
    -v /opt/StrataAI/workspace:/app/StrataAI/workspace \
    StrataAI/StrataAI:latest

docker exec -it StrataAI /bin/bash
$ StrataAI "Write a cli snake game"
```

The command `docker run ...` do the following things:

- Run in privileged mode to have permission to run the browser
- Map host configure file `/opt/StrataAI/config/config2.yaml` to container `/app/StrataAI/config/config2.yaml`
- Map host directory `/opt/StrataAI/workspace` to container `/app/StrataAI/workspace`
- Execute the demo command `StrataAI "Write a cli snake game"`

### Build image by yourself

```bash
# You can also build StrataAI image by yourself.
git clone https://github.com/geekan/StrataAI.git
cd StrataAI && docker build -t StrataAI:custom .
```
