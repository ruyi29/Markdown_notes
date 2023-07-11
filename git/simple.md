# git基本使用
1. 基本配置
```
git config --global user.name "Your Name"
git config --global user.email "email@example.com"
```
2. 初始化本地仓库
```
git init
git add .
git commit -m "提交注释"
```
- git add -A .表示一次添加所有改变的文件
- git add . 表示添加新文件和编辑过的文件不包括删除的文件
- git add -u 表示添加编辑或者删除的文件，不包括新添加的文件

1. 连接远程仓库
```
git remote add origin git@github.com:ruyi29/learngit.git
git push origin master
git pull origin master
```
- push：上传
- pull：拉取
- git push origin  分支名称

4. 查看/克隆

- `git ls-files `查看已提交仓库的文件

- `git clone git@github.com:ruyi29/Markdown_notes.git`