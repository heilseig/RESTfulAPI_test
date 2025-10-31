import pytest
from operation.user import update_object
from tests.conftest import objects_data
from common.logger import application_logger

class TestObjectUpdater:
	@pytest.mark.parametrize("id, name, data, expected_success", objects_data["test_update"])
	def test_update_object(self, id, name, data, expected_success):
		application_logger.info("*************** 开始执行用例 ***************")
		result = update_object(id, name, data)
		assert result.response.status_code == 200 or 405
		application_logger.info(f"""测试了:
				expected_success
				期待结果:
				{expected_success}
				实际结果:
				{result.success}
			""")
		assert result.success == expected_success
		application_logger.info("********** 结束执行用例 **********")