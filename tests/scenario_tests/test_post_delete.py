import pytest
from operation.user import register_object, delete_object
from common.logger import application_logger
from tests.conftest import scenario_data

class TestRegisterDelete:
	@pytest.mark.parametrize("name, data, expected_success", scenario_data["test_post_delete_object"])
	def test_post_delete_object(self, name, data, expected_success):
 		application_logger.info("*************** 开始执行用例 ***************")
 		register_result = register_object(name, data)
 		assert register_result.response.status_code == 200
 		id = register_result.response.json()["id"]
 		delete_result = delete_object(id)
 		assert delete_result.response.status_code == 200
 		application_logger.info(f"""测试了:
				expected_success
				期待结果:
				{expected_success}
				实际结果:
				{register_result.success}, {delete_result.success}
			""")
 		assert register_result.success == expected_success
 		assert delete_result.success == expected_success
 		application_logger.info("*************** 结束执行用例 ***************")