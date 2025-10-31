## RESTful API 测试项目

## 📋 项目简介

一个基于 RESTful-API.dev 提供的免费测试 API 构建的演示与测试项目
使用 Python + Requests + Pytest 进行自动化测试
使用 YAML 管理测试数据

## 🚀 项目特色

- ✅ 零配置，开箱即用：无需申请 API Key，无需复杂配置，克隆即用。

- ✅ 丰富的 CRUD 操作：完整支持对“对象”资源的创建、读取、更新和删除操作。

- ✅ 纯净的测试数据：所有操作均在沙盒环境中进行，不会影响真实数据。

- ✅ 多格式支持：API 响应支持 JSON 和 XML 格式。

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

## 🔧 项目部署

首先，下载项目源码后，在根目录下找到 ```requirements.txt``` 文件，然后通过 pip 工具安装 requirements.txt 依赖，执行命令：

```
pip3 install -r requirements.txt
```

接着，修改 ```config.ini``` 配置文件，在Windows环境下，安装相应依赖之后，在命令行窗口执行命令：

```
pytest
```

## 🙏 致谢

感谢 RESTful-API.dev 提供免费、稳定且易于使用的测试 API。