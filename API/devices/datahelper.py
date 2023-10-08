from flask import g

# def add_customer(c):
#     db.append(c)

# def create_product(name, price):
#     cur = g.cursor()
#     cur.execute(
#         '''
#         insert into product
#         (name, price)
#         values
#         (%s, %s)  
#         ''',
#         (name, price)
#     )
#     new_id = cur.lastrowid
#     cur.execute(
#         '''
#         select * from product where product_id = %s
#         ''',
#         (new_id)
#     )
#     ret_dict = cur.fetchone()

#     return ret_dict


# def get_products():
#     cur = g.cursor()
#     cur.execute(
#         '''
#         select * from product
#         '''
#     )
#     ret_dicts = cur.fetchall()

#     return ret_dicts




# def get_product(product_id):
#     cur = g.cursor()
#     cur.execute(
#         '''
#         select * from product where product_id=%s
#         ''',
#         (product_id)
#     )
#     ret_dict = cur.fetchone()

#     return ret_dict

# def update_product(product_id, name, price):
#     cur = g.cursor()
#     cur.execute(
#         '''
#         update product
#         set name=%s, price=%s
#         where product_id=%s 
#         ''',
#         (name, price, product_id)
#     )
#     cur.execute(
#         '''
#         select * from product where product_id = %s
#         ''',
#         (product_id)
#     )
#     ret_dict = cur.fetchone()

#     return ret_dict


# def delete_product(product_id):
#     cur = g.cursor()
#     cur.execute(
#             '''

#             delete from product where product_id=%s
#             ''',
#             (product_id)
#         )
 
#     rowcount = cur.rowcount
    
#     return rowcount > 0





# def device_name(name):
#     cur = g.cursor()
#     cur.execute(
#         '''
#         select * from devices where name=%s
#         ''',
#         (name)
#     )
#     ret_dict = cur.fetchone()

#     return ret_dict != None

def is_device_name_existed(neme):
    cur = g.cursor()
    cur.execute(
        '''
        select * from lamp_devices.devices where name=%s
        ''',
        (neme)
    )
    ret_dict = cur.fetchone()

    return ret_dict != None

def create_device(name,status):
    cur = g.cursor()
    cur.execute(
        '''
        insert into lamp_devices.devices
        (name,status,created_at)
        values
        (%s, %s,now())  
        ''',
        (name,status)
    )
    device_id = cur.lastrowid
    cur.execute(
        '''
        select * from lamp_devices.devices where device_id = %s
        ''',
        (device_id)
    )
    ret_dict = cur.fetchone()

    return ret_dict

def get_devices():
    cur = g.cursor()
    cur.execute(
        '''
        select * from lamp_devices.devices
        '''
    )
    ret_dicts = cur.fetchall()

    return ret_dicts

def get_device(name):
    cur = g.cursor()
    cur.execute(
        '''
        select * from lamp_devices.devices where name=%s
        ''',
        (name)
    )
    ret_dicts = cur.fetchone()

    return ret_dicts

def is_devices_status_existed(status):
    cur = g.cursor()
    cur.execute(
        '''
        select * from lamp_devices.devices where status=%s
        ''',
        (status)
    )
    ret_dict = cur.fetchall()

    return ret_dict != None

def get_devices_status(status):
    cur = g.cursor()
    cur.execute(
        '''
        select * from lamp_devices.devices where status=%s
        ''',
        (status)
    )
    ret_dicts = cur.fetchall()

    return ret_dicts

def update_device_status(devcie_id,name,status):
    cur = g.cursor()
    cur.execute(
        '''
        update lamp_devices.devices 
        set name=%s, status=%s
        where devcie_id=%s
        ''',
        (name,status,devcie_id)
    )
    cur.execute(
        '''  
        insert into lamp_devices.devices_logs 
        (devcie_id,name,status,update_time)
        values
        (%s, %s, %s,now()) 
        ''',
        (devcie_id,name,status)
    )
    cur.execute(
        '''
        select * from lamp_devices.devices_logs 
        where 
        device_id =%s
        ''',
        (devcie_id)
    )
    ret_dicts = cur.fetchone()

    return ret_dicts

# def update_device_status_log(devcie_id,name,status):
#     cur = g.cursor()
#     cur.execute(
#         '''  
#         insert into lamp_devices.devices_logs 
#         (devcie_id,name,status,update_time)
#         values
#         (%s, %s, %s,now()) 
#         ''',
#         (devcie_id,name,status)
#     )
#     cur.execute(
#         '''
#         select * from lamp_devices.devices_logs 
#         where 
#         device_id =%s
#         ''',
#         (devcie_id)
#     )
#     ret_dicts = cur.fetchone()

#     return ret_dicts


def create_device_log(device_id,name,status):
    cur = g.cursor()
    cur.execute(
        '''
        insert into lamp_devices.devices
        (device_id,name,status,created_at)
        values
        (%s, %s, %s,now())  
        ''',
        (device_id,name,status)
    )
    cur.execute(
        '''
        select * from lamp_devices.devices_logs where device_id = %s
        ''',
        (device_id)
    )
    ret_dict = cur.fetchall()

    return ret_dict

def is_device_id_existed(device_id):
    cur = g.cursor()
    cur.execute(
        '''
        select * from lamp_devices.devices where device_id=%s
        ''',
        (device_id)
    )
    ret_dict = cur.fetchone()

    return ret_dict != None

def get_device_id_logs(device_id):
    cur = g.cursor()
    cur.execute(
        '''
        select * from lamp_devices.devices_logs where device_id=%s
        ''',
        (device_id)
    )
    ret_dicts = cur.fetchall()

    return ret_dicts

def delete_device(name):
    cur = g.cursor()
    cur.execute(
            '''
            delete from lamp_devices.devices where name=%s
            ''',
            (name)
        )
 
    rowcount = cur.rowcount
    
    return rowcount > 0


# def get_reviews(restaurant_id):
#     cur = g.cursor()
#     cur.execute(
#         '''
#         select * from reviews where restaurant_id=%s
#         ''',
#         (restaurant_id)
#     )
#     ret_dicts = cur.fetchall()

#     return ret_dicts


# def get_reviews_stats(restaurant_id):
#     cur = g.cursor()
#     cur.execute(
#         '''
#         select avg(rating) as avg_rating from reviews where restaurant_id=%s
#         group by restaurant_id
#         ''',
#         (restaurant_id)
#     )
#     ret_dict = cur.fetchone()

#     if ret_dict == None:
#         return None
#     else:
#         return ret_dict['avg_rating']


# def is_review_id_existed(review_id):
#     cur = g.cursor()
#     cur.execute(
#         '''
#         select * from reviews where review_id=%s
#         ''',
#         (review_id)
#     )
#     ret_dict = cur.fetchone()

#     return ret_dict != None


# def delete_review(review_id):
#     cur = g.cursor()
#     cur.execute(
#             '''
#             delete from reviews where review_id=%s
#             ''',
#             (review_id)
#         )
 
#     rowcount = cur.rowcount
    
#     return rowcount > 0