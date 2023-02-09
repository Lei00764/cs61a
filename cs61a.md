## Git和Github

### 基本流程

```bash
git init // 初始化，使用当前目录作为git仓库

git add -A // 添加当前目录所有文件到暂存区（追踪）

git commit -m "提交说明"  // 将暂存区的内容添加到仓库

git branch -M main // 创建main分支

// 以上为git命令，可单独在本地运行
// github相当于一个远程仓库

// 远程库的名字就是origin，这是Git默认的叫法（可以改成别的）
git remote add origin git@github.com:Lei00764/cs61a.git

git push -u origin main // 上传代码并合并
// 第一次push时需要使用-u参数，作用是将本地main分支和远程分支关联起来，默认名称相同
```

### 其他语法

```bash
git checkout xxx // 切换分支

// -u 表示把本地分支和远程分支进行关联，只在第一次推送的时候需要带 -u 参数
git push -u 远程仓库的别名 本地分支名称: 远程分支名称
git push -u origin payment:pay

//如果希望远程分支的名称和本地分支名称保持一直，可以对命令进行简化：
git push -u origin payment
```

### 注意点

- 合并分支时的注意点：假设要把 C 分支的代码合并到 A 分支，则必须先切换到 A 分支上，再运行 git merge 命令，来合并 C 分支！
- 删除分支时的注意点：删除分支不能在该分支上删除该分支

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













