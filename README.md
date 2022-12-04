# flask_search
一个基于Flask的数据查询系统，支持`Excel2007及以上版本产生的.xlsx等格式`（范围同openpyxl模块）

**TODO**：

- [x] Excel文件导入

- [ ] 数据转存数据库
- [ ] 网页上传数据、修改配置
- [ ] tbd...

## 安装

> 下文所有操作均默认读者已经安装好Python3.8或以上版本的Python环境，并且具有**良好的网络环境**

使用命令`git clone https://github.com/Lord2333/flask_search`克隆本项目到本地（国内用户可尝试在项目地址前加上`https://gh.j8.market `以加速下载），或者直接点击右侧的`release`进行下载，后进入项目文件夹，大概会有这些内容东西：

![](https://gh.j8.market/https://github.com/Lord2333/Pics/blob/main/img/fix-dir/Roaming/picgo/2022/12/04/10-43-47-be2076afdab2a22f9eff2474652f7467-20221204104347-3507b8.png)

### 首次运行

点击资源管理器上方的地址栏，输入`cmd`，敲回车出现一个命令行窗口（Linux操作系统直接切换至程序所在目录即可）

![](https://gh.j8.market/https://github.com/Lord2333/Pics/blob/main/img/fix-dir/28590/Desktop/2022/12/04/10-50-46-8fc51ad728be2f32b83a194cf8a33805-GIF%202022-12-4%2010-47-40-b23733.gif)

接着输入`pip install -r requirements.txt`安装依赖，如果提示`pip`命令不存在，就换成`pip3`再次尝试，可以使用`-i https://pypi.tuna.tsinghua.edu.cn/simple`参数提高国内安装速度。

在全部安装完成后，在命令行中输入`python main.py`或者`python3 main.py`即可运行程序，出现以下输出则程序正常运行。

```shell
 * Serving Flask app 'main' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 125-608-896
 * Running on http://127.0.0.1:8848/ (Press CTRL+C to quit)
```

打开浏览器访问`127.0.0.1:8848`即可

![](https://gh.j8.market/https://github.com/Lord2333/Pics/blob/main/img/fix-dir/Roaming/picgo/2022/12/04/11-05-22-68df4b41364b4c06190091e41e7ea667-20221204110521-55ad02.png)

> 程序默认运行在8848端口，可在main.py最后一行`app.run(debug=True, port=8848)`更改对应端口号，默认开启debug，可自行关闭。

## 使用

### 上传数据

项目中包含了一个`data.xlsx`文件，程序的查询条件是`data.xlsx`文件的第一列，例如：

| 学号            | 姓名 | 四级成绩 |
| --------------- | ---- | -------- |
| 202206010101001 | 张三 | 401      |
| 202206010102002 | 李四 | 469      |
| 202206010103003 | 王五 | 504      |

那么在查询条件里输入`202206010101001`即可得到张三的数据

![](https://gh.j8.market/https://github.com/Lord2333/Pics/blob/main/img/fix-dir/Roaming/picgo/2022/12/04/11-09-20-541a4933f4aa9264e14f89ae381f14f8-20221204110919-31701d.png)

只需要把数据表格名称更改为`data.xlsx`删除程序目录中原本的模板，上传即可使用。

### 修改网站信息

在`main.py`的12行-19行有配置信息

![](https://gh.j8.market/https://github.com/Lord2333/Pics/blob/main/img/fix-dir/Roaming/picgo/2022/12/04/11-20-15-4abc8aba57c9ca49a27dda908e72dd9b-20221204112015-902111.png)

可自行修改，修改后重启程序即可展示。

## 声明

Apache 2.0

本项目前端设计来自[php-Excel查询](http://12391.net/)

