import pytest
import allure
from pathlib import Path
from api.user import user
from common.file_data_loader import file_loader
from common.logger import application_logger

def read_data(file_name):
	base_path = Path(__file__).parent.parent
	file_path = base_path / "data" / file_name
	data = file_loader.load_yaml(file_path)

	return data

objects_data = read_data("objects_test_data.yaml")
scenario_data = read_data("scenario_test_data.yaml")