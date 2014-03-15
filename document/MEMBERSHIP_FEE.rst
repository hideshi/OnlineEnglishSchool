MEMBERSHIP_FEE: 会費
====================

.. csv-table::
   :header: 論理名, 物理名, データ型, 桁数, PK, NOT NULL, 備考
   :widths: 20, 20, 10, 10, 4, 4, 40

   ID,ID,INTEGER,,○,○
   生徒ID,STUDENT_ID,INTEGER,,,○
   支払日,DUE_DATE,DATE,,,○
   支払金額,PAYMENT_AMOUNT,INTEGER,,,○
   支払方法,PAYMENT_METHOD,CHAR,1,,○,1:クレジット決済 2:銀行振込
   登録ユーザID,REG_USER_ID,INTEGER
   登録タイムスタンプ,REG_TIMESTAMP,TIMESTAMP
   更新ユーザID,UPD_USER_ID,INTEGER
   更新タイムスタンプ,UPD_TIMESTAMP,TIMESTAMP
   削除フラグ,DELETE_FLG,CHAR,1
