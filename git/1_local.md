# git基本使用1
参考教程：[廖雪峰](https://www.liaoxuefeng.com/wiki/896043488029600)
#
## 1.git配置
```
$ git config --global user.name "Your Name"
$ git config --global user.email "email@example.com"
```
注意git config命令的--global参数，表示你这台机器上所有的Git仓库都会使用这个配置，也可以对某个仓库指定不同的用户名和Email地址。
#
## 2.初始化git仓库（repository）
### 进入要使用git管理的目录中，进行仓库初始化
（若使用Windows系统，请确保目录名（包括父目录）不包含中文。）
```
$ cd learngit
$ git init
Initialized empty Git repository in /Users/michael/learngit/.git/
```
仓库建成，并告诉你是一个空的仓库（empty Git repository） 

当前目录下多了一个.git的目录，不要手动修改，用`ls -ah`命令就可以看见。
#
## 3.添加文件到git仓库
### 进入该文件所在目录，把文件从工作区添加到暂存区（stage），然后提交到当前分支
Git命令必须在Git仓库目录内执行（`git init`除外），子目录也可以
```
$ git add readme.txt
$ git commit -m "wrote a readme file"
[master (root-commit) eaadf4e] wrote a readme file
 1 file changed, 2 insertions(+)
 create mode 100644 readme.txt
```
git commit命令，-m后面输入的是本次提交的说明

### commit可以一次提交很多文件，也可以多次add不同的文件，比如：
```
$ git add file1.txt
$ git add file2.txt file3.txt
$ git commit -m "add 3 files."
```
#
## 4.查看当前状态及修改内容
### 掌握工作区状态
```
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   readme.txt

no changes added to commit (use "git add" and/or "git commit -a")
```
### 查看修改
```
$ git diff readme.txt 
diff --git a/readme.txt b/readme.txt
index 46d49bf..9247db6 100644
--- a/readme.txt
+++ b/readme.txt
@@ -1,2 +1,2 @@
-Git is a version control system.
+Git is a distributed version control system.
 Git is free software.
 ```
也可以不指定文件，直接执行`git diff`
#
## 5.版本回退
### 查看版本控制历史
```
$ git log
或者
$ git log --pretty=oneline
```
### 回到上一个版本
```
$ git reset --hard HEAD^
```
### 回到历史版本
```
$ git reset --hard 1094a
```
1094a为commit_id。
### 查看命令历史以返回未来版本
```
$ git reflog
```
#
## 6.撤销修改
### 把readme.txt文件在工作区的修改全部撤销，回到最近一次`git commit`或`git add`时的状态。
```
$ git checkout -- readme.txt
```
没有--，就变成了“切换到另一个分支”的命令
### 把暂存区的修改撤销掉（unstage），重新放回工作区
```
$ git reset HEAD readme.txt
```
#
## 7.文件删除
`$ rm test.txt`
### 从版本库中删除该文件
```
$ git rm test.txt
```
### 把误删的文件恢复到最新版本
```
$ git checkout -- test.txt
```
git checkout其实是用版本库里的版本替换工作区的版本