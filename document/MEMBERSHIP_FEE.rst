MEMBERSHIP_FEE: 会費
====================

.. csv-table::
   :header: 物理名, 論理名, データ型, 桁数, PK, NOT NULL, 備考
   :widths: 20, 20, 10, 10, 4, 4, 40

   ID, ID, INTEGER, , ○, ○
   STUDENT_ID, 生徒ID, INTEGER, , , ○
   DUE_DATE, 支払日, DATE, , , ○
   PAYMENT_AMOUNT, 支払金額, INTEGER, , , ○
   PAYMENT_METHOD, 支払方法, CHAR, 1, , ○, 1:クレジット決済 2:銀行振込
   REG_USER_ID, 登録ユーザID, INTEGER
   REG_TIMESTAMP, 登録タイムスタンプ, TIMESTAMP
   UPD_USER_ID, 更新ユーザID, INTEGER
   UPD_TIMESTAMP, 更新タイムスタンプ, TIMESTAMP
   DELETE_FLG, 削除フラグ, CHAR, 1
