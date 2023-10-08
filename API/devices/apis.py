from flask import Blueprint, request, json, g
from dacite import from_dict
from dacite_config import config
from devices import dataclasses, datahelper, errors
from results import make_data_result

blueprint = Blueprint("devices", import_name = "devices")


#一、新增devices
@blueprint.route('', methods=["POST"])
def add_devices():
    #1. 解析JSON或參數
    x = json.loads(request.data)
    obj = from_dict(dataclasses.AddDevice, x, config=config)
    #2. 驗證資料
    #2.1. name不得重複且不得為空值0
    if  datahelper.is_device_name_existed(obj.name) == True:  
        return json.jsonify(errors.e1001)
    #3. device
    #3.1. 建立device
    s = datahelper.create_device(obj.name,obj.status)
    #3.2. 提交
    g.cursor().connection.commit()
   #4. 回傳devices
    return json.jsonify(make_data_result(s))

#二、取得所有devices table中的裝置
@blueprint.route('', methods=["GET"])
def get_devices():
    s = datahelper.get_devices()
   #4. 回傳產品
    return json.jsonify(make_data_result(s))

#三、取得特定name_devices狀態
@blueprint.route('/<name>', methods=["GET"])
def get_device(name):
    #1. 解析JSON或參數
    #1.1. 解析name為str
    try:
        name=str(name)
    except:
        return json.jsonify(errors.e3001)
    #2. 驗證資料
    #2.1. 驗證product_id是否存在
    if  datahelper.is_device_name_existed(name) == False:
        return json.jsonify(errors.e3001)
    #3. 取得產品
    s = datahelper.get_device(name)
   #4. 回傳產品
    return json.jsonify(make_data_result(s))


#四、取得特定狀態(staus)的devices
@blueprint.route('/<status>', methods=["GET"])
def get_devices_status(status):
    #1. 解析JSON或參數
    #2. 驗證資料
    #2.1. 驗證status是否存在
    if  datahelper.is_devices_status_existed(status) == False:
        return json.jsonify(errors.e4001)
    #3. 取得產品
    s = datahelper.get_devices_status(status)
   #4. 回傳產品
    return json.jsonify(make_data_result(s))


#五、更新 (切換) 特定devices狀態(開/關)-同時新增log紀錄
@blueprint.route('/<name>', methods=["PUT"])
def update_device(name):
    #1. 解析JSON或參數
    x = json.loads(request.data)
    obj = from_dict(dataclasses.UpdateDevice, x, config=config)
   #1.1. 解析name為str
    try:
        name = str(name)
    except:
        pass

    #2. 驗證資料
    #2.1. 驗證device_id是否存在
    if  datahelper.is_device_id_existed(obj.device_id) == False:
        return json.jsonify(errors.e5001)
    #2.2. 驗證name是否存在
    if  datahelper.is_device_name_existed(obj.name) == False:
        return json.jsonify(errors.e5002)
    #2.2 驗證status是否存在
    if  datahelper.is_devices_status_existed(obj.status) == False:
        return json.jsonify(errors.e5003)

    #3. 更新devices的資料
    success = datahelper.update_device_status(obj.device_id,obj.name,obj.status)
    # save = datahelper.update_device_status_log(obj.device_id,obj.name,obj.status)
    #3.2. 提交
    g.cursor().connection.commit()
    #4. 回傳是否成功更新devices的資料
    return json.jsonify(make_data_result({"success":success} ))
    # return json.jsonify(make_data_result({"success":success} and {"save":save}))

# #測試五、新增device_id_log
# @blueprint.route('/AddLog', methods=["POST"])
# def add_device_log():
#     #1. 解析JSON或參數
#     x = json.loads(request.data)
#     obj = from_dict(dataclasses.AddDevice, x, config=config)
#     #2. 驗證資料
#     #2.1. device_id是否存在
#     if  datahelper.is_device_id_existed(obj.device_id) == False:  
#         return json.jsonify(errors.e6001)
#     #3. device
#     #3.1. 建立device
#     s = datahelper.create_device_log(obj.device_id,obj.name,obj.status)
#     #3.2. 提交
#     g.cursor().connection.commit()
#    #4. 回傳devices
#     return json.jsonify(make_data_result(s))


#六、取得特定devices更新日誌(table:devices_logs)-get_device_log
@blueprint.route('/<device_id>', methods=["GET"])
def get_device_id_logs(device_id):
    # 1. 解析JSON或參數

    #2. 驗證資料
    #2.1. 驗證device_id是否存在
    if  datahelper.is_device_id_existed(device_id) == False:
        return json.jsonify(errors.e6001)
    
    #3. 取得device_id的update_log
    s = datahelper.get_device_id_logs(device_id)

    #4. 回傳特定device_id的log
    return json.jsonify(make_data_result(s))

# 七、刪除設備(name)
@blueprint.route('/<name>', methods=["DELETE"])
def delete_device(name):
    # 1. 解析JSON
    # 1.1. 解析name為str
    try:
        name = str(name)
    except:
        pass
    #2. 驗證資料
    #2.1. 驗證device_name是否存在
    if  datahelper.is_device_name_existed(name) == False:
        return json.jsonify(errors.e7001) 
    #3. 刪除資料
    #3.1. 刪除資料
    success = datahelper.delete_device(name)
    #3.2. 提交
    g.cursor().connection.commit()
    #4. 回傳是否成功刪除
    return json.jsonify(make_data_result({"success":success}))





# # @blueprint.route('/<product_id>', methods=["PUT"])
# def update_product(product_id):
#     1. 解析JSON或參數
#     1.1. 解析JSON
#     x = json.loads(request.data)
#     obj = from_dict(dataclasses.UpdateProduct, x, config=config)
#     #1.2. 解析product_id為int
#     try:
#         product_id = int(product_id)
#     except:
#         pass

#     #2. 驗證資料
#     #2.1. 驗證product_id是否存在
#     if  isinstance(product_id, int) == False or \
#           datahelper.is_product_id_existed(product_id) == False:
#         return json.jsonify(errors.e3001) 
#     #2.2. 價格必須大於0
#     if obj.price < 0:
#         return json.jsonify(errors.e3002)
#     #3. 更新產品
#     #3.1. 更新產品
#     s = datahelper.update_product(product_id, obj.name, obj.price)
#     #3.2. 提交
#     g.cursor().connection.commit()
#    #4. 回傳產品
#     return json.jsonify(make_data_result(s))

# # @blueprint.route('<product_id>', methods=["DELETE"])
# # def delete_product(product_id):
#     1. 解析JSON
#     1.1. 解析product_id為int
#     try:
#         product_id = int(product_id)
#     except:
#         pass
#     #2. 驗證資料
#     #2.1. 驗證product_id是否存在
#     if  isinstance(product_id, int) == False or \
#           datahelper.is_product_id_existed(product_id) == False:
#         return json.jsonify(errors.e4001) 
#     #3. 刪除資料
#     #3.1. 刪除資料
#     success = datahelper.delete_product(product_id)
#     #3.2. 提交
#     g.cursor().connection.commit()
#     #4. 回傳是否成功刪除
#     return json.jsonify(make_data_result({"success":success}))