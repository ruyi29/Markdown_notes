## 执行 `sudo ./setup.bash `时
报错`unable to execute ./setup.bash:no such file or directory`

改为执行 
```
sudo bash ./setup.bash 
```

## 编译时报错
`relocation R_X86_64_PC32 against symbol ‘stderr@@GLIBC_2.2.5’ can not be used when making a shared object; recompile with -fPIC`
- 原因：由于链接库中使用了libfmt.a与libmyslam.so，编译时动态库与静态库不能混用。.a是静态库，.so是动态库，具体问题具体分析，有的是因为gflags安装是安装的静态库
- 解决：在编译时（cmake … -DGFLAGS_NAMESPACE=google -DCMAKE_CXX_FLAGS=-fPIC …）改成动态库就行了。
```
cd fmt/build/
cmake .. -DGFLAGS_NAMESPACE=google -DCMAKE_CXX_FLAGS=-fPIC ..
make -j8
sudo make install
```

## clangd下载后找不到标准库（配置vscode）
- clangd直接用apt装，vscode里下插件
- 并在工作区的setting里配置
	```
	{
		// 指定 clangd 可执行文件的路径（如果在系统路径中可直接使用 "clangd"）
		"clangd.path": "clangd",

		// 作为编译失败的备选标志，指定了包含文件夹的路径
		"clangd.fallbackFlags": [
			"-I${workspaceFolder}/include",
			//"-std=c++11",
			//"-l/usr/include/c++/11"
		],

		// 配置 clangd 启动参数
		"clangd.arguments": [
			//"--query-driver=/usr/bin/g++.exe",
			"--background-index",        // 启用后台索引
			"--compile-commands-dir=${workspaceFolder}/build",  // 设置编译命令文件夹
			"--all-scopes-completion",   // 允许在所有作用域中进行代码补全
			"--completion-style=detailed",  // 详细模式的代码补全
			"--clang-tidy",              // 启用 Clang-Tidy 静态代码分析
			"--log=verbose",             // 输出详细的日志信息
			"--pretty"                   // 漂亮的输出格式
		],

		// 配置 CMake 构建目录
		"cmake.buildDirectory": "${workspaceFolder}/build",

		// 配置 CMake 构建环境变量，使其生成编译命令数据库
		"cmake.buildEnvironment": {
			"CMAKE_EXPORT_COMPILE_COMMANDS": "ON"
		}
	}
	```
- 发现无法找到标准库，执行：`sudo apt-get install libstdc++-12-dev`
- 好像是因为我根本没有下载那个库？