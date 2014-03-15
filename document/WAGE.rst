WAGE: 給料
==========

.. csv-table::
   :header: 物理名, 論理名, データ型, 桁数, PK, NOT NULL, 備考
   :widths: 20, 20, 10, 10, 4, 4, 40

   ID, ID, INTEGER, , ○, ○
   CUTOFF_DATE, 締め日, DATE
   PAYDAY, 支払日, DATE
   REG_USER_ID, 登録ユーザID, INTEGER
   REG_TIMESTAMP, 登録タイムスタンプ, TIMESTAMP
   UPD_USER_ID, 更新ユーザID, INTEGER
   UPD_TIMESTAMP, 更新タイムスタンプ, TIMESTAMP
   DELETE_FLG, 削除フラグ, CHAR, 1
