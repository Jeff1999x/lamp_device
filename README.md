

**1. 物聯網（IoT）設備控制 API 範例**

假設您想要控制燈具的開關狀態。

**2. API端點表格**

| 端點                     | HTTP 方法 | 描述                           |
|--------------------------|-----------|--------------------------------|
| /devices                 | POST       | 新增連接的設備。       |
  /devices                 | GET       | 檢索所有的設備列表。       |
| /devices/{name}     | GET       | 檢索特定名稱設備的狀態。           |
| /devices/{status}     | GET       | 檢索特定狀態的設備。           |
| /devices/{name}     | PUT       | 更新特定設備的狀態（開/關）。 |
| /devices/{device_id}     | GET       | 取得特定設備的更新日誌。 |
| /devices/{name} | DELETE       | 刪除特定名稱的設備       |

**3. 所需的資料表格與欄位表格**

有一個資料表 "devices"，包含以下欄位：

| 欄位名稱 | 類型         | 描述                  |
|----------|--------------|-----------------------|
| device_id| 整數 (INT)   | 設備ID（主鍵）        |
| name     | 字串 (VARCHAR)| 設備名稱              |
| status   | 布林 (BOOLEAN)| 設備開/關狀態         |
| created_at| 時間 (DATETIME)| 新增的時間         |

另有一個資料表 "devices_logs"，包含以下欄位：

| 欄位名稱 | 類型         | 描述                  |
|----------|--------------|-----------------------|
 update_number| 整數 (INT)   | 設備更新次序（主鍵）        |
| device_id| 整數 (INT)   | 設備ID        |
| name     | 字串 (VARCHAR)| 設備名稱              |
| status   | 布林 (BOOLEAN)| 設備開/關狀態         |
| update_time| 時間 (DATETIME)| 新增的時間         |


