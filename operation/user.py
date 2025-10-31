from core.result import Result
from api.user import user
from common.logger import application_logger

def get_all_objects_info():
	result = Result()
	res = user.get_all_objects()
	result.response = res
	result.id_unique = False
	data = res.json()
	# 检查id是否唯一
	id_list = [item['id'] for item in data]
	if len(id_list) == len(set(id_list)):
		result.id_unique = True
	# 用户总数
	result.user_count = len(data)
	application_logger.info(f"查询全部项目 ==>> 返回结果 ==>> \n{data}")

	return result

def get_single_object_info(id):
	result = Result()
	res = user.get_single_object(id)
	result.response = res
	data = res.json()
	result.success = True
	# 检查是否成功
	if "error" in data:
		result.success = False
		result.error = data['error']
	# 姓名
	result.name = data.get('name', None)
	application_logger.info(f"查询单个项目 ==>> 返回结果 ==>> \n{data}")

	return result

def register_object(name, data):
	result = Result()
	json_data = {
		"name": name,
		"data": data
	}
	res = user.register(json=json_data)
	result.response = res
	data = res.json()
	result.success = False
	# 验证是否成功
	if "error" not in data:
		result.success = True
	application_logger.info(f"注册单个项目 ==>> 返回结果 ==>> \n{data}")

	return result

def update_object(id, name, data):
	result = Result()
	update_data = {
		"name": name,
		"data": data
	}
	res = user.update(id, json=update_data)
	result.response = res
	data = res.json()
	result.success = True
	# 验证是否成功
	if "error" in data:
		result.success = False
	application_logger.info(f"更新单个项目 ==>> 返回结果 ==>> \n{data}")

	return result

def delete_object(id):
	result = Result()
	res = user._delete(id)
	result.response = res
	data = res.json()
	result.success = True
	# 验证是否成功
	if "error" in data:
		result.success = False
	application_logger.info(f"删除单个项目 ==>> 返回结果 ==>> \n{data}")

	return result