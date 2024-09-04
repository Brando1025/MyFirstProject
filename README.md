# MyFirstProject
a road to fortune

- [x] git & github
- [x] dependence
- [x] .gitignore
- [x] pytest
- [x] LICENSE
- [ ] CI/CD
- [ ] setup.cfg
- [ ] pre-commit
- [ ] docker
- [ ] makefile
- [ ] markdown
## About Git & GitHub
1. git的安装可以绑定到vscode中，这样方便我们直接在vscode中进行git操作，并且vscode有许多方便的git插件。
2. 好用的插件：**GitLens**
3. 当我们使用`git clone`或者`git pull`可以得到一个*库*。用 **.git**文件夹（一般是隐藏的）来进行管理的本地版本控制。
4. 初次使用git命令会配置用户名和密码，按提示来就好。
5. 当我们需要将本地库与远程库（github）绑定的时候可以使用SSH
   1. SSH在安装git后自带，输入ssh-keygen -t rsa -C "your email"。
   2. 获得密钥，打开pub后缀文件，复制内容。
   3. 站到github里SSH的KEY里。
   4. 以后pull最好都用SSH。
   5. [教程链接（我上面写的更简洁）](https://www.cnblogs.com/olive27/p/6056612.html)
6. vscode里打开终端，可以在终端右上角更改使用powershell或者git bash。
7. 相关git操作
    ```python
    #常用git命令
    #克隆仓库：
    git clone <git地址>
    #初始化仓库：
    git init

    #添加文件到暂存区：
    git add .
    #把暂存区的文件提交到仓库：
    git commit -m "提交信息"
    #查看提交的历史记录：
    git log --stat

    #工作区回滚：
    git checkout <filename>
    #撤销最后一次提交：
    git reset HEAD^1

    #以当前分支为基础新建分支：
    git checkout -b <branchname>
    #列举所有的分支：
    git branch
    #单纯地切换到某个分支：
    git checkout <branchname>
    #删掉特定的分支：
    git branch -d <branchname>
    #合并分支：
    git merge <branchname>

    #推送当前分支最新的提交到远程：
    git push
    #拉取远程分支最新的提交到本地：
    git pull

    #推送到主分支（main 或 master）
    git push origin main
    #推送到其他分支
    git push origin feature-branch
    #推送本地分支到远程的新分支(没有已存在的就新建，-u提供绑定)
    git push -u origin my-local-branch
    git push -u origin my-local-branch:remote-branch-name
    ```
8. 大多数操作可以利用GitLens进行可视化操作。
9. > [B站教程](https://www.bilibili.com/video/BV1db4y1d79C/?spm_id_from=333.1007.top_right_bar_window_history.content.click&vd_source=cc0f1a739a49e6242d2584c6f680be01)

## Dependence
环境依赖可以自动生成，主要有四种方法：
1. requirements.txt
   1. 格式：TXT
   2. 生成: `pip freeze > requirements.txt`
   3. 安装：`pip install -r requirements.txt`
2. Pipfile
   1. 格式：TOML
   2. 生成: 当使用 Pipenv 安装依赖时，Pipfile 文件会自动生成，`pipenv install numpy pandas`
   3. 安装：`pipenv install`
3. environment.yml
   1. 格式：YAML
   2. 生成: `conda env export > environment.yml`
   3. 安装：`conda env create -f environment.yml`
4. pyproject.toml
   1. 格式：TOML
   2. 生成: 当使用 Poetry 安装依赖时，pyproject.toml 文件会自动生成，`poetry add numpy pandas`
   3. 安装：`poetry install`

- **相对于*requirement.txt*，*environment.yml*可以包含conda和pip安装的，但前者只能查找出pip安装的。**

## .gitignore
- github可以自动生成模板

## Pytest
- pytest
  - 测试目标：
    - 单元测试：用于确保代码的基础功能是正确的。
    - 集成测试：用于验证模块之间的交互。
    - 端到端测试：用于模拟真实用户操作。
    - 回归测试：确保代码修改不会引入新问题。
  - 命名规则：
    - pytest 默认会自动查找以下命名规则的**文件**：
      - 文件名以 test_ 开头，例如 test_example.py。
      - 文件名以 _test.py 结尾，例如 example_test.py。
    - pytest 会自动发现并运行以下命名规则的**函数**：
      - 函数名以 test_ 开头，例如 def test_addition():。
    - pytest 会自动发现并运行以下命名规则的**类与方法**：
      - **类**名必须以 Test 开头。例如，class TestMyFunctions 是一个有效的测试类名称。
      - 类中的测试**方法**必须以 test_ 开头。例如，def test_addition(self): 会被自动识别为一个测试方法。
    - 文件名符合，函数或者类的命名不符合也不会执行
  - **@pytest.fixture 装饰器**：用于定义夹具，用于准备和清理测试所需的资源。只有需要提供特殊功能（如资源准备或清理）的函数才需要使用这个装饰器。普通的测试函数不需要这个装饰器。
- report of pytest
  - 自动生成测试报告，pytest-testreport，pytest-html，allure-pytest。以下使用pytest-testreport（和html包会起冲突）；allure需要下载软件。
  - pytest.ini和setup.cfg，以上两种方式可以为pytest配置一些初始化参数，规整后续可能用到pytest时（如CI/CD）的格式。
- `pytest --report=report.html --title=测试报告 --tester=Brando --desc=FirstProject  --template=2`

## LICENSE
- MIT和APACHE都是都是比较宽松的协议
