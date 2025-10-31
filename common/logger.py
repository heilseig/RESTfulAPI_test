import logging
from datetime import datetime
from pathlib import Path

class LogManager:
	def __init__(self):
		self.setup_logging_envirement()
		self.initialize_logger()

	def setup_logging_envirement(self):
		"""配置日志环境"""
		base_dir = Path(__file__).parent.parent
		self.log_dir = base_dir / "logs"
		self.log_dir.mkdir(exist_ok=True)

		current_date = datetime.now().strftime("%Y%m%d")
		self.log_file = self.log_dir / f"{current_date}.log"

	def initialize_logger(self):
		"""初始化日志记录器"""
		self.logger = logging.getLogger("application_logger")
		self.logger.setLevel(logging.DEBUG)

		# 创建日志格式器
		log_format = self.create_log_formatter()

		# 配置处理器
		self.configure_handlers(log_format)

	def create_log_formatter(self):
		"""创建日志格式"""
		return logging.Formatter(
				'[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s',
				datefmt='%Y-%m-%d %H:%M:%S'
			)

	def configure_handlers(self, formatter):
		"""配置日志处理器"""
		# 文件处理器
		file_handler = logging.FileHandler(
				self.log_file,
				'a',
				encoding='utf8'
			)
		file_handler.setLevel(logging.DEBUG)
		file_handler.setFormatter(formatter)

		# 控制台处理器
		console_handler = logging.StreamHandler()
		console_handler.setLevel(logging.DEBUG)
		console_handler.setFormatter(formatter)

		self.logger.addHandler(file_handler)
		self.logger.addHandler(console_handler)

application_logger = LogManager().logger

def main():
	"""测试函数"""
	application_logger.info("=== 测试开始 ===")
	application_logger.debug("=== 测试结束 ===")		

if __name__ == "__main__":
	main()	