from pathlib import Path
from core.api_client import APIClient
from common.file_data_loader import file_loader

class APIClientConfig:
	def __init__(self):
		self.load_configuration()

	def load_configuration(self):
		"""加载配置文件"""
		base_dir = Path(__file__).parent.parent
		config_file = base_dir / "config.ini"
		config_data = file_loader.load_ini(config_file)

		self.base_url = config_data["host"]["base_url"]

class UserServiceClient(APIClient):
	"""用户服务API客户端"""
	def __init__(self, api_config=None, **kwargs):
		config = api_config or APIClientConfig()
		super().__init__(config.base_url, **kwargs)

	def get_all_objects(self, **kwargs):
		return self.get("/objects", **kwargs)

	def get_single_object(self, id, **kwargs):
		return self.get(f"/objects/{id}", **kwargs)

	def register(self, **kwargs):
		return self.post("/objects", **kwargs)

	def update(self, id, **kwargs):
		return self.put(f"/objects/{id}", **kwargs)

	def _delete(self, id, **kwargs):
		return self.delete(f"/objects/{id}", **kwargs)

user = UserServiceClient()					