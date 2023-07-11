## 执行 `sudo ./setup.bash `时
报错`unable to execute ./setup.bash:no such file or directory`

改为执行 
```
sudo bash ./setup.bash 
```
#
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