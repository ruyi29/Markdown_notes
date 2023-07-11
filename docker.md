# Docker
### 1. 简介
- 一个用于 构建、运行、传送 应用程序的平台（build、run、share）
- 是容器技术的一种实现 

### 2. 优点
- 轻量级且占用的资源少
- 高效快速部署
- 启动快，资源占用少

### 3. 基本概念
- image：可执行程序
- container：运行起来的进程
- Dockerfile：image的源代码（docker相当于编译器）
- 镜像：用来创建容器的只读模板
- 容器：Docker的运行实例，提供一个运行应用程序的独立可移植环境
- Docker仓库：用来存储Docker镜像的地方（如Dockerhub）

### 4. 容器化过程
- 创建一个Dockerfile，使用Dockerfile构建镜像，指定所需程序和依赖配置
- 使用镜像创建，即交给docker编译（docker build），生成image
- 运行容器（docker run），image运行起来后就是docker container

### 5. 命令实现原理
docker使用了常见的CS架构，也就是client-server模式，docker client负责处理用户输入的各种命令，比如docker build、docker run，真正工作的其实是server，也就是docker demon，值得注意的是，docker client和docker demon可以运行在同一台机器上。
- `docker build`：当我们写完dockerfile交给docker“编译”时使用这个命令，client在接收到请求后转发给docker daemon，docker daemon根据dockerfile创建出“可执行程序”image。
- `docker run`：有了“可执行程序”image后就可以运行程序了，接下来使用命令docker run，docker daemon接收到该命令后找到具体的image，然后加载到内存开始执行，image执行起来就是所谓的container。
- `docker pull`：用户通过docker client发送命令，docker daemon接收到命令后向docker registry发送image下载请求，下载后存放在本地，这样我们就可以使用image了。
