## Docker安装

### 使用StrataAI镜像

```bash
# 步骤1: 下载StrataAI官方镜像并准备好config2.yaml
docker pull StrataAI/StrataAI:latest
mkdir -p /opt/StrataAI/{config,workspace}
docker run --rm StrataAI/StrataAI:latest cat /app/StrataAI/config/config2.yaml > /opt/StrataAI/config/config2.yaml
vim /opt/StrataAI/config/config2.yaml # 修改配置文件

# 步骤2: 使用容器运行StrataAI演示
docker run --rm \
    --privileged \
    -v /opt/StrataAI/config/config2.yaml:/app/StrataAI/config/config2.yaml \
    -v /opt/StrataAI/workspace:/app/StrataAI/workspace \
    StrataAI/StrataAI:latest \
    StrataAI "Write a cli snake game"

# 您也可以启动一个容器并在其中执行命令
docker run --name StrataAI -d \
    --privileged \
    -v /opt/StrataAI/config/config2.yaml:/app/StrataAI/config/config2.yaml \
    -v /opt/StrataAI/workspace:/app/StrataAI/workspace \
    StrataAI/StrataAI:latest

docker exec -it StrataAI /bin/bash
$ StrataAI "Write a cli snake game"
```

`docker run ...`做了以下事情:

- 以特权模式运行，有权限运行浏览器
- 将主机文件 `/opt/StrataAI/config/config2.yaml` 映射到容器文件 `/app/StrataAI/config/config2.yaml`
- 将主机目录 `/opt/StrataAI/workspace` 映射到容器目录 `/app/StrataAI/workspace`
- 执行示例命令 `StrataAI "Write a cli snake game"`

### 自己构建镜像

```bash
# 您也可以自己构建StrataAI镜像
git clone https://github.com/geekan/StrataAI.git
cd StrataAI && docker build -t StrataAI:custom .
```
