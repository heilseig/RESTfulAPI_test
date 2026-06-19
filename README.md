# RESTful API 接口测试项目

## 📋 项目简介

本项目基于 RESTful-API.dev 提供的免费测试 API，完成了一套完整的接口测试实践。包含：

- **Postman** 接口调试、用例设计、断言编写与集合管理
- **Newman** 命令行执行 Postman 集合，生成 HTML 测试报告
- **Python + Pytest + Requests** 数据驱动自动化测试
- **YAML** 测试数据与代码分离管理
- **SQL** 数据校验脚本（模拟生产环境数据落库验证）

## 🛠 技术栈

类别       工具/技术                   用途 
接口测试   Postman + Newman           接口调试、用例管理、断言编写、命令行执行 
自动化测试 Python + Pytest + Requests 数据驱动测试、接口封装 
数据管理   YAML                       测试数据与代码分离 
版本控制   Git                        代码与测试资产版本管理 

## 📁 项目结构
RESTfulAPI_test/
├── postman/ # Postman 集合与环境变量
│ ├── RESTfulAPITest.json # 接口测试用例集合
│ └── dev.json # 开发环境变量配置
├── reports/ # 测试报告
│ └── test-report.html # Newman 生成的 HTML 报告
├── api/ # 接口封装层（Python）
│ └── user.py # 封装 HTTP 接口为 Python 方法
├── common/ # 工具类
│ ├── file_data_loader.py # YAML/JSON/INI 文件加载器
│ └── logger.py # 日志模块
├── core/ # 核心层
│ └── api_client.py # Requests 请求封装
├── data/ # 测试数据
│ ├── objects_test_data.yaml # 接口级测试数据
│ └── scenario_test_data.yaml # 场景级测试数据
├── operation/ # 业务关键字层
│ └── user.py # 封装业务操作（注册/查询/更新/删除）
├── tests/ # 测试用例层
│ ├── api_tests/ # 单接口测试用例
│ │ ├── test_objects.py # GET 查询测试
│ │ ├── test_posts.py # POST 新增测试
│ │ ├── test_update.py # PUT 更新测试
│ │ └── test_delete.py # DELETE 删除测试
│ └── scenario_tests/ # 业务场景测试用例
│ ├── test_post_delete.py # 注册后删除场景
│ └── test_post_update.py # 注册后更新场景
├── config.ini # 配置文件（base_url 等）
├── pytest.ini # Pytest 配置文件
├── requirements.txt # Python 依赖
└── README.md # 项目说明


## 🚀 快速开始

### 1. 克隆项目

git clone https://github.com/heiiseig/RESTfulAPI_test.git
cd RESTfulAPI_test

### 2. 安装依赖
pip install -r requirements.txt

### 3. 安装newman
npm install -g newman
npm install -g newman-reporter-html

### 4. 运行 Pytest 自动化测试
pytest

### 5. 运行postman集合
newman run postman/RESTfulAPITest.json -e postman/dev.json --reporters cli,html --reporter-html-export reports/test-report.html
将RESTfulAPITest.json和dev.json替换成你的文件

✅ 测试覆盖

接口	        方法	说明
/objects	    GET	    查询全部对象
/objects/{id}	GET	    查询单个对象
/objects	    POST	新增对象
/objects/{id}	PUT	    更新对象
/objects/{id}	DELETE	删除对象

📊 测试报告
执行 Newman 后，会在 reports/ 目录下生成 HTML 格式的测试报告，用浏览器打开即可查看详细结果。

🙏 致谢
感谢 RESTful-API.dev 提供免费、稳定且易于使用的测试 API。