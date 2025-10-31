import yaml
import json
from configparser import ConfigParser
from pathlib import Path
from common.logger import application_logger

class MyConfigParser(ConfigParser):
	"""重写转换方法，保留原始大小写"""
	def optionxform(self, optionstr):
		return optionstr

class FileDateLoader:
	"""文件数据加载器"""
	def __init__(self):
		self.support_formats = {
			'yaml': self.load_yaml,
			'yml': self.load_yaml,
			'json': self.load_json,
			'ini': self.load_ini,
			'conf': self.load_ini
		}

	def load_file(self, file_path):
		"""根据扩展名选择解析器"""
		path = Path(file_path)

		if not path.exists():
			raise FileNotFoundError(f"文件不存在: {file_path}")

		file_extension = path.suffix.lower().lstrip('.')	
		loader_method = self.support_formats.get(file_extension)

		if not loader_method:
			raise ValueError(f"不支持的文件格式: {self.file_extension}")
		
		return loader_method(file_path)

	def load_yaml(self, file_path):
		"""加载YAML格式文件"""
		application_logger.debug(f"正在解析YAML文件: {file_path}")

		with open(file_path, encoding='utf8') as f:
			content = yaml.safe_load(f)
		
		application_logger.debug(f"YAML文件内容: {content}")
		return content

	def load_json(self, file_path):
		"""加载JSON格式文件"""
		application_logger.debug(f"正在解析JSON文件: {file_path}")

		with open(file_path, encoding='utf8') as f:
			content = json.load(f)
		
		application_logger.debug(f"JSON文件内容: {content}")
		return content
	
	def load_ini(self, file_path):
		"""加载INI格式文件"""
		application_logger.debug(f"正在解析INI文件: {file_path}")

		config = MyConfigParser()
		config.read(file_path, encoding='utf8')
		data = dict(config._sections)

		return data

file_loader = FileDateLoader()