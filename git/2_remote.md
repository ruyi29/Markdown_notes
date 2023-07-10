# git基本使用2

## 1.github配置
创建SSH Key
```
$ ssh-keygen -t rsa -C "youremail@example.com"
```
然后一路回车

登陆GitHub，打开“Settings”，“SSH and GPG Keys”页面：

然后，点“NEW SSH Key”，填上任意Title，在Key文本框里粘贴id_rsa.pub文件的内容
（id_rsa.pub文件在用户主目录.ssh文件夹里）

## 2.远程仓库
登录Github，Create a new repo后填写Repository name（其余默认即可）
### 在本地关联远程仓库(在本地仓库中执行)
```
$ git remote add origin git@github.com:ruyi29/learngit.git
```
learngit为github上仓库的名字
关联一个远程库时必须给远程库指定一个名字，origin是默认习惯命名；

### 将本地库的内容推送到远程库上
第一次加-u，之后不用
```
$ git push -u origin master
$ git push origin master
$ git push -f origin 分支名  --> 覆盖提交
```
实际上是把当前分支master推送到远程。

由于远程库是空的，我们第一次推送master分支时，加上了-u参数，Git不但会把本地的master分支内容推送的远程新的master分支，还会把本地的master分支和远程的master分支关联起来

### 删除远程库
查看远程库信息
```
$ git remote -v
```
删除
```
$ git remote rm origin
```
origin为远程库名字
此处的“删除”其实是解除了本地和远程的绑定关系
要真正删除远程库，需要登录到GitHub，在后台页面找到删除按钮再删除。

### 克隆远程仓库
```
$ git clone git@github.com:ruyi29/learngit.git
```
`git clone `+地址
#
## 3.分支管理
查看分支：`git branch`

创建分支：`git branch <name>`

切换分支：`git checkout <name>`或者`git switch <name>`

创建+切换分支：`git checkout -b <name>`或者`git switch -c <name>`

合并某分支到当前分支：`git merge <name>`

删除分支：`git branch -d <name>`