TEACHER_CHARACTERISTIC: 講師特性
================================

.. csv-table::
   :header: 物理名, 論理名, データ型, 桁数, PK, NOT NULL, 備考
   :widths: 20, 20, 10, 10, 4, 4, 40

   ID, ID, INTEGER, , ○, ○
   TEACHER_ID, 講師ID, INTEGER, , , ○
   CHARACTERISTIC, 特性, CHAR, 1, , ○, 1:TOEIC対策 2:初心者向け 3:子供向け 4:ビジネス英語 5:フリートーク 6:日本語OK
   REG_USER_ID, 登録ユーザID, INTEGER
   REG_TIMESTAMP, 登録タイムスタンプ, TIMESTAMP
   UPD_USER_ID, 更新ユーザID, INTEGER
   UPD_TIMESTAMP, 更新タイムスタンプ, TIMESTAMP
   DELETE_FLG, 削除フラグ, CHAR, 1
