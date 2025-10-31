import pytest
from operation.user import delete_object
from tests.conftest import objects_data
from common.logger import application_logger

class TestObjectDeleter:
	@pytest.mark.parametrize("id, expected_success", objects_data["test_delete"])
	def test_delete_object(self, id, expected_success):
		application_logger.info("*************** 开始执行用例 ***************")
		result = delete_object(id)
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