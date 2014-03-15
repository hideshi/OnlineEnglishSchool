OFFICE: オフィス
================

.. csv-table::
   :header: 物理名, 論理名, データ型, 桁数, PK, NOT NULL, 備考
   :widths: 20, 20, 10, 10, 4, 4, 40

   ID, ID, INTEGER, , ○, ○
   NAME, 名称, VARCHAR, 100, , ○
   ZIP_CODE, 郵便番号, VARCHAR, 20
   ADDRESS, 住所, VARCHAR, 400
   TEL, 電話番号, VARCHAR, 20
   FAX, FAX番号, VARCHAR, 20
   REG_USER_ID, 登録ユーザID, INTEGER
   REG_TIMESTAMP, 登録タイムスタンプ, TIMESTAMP
   UPD_USER_ID, 更新ユーザID, INTEGER
   UPD_TIMESTAMP, 更新タイムスタンプ, TIMESTAMP
   DELETE_FLG, 削除フラグ, CHAR, 1
