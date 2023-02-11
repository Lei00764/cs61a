## Git和Github

### 创建流程

如果之前在本目录中没有创建git，请依次执行下列语句。

```bash
git init # 初始化，使用当前目录作为git仓库 本地

git add . # 添加当前目录所有文件到暂存区（追踪）

git commit -m "提交说明"  # 将暂存区的内容添加到仓库

git branch -M main # 创建main分支

# 以上为git命令，可单独在本地运行
# github相当于一个远程仓库
# 在执行下一行代码前，要创建一个github仓库，这里仓库名是cs61a
# 远程库的名字就是origin，这是Git默认的叫法（可以改成别的）
git remote add origin git@github.com:Lei00764/cs61a.git

git push -u origin main # 上传代码并合并
# 第一次push时需要使用-u参数，作用是将本地main分支和远程分支关联起来，默认名称相同
```

### 基本使用流程

在创建git，并且与github建立联系后，将修改后的文件上传到github的方法。

```bash
git add .  # 仅发生修改的文件会上传

git commit -m "提交说明

git push
```

### 其他语法

```bash
git log  # 查看目前为止所有的存档 

git status # 显示当前的工作目录下的提交文件状态

git reset --hard xxxx  # 回到过去（读档） 不需要整个 hash code 4位即可

git branch xxx # 创建分支
git checkout xxx # 切换分支

# -u 表示把本地分支和远程分支进行关联，只在第一次推送的时候需要带 -u 参数
git push -u 远程仓库的别名 本地分支名称: 远程分支名称
git push -u origin payment:pay

# 如果希望远程分支的名称和本地分支名称保持一直，可以对命令进行简化：
git push -u origin payment
```

注意：在使用 `git reset` 的hard模式之前, 你需要再三确认选择的存档是不是你的真正目标. 如果你读入了一个较早的存档, 那么比这个存档新的所有记录都将被删除! 这意为着你不能随便回到"将来"了。

前面介绍的是自己一个人管理github仓库的流程，下面介绍多人协作的方法。

### Github 工作流

```bash
git clone https://github.com/ultralytics/yolov5.git  # 克隆文件到本地

git checkout -b my_feature  # 创建并切换到新分支 效果：复制一份当前分支的内容到新分支上（现在有两个分支，其内容是一样的）

git diff  # 查看自己对代码的修改内容(相较于现在远程仓库现有内容)

git add 文件  # 把文件放到暂存区 让git知道我有一些代码想提交

git commit -m "提交信息"  # 将暂存取的内容提交到本地git，也就是让git管理

#以上是完成了本地管理

git push origin my_feature  # 将本地my_feature分支的内容push到github上 效果：github上多了一个my_feature分支

# 如果当push代码时发现，github仓库上main分支更新了，那么我就要测试在更新后，我更新的代码是否正确，因此，我现在需要将github更新后的内容同步到我的my_feature分支。
git checkout main  # 切换到本地的main分支，磁盘内容会发生修改

git pull origin main  # 把github上的现有分支main的内容（也就是上面说的main分支更新后的内容）拉取到本地

git checkout my_feature  # 此时磁盘内容有我自己修改的，但没有github上更新的

git rebase main  # 同步这两个代码 效果：把我的修改先放在一边，然后把github上的修改拿过来，然后在此基础之上，再把我的修改加上去
# 在这个过程中，有可能会出现rebase conflict，就需要手动选择需要哪一个代码

git push -f origin my_feature  # -f force

# 上述步骤，我们将修改后的代码成功push到github上的my_feature分支，接着就需要等仓库的主人接受我们的分支，即我们提交pull request，请求仓库主任把我这个分支给pull到这个项目

# 仓库主人一般使用squash merge
# 效果：把这一个分支上的所有改变合并成一个改变，然后commit到main分支
# 然后再把远端的my_feature删掉，即delete branch

# 在我们本地，也应该把my_feature删掉
git checkout main

git branch -D my-feature # 删除my-feature分支

git pull origin master  # 再把远程的拉下来
```

### 注意点

- 合并分支时的注意点：假设要把 C 分支的代码合并到 A 分支，则必须先切换到 A 分支上，再运行 git merge 命令，来合并 C 分支！如果两个人修改的是一个文件的不同位置，在使用merge指令时，git会自动帮我们合并，但若修改的是同一位置，此时会出现冲突！需要人为修改。
- 删除分支时的注意点：删除分支不能在该分支上删除该分支
- 不在分支没有被pr(pull request)之前merge，最好少commit，不然最后merge时非常困难，可以用rebase -i命令在本地压缩commit到一个里面

### 创建脚本

https://cn.vitejs.dev/guide/static-deploy.html

在你的项目中，创建一个 `deploy.sh` 脚本，包含以下内容（注意高亮的行，按需使用），运行脚本来部署站点：

```bash
#!/usr/bin/env sh

# 发生错误时终止
set -e

# 构建
npm run build

# 进入构建文件夹
cd dist

# 放置 .nojekyll 以绕过 Jekyll 的处理。
echo > .nojekyll

# 如果你要部署到自定义域名
# echo 'www.example.com' > CNAME

git init
git checkout -B main
git add -A
git commit -m 'deploy'

# 如果你要部署在 https://<USERNAME>.github.io
# git push -f git@github.com:<USERNAME>/<USERNAME>.github.io.git main

# 如果你要部署在 https://<USERNAME>.github.io/<REPO>
# git push -f git@github.com:<USERNAME>/<REPO>.git main:gh-pages

cd -
```

### 错误上传

有时候文件上传到github上，如果想要删除的话。

```bash
# 这句话视情况决定要不要
git pull origin master  # 将远程仓库的内容拉到本地

git rm -r --cached xxx # 删除文件 github上
# rm -rf xxx  # 删除文件 git （若要在本地也删除）

git commit -m "提示信息"

git push
```







