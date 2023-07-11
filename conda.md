# conda语法
参考链接：https://blog.csdn.net/chenxy_bwave/article/details/119996001

__1. 创建虚拟环境__
```conda create -n your_env_name python=X.X```
- your_env_name文件可以在Anaconda安装目录envs文件下找到。
- 注意至少需要指定python版本或者要安装的包
- 在不指定python版本时，自动安装最新python版本

__2. 激活虚拟环境__
- Linux: ```source activate your_env_name ```
- (Linux:``` conda activate your_env_name```)
- Windows: ```activate your_env_name```
- 使用python --version查看虚拟环境python版本

__3. 退出虚拟环境__
- Linux: ```conda activate / conda deactivate```
- Win: ```deactivate your_env_name ```
- 回到 base environment

__4. 删除虚拟环境__
- 删除环境：```conda remove -name your_env_name --all```(all不能省)
- 删除虚拟环境中的包：```conda remove package_name```或者```pip uninstall package_name```
  
__5. 查看有哪些虚拟环境__
- ```conda env list```
- ```conda info -e```
- ```conda info --envs```

__6.查询包的安装情况__

- 查询看当前环境中安装了哪些包 ```conda list``` / ```pip list```
- 查询当前Anaconda repository中是否有你想要安装的包 ```conda search package_name```
- 与互联网的连接是执行这个查询操作乃至后续安装的前提条件.

__7.包的导出和安装__

- ```pip freeze > requirements.txt```
- ```pip install -r requirements.txt```
