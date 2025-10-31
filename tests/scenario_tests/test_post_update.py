import pytest
from operation.user import register_object, update_object
from common.logger import application_logger
from tests.conftest import scenario_data

class TestRegisterUpdate:
	@pytest.mark.parametrize("name, data, expected_register_success", 
		scenario_data['test_post_update_object']['register'])
	@pytest.mark.parametrize("updated_name, updated_data, expected_updated_success", 
		scenario_data['test_post_update_object']['update'])
	def test_post_update_object(self, name, data, expected_register_success, updated_name, updated_data, expected_updated_success):
 		application_logger.info("*************** 开始执行用例 ***************")
 		register_result = register_object(name, data)
 		assert register_result.response.status_code == 200
 		id = register_result.response.json()["id"]
 		updated_result = update_object(id, updated_name, updated_data)
 		assert updated_result.response.status_code == 200
 		application_logger.info(f"""测试了:
				expected_register_success, expected_updated_success
				期待结果:
				{expected_register_success}, {expected_updated_success}
				实际结果:
				{register_result.success}, {updated_result.success}
			""")
 		assert register_result.success == expected_register_success
 		assert updated_result.success == expected_updated_success
 		application_logger.info("*************** 结束执行用例 ***************")