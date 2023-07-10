1. git add . 

2. git add xx命令可以将xx文件添加到暂存区，如果有很多改动可以通过 git add -A .来一次添加所有改变的文件。注意 -A 选项后面还有一个句点。 git add -A表示添加所有内容， git add . 表示添加新文件和编辑过的文件不包括删除的文件; git add -u 表示添加编辑或者删除的文件，不包括新添加的文件

3. git commit -m "提交注释"

git push origin  分支名称，一般使用：git push origin master

git ls-files 查看已提交仓库的文件
git clone git@github.com:ruyi29/Markdown_notes.git