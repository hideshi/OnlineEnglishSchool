LESSON_SCHEDULE: レッスンスケジュール
=====================================

.. csv-table::
   :header: 物理名, 論理名, データ型, 桁数, PK, NOT NULL, 備考
   :widths: 20, 20, 10, 10, 4, 4, 40

   ID, ID, INTEGER, , ○, ○
   TEACHER_ID, 講師ID, INTEGER, , , ○
   DATE, 日付, DATE, , , ○
   START_TIME, 開始時刻, TIME, , , ○
   LESSON_RESERVATION_ID, 予約ID, INTEGER
   STATUS, ステータス, CHAR, 1, , ○, 1:予約なし 2:受講前 3:受講中 4:受講後 5:欠席 6:休講
   REG_USER_ID, 登録ユーザID, INTEGER
   REG_TIMESTAMP, 登録タイムスタンプ, TIMESTAMP
   UPD_USER_ID, 更新ユーザID, INTEGER
   UPD_TIMESTAMP, 更新タイムスタンプ, TIMESTAMP
   DELETE_FLG, 削除フラグ, CHAR, 1
