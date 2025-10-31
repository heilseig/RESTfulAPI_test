import requests
import json as complexjson
from common.logger import application_logger

class APIClient:
	def __init__(self, base_url):
		self.base_url = base_url
		self.session = requests.Session()
		self.method = {
			'GET': self.session.get,
			'POST': self.session.post,
			'PUT': self.session.put,
			'DELETE': self.session.delete,
			'PATCH': self.session.patch
		}

	def get(self, endpoint, **kwargs):
		return self.request(endpoint ,'GET', **kwargs)

	def post(self, endpoint, data=None, json=None, **kwargs):
		return self.request(endpoint, 'POST', data=data, json=json, **kwargs)

	def put(self, endpoint, data=None, **kwargs):
		return self.request(endpoint, 'PUT', data=data, **kwargs)

	def delete(self, endpoint, **kwargs):
		return self.request(endpoint, 'DELETE', **kwargs)

	def patch(self, endpoint, data=None, **kwargs):
		return self.request(endpoint, 'PATCH', data=data, **kwargs)

	def request(self, endpoint, method, data=None, json=None, **kwargs):
		full_url = self.build_url(endpoint)
		request_params = self.extract(kwargs)

		self.request_log(full_url, method, data, json, request_params)
		
		return self.request_execute(full_url, method, data, json, **kwargs)

	def build_url(self, endpoint):
		return f"{self.base_url}/{endpoint}"		

	def extract(self, kwargs):
		return {
			'headers': kwargs.get('headers'),
			'params': kwargs.get('params'),
			'files': kwargs.get('files'),
			'cookies': kwargs.get('cookies')
		}

	def request_execute(self, full_url, method, data, json, **kwargs):
		if method in ['PUT', 'PATCH'] and json:
			# PUT 和 PATCH 中没有提供直接使用json参数的方法，因此需要用data来传入
			data = complexjson.dumps(json)
			# 更新headers,但保持原有headers不变
			"""
			服务器通常期望 JSON 数据的 Content-Type 是 application/json，
			当我们手动将 JSON 对象转换为字符串并通过 data 传递时，
			requests 默认会使用 application/x-www-form-urlencoded
			"""
			kwargs = {
				**kwargs,
				'headers': {
					**kwargs.get('headers', {}),
					'Content-Type': 'application/json'
				}
			}

		request_func = self.method[method]

		if method == 'POST':
			return request_func(full_url, data=data, json=json, **kwargs)
		else:
			return request_func(full_url, data=data, **kwargs)

	def request_log(self, full_url, method, data, json, request_params):
		log_entries = [
			("请求地址", full_url),
			("请求方法", method),
			("请求头", request_params['headers']),
			("URL参数", request_params['params']),
			("表单数据", data),
			("JSON数据", json),
			("文件参数", request_params['files']),
			("Cookies", request_params['cookies'])
		]			

		for desc, content in log_entries:
			formatted_content = self.format_log_content(content)
			application_logger.info(f"接口{desc} ==>> {formatted_content}")

	def format_log_content(self, content):
		if content is None:
			return "无"

		if isinstance(content, (dict, list)):
			# Python3中，json在做dumps操作时，会将中文转换成unicode编码，因此设置 ensure_ascii=False
			return complexjson.dumps(content, indent=4, ensure_ascii=False)

		return str(content)					