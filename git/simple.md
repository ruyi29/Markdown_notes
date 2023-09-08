# git基本使用
```
# 分支合并发布流程：
git add .			# 将所有新增、修改或删除的文件添加到暂存区
git commit -m "版本发布" # 将暂存区的文件发版
git status 			# 查看是否还有文件没有发布上去
git checkout test	# 切换到要合并的分支
git pull			# 在test 分支上拉取最新代码，避免冲突
git merge dev   	# 在test 分支上合并 dev 分支上的代码
git push			# 上传test分支代码
```

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

5. Git pull 强制拉取并覆盖本地代码
git默认不上传空文件夹
```
git fetch --all
git reset --hard origin/master
git pull
```