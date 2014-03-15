TEACHER_SCHEDULE: 講師スケジュール
=====================================

.. csv-table::
   :header: 論理名, 物理名, データ型, 桁数, PK, NOT NULL, 備考
   :widths: 20, 20, 10, 10, 4, 4, 40

   ID,ID,INTEGER,,○,○
   講師ID,TEACHER_ID,INTEGER,,,○
   日付,DATE,DATE,,,○
   開始時刻,START_TIME,TIME,,,○
   ステータス,STATUS,CHAR,1,,○,1:予約なし 2:受講前 3:受講中 4:受講後 5:欠席 6:休講
   予約ID,RESERVATION_ID,INTEGER
   登録ユーザID,REG_USER_ID,INTEGER
   登録タイムスタンプ,REG_TIMESTAMP,TIMESTAMP
   更新ユーザID,UPD_USER_ID,INTEGER
   更新タイムスタンプ,UPD_TIMESTAMP,TIMESTAMP
   削除フラグ,DELETE_FLG,CHAR,1
