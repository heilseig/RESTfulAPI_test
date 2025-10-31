import pytest
from operation.user import get_all_objects_info, get_single_object_info
from common.logger import application_logger
from tests.conftest import objects_data

class TestGetObjectInfo:
	@pytest.mark.parametrize("expected_user_count, expected_id_unique", 
		objects_data["test_get_all_objects_info"])
	def test_get_all_objects_info(self, expected_user_count, expected_id_unique):
		application_logger.info("********** 开始执行用例 **********")
		result = get_all_objects_info()
		assert result.response.status_code == 200 
		application_logger.info(f"""测试了:
				user_count, id_unique, expected_success
				期待结果:
				{expected_user_count}, {expected_id_unique},
				实际结果:
				{result.user_count}, {result.id_unique}
			""")
		assert result.user_count == expected_user_count
		assert result.id_unique == expected_id_unique
		application_logger.info("********** 结束执行用例 **********")

	@pytest.mark.parametrize("id, expected_name, expected_success", 
		objects_data["test_get_single_object_info"])
	def test_get_single_object_info(self, id, expected_name, expected_success):
		application_logger.info("********** 开始执行用例 **********")
		result = get_single_object_info(id)
		assert result.response.status_code == 200 or 404
		application_logger.info(f"""测试了:
				name, expected_success 
				期待结果:
				{expected_name}, {expected_success}
				实际结果:
				{result.name}, {expected_success}
			""")
		assert result.name == expected_name or result.name is None
		application_logger.info("********** 结束执行用例 **********")