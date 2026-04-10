# 测试环境账号管理工具-需求文档

## 引言
  在日常测试工作中，环境账号分散在记事本、Excel、内部Wiki，每次切换环境都要翻半天；常用的测试工具网址（如 Mockaroo、SampleLib）收藏在浏览器书签里，换个电脑就得重新找；临时记录的测试要点和脚本路径更是散落各处。这些琐碎但又频繁使用的信息，严重拉低了测试效率。为此，我用 PySide6 结合AI开发了一款开源桌面小工具，将环境账号管理、常用名片自定义和记事本集成在一个面板中，并支持窗口置顶，真正告别记事本式的低效管理。

## 项目结构
```
项目目录/
├── conf/
│   └── data.json          # 配置文件（JSON格式）
├── log/
│   └── app.log         # 运行日志
├── notes/              # 笔记文件目录
├── src/               # 源代码
│   ├── main.py        # 主入口
│   ├── ui_mainwindow.py # UI定义
│   ├── app_controller.py # 业务逻辑
│   ├── data_store.py   # 数据存储
│   └── logger_config.py # 日志配置
├── test_tools.ui       # Qt Designer UI文件
└── requirements.txt   # 依赖包
```

## 需求简介
> 面板功能点从上到下开始说明
1. 环境账号管理（切换环境、多个账户、复制、网址内容、密码密文、新增/保存/删除）
2. 常用名片自定义（新增、保存、删除、跳转、复制）
3. 记事本（保存、切换笔记、打开目录）
4. 窗口置顶功能

## 功能点详解

### 3.1 环境账号管理
功能描述：

切换环境（dev / test / staging 等）

每个环境下可存多个账户

每个账户包含：环境名称、账户名称、网址、账号、密码（密文显示）

一键复制网址 / 账号 / 密码

环境名称和账户名称可直接编辑修改

- 账户名称未修改时：修改当前账户的账号和密码
- 账户名称被修改时：弹出确认对话框，点击确认后新增账户（账号和密码置空）

环境保存（新增/保存/删除环境）

技术实现：

数据存储：JSON 文件（conf/data.json）

UI 组件：QComboBox 切换环境（setEditable=True）

密码输入框：QLineEdit.EchoMode.Password

复制功能：QApplication.clipboard()

按钮组：新增、保存、删除（环境级别操作）

### 3.2 常用名片自定义
功能描述：

可添加多个名片（网址 / 路径 / 下载链接等）

每个名片包含：标题、内容（URL或命令）

支持复制文本

支持新增/保存/删除，但最少保留一个，默认"测试数据生成"不可删除，但可以修改，内容为https://www.mockaroo.com/

支持打开跳转（使用系统默认浏览器打开）

示例内置：

测试数据生成 → https://www.mockaroo.com/

测试文件生成 → https://samplelib.com/zh/

技术实现：

删除时校验条目数量，阻止删除最后一个预设项

使用 QDesktopServices.openUrl() 实现跳转

按钮组：保存、新增、删除、跳转（打开链接）

### 3.3 记事本
功能描述：

简单的文本编辑区域

支持保存到本地文件（notes目录）

支持切换不同笔记文件

支持打开笔记目录

技术实现：

QPlainTextEdit 配合 QPushButton 保存/加载

### 3.4 窗口置顶功能
QPushButton 切换窗口置顶

技术点：setWindowFlags(Qt.WindowType.WindowStaysOnTopHint) 后需要调用 show()

## 技术栈
- Python 3.11+
- PySide6 6.5.0+
- loguru 0.7.0+

## 数据格式
```json
{
  "environments": [
    {
      "name": "dev",
      "accounts": [
        {"name": "admin", "host": "http://dev.example.com", "account": "admin", "password": "123456"}
      ]
    }
  ],
  "cards": [
    {"title": "测试数据生成", "content": "https://www.mockaroo.com/"},
    {"title": "测试文件生成", "content": "https://samplelib.com/zh/"}
  ]
}
```