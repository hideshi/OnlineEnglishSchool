TEACHER_CHARACTERISTIC: 講師特性
================================

.. csv-table::
   :header: 論理名, 物理名, データ型, 桁数, PK, NOT NULL, 備考
   :widths: 20, 20, 10, 10, 4, 4, 40

   ID,ID,INTEGER,,○,○
   講師ID,TEACHER_ID,INTEGER,,,○
   特性,CHARACTERISTIC,INTEGER,,,○,1:TOEIC対策 2:初心者向け 3:子供向け 4:ビジネス英語 5:フリートーク 6:日本語OK
   登録ユーザID,REG_USER_ID,INTEGER
   登録タイムスタンプ,REG_TIMESTAMP,TIMESTAMP
   更新ユーザID,UPD_USER_ID,INTEGER
   更新タイムスタンプ,UPD_TIMESTAMP,TIMESTAMP
   削除フラグ,DELETE_FLG,CHAR,1
