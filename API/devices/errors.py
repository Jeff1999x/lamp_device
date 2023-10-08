from results import make_error_result

# #給unregister API使用的error
# e2001 = make_error_result("e2001","此客戶名字不存在")

#給add_devices API使用的error
e1001 = make_error_result("e1001","name不得重複且不得為空值")

# 給get_device API使用的error
e3001 = make_error_result("e3001","此 name 的設備不存在")

# 給get_device_status API使用的error
e4001 = make_error_result("e4001","此 status 的設備不存在")

# 給update_device API使用的error
e5001 = make_error_result("e5001","此 device_id 的設備不存在")
e5002 = make_error_result("e5002","此 name 的設備不存在")
e5003 = make_error_result("e5003","此 status 應為1(true)或是0(false)")

# 給get_device_log API使用的error
e6001 = make_error_result("e6001","此 device_id 的設備不存在")

# 給update_device API使用的error
e7001 = make_error_result("e7001","此 name 的設備不存在")

# e1002 = make_error_result("e1002","rating需介於1~5之間")
# e1003 = make_error_result("e1002","comment需<=45個字")


#給get_reviews API使用的error
# e2001 = make_error_result("e2001","restaurant_id 不存在")

# #給get_reviews_stats API使用的error
# e3001 = make_error_result("e3001","restaurant_id不存在")

# #給delete_review API使用的error
# e4001 = make_error_result("e4001","review_id不存在")

# #給update API使用的error
# e3001 = make_error_result("e3001","product_id不存在")
# e3002 = make_error_result("e3002","price必須大於0")

# #給delete API使用的error
# e4001 = make_error_result("e4001","product_id不存在")