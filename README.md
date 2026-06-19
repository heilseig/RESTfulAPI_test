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
- api ====>> 接口封装层，如封装HTTP接口为Python接口
- common ====>> 各种工具类
- core ====>> requests请求方法封装、关键字返回结果类
- data ====>> 测试数据文件管理
- operation ====>> 关键字封装层，如把多个Python接口封装为关键字
- pytest.ini ====>> pytest配置文件
- requirements.txt ====>> 相关依赖包文件
- config.ini ====>> 配置文件
- tests ====>> 测试用例
- postman ====>> Postman 集合与环境变量
- reports ====>> 测试报告


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

## 🚀 项目特色

- ✅ 零配置，开箱即用：无需申请 API Key，无需复杂配置，克隆即用。

- ✅ 丰富的 CRUD 操作：完整支持对“对象”资源的创建、读取、更新和删除操作。

- ✅ 纯净的测试数据：所有操作均在沙盒环境中进行，不会影响真实数据。

## 📊 测试报告
执行 Newman 后，会在 reports/ 目录下生成 HTML 格式的测试报告，用浏览器打开即可查看详细结果。

## 🙏 致谢
感谢 RESTful-API.dev 提供免费、稳定且易于使用的测试 API。