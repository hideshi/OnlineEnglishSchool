SCHEDULE: スケジュール
======================

.. csv-table::
   :header: 物理名, 論理名, データ型, 桁数, PK, NOT NULL, 備考
   :widths: 20, 20, 10, 10, 4, 4, 40

   ID, ID, INTEGER, , ○, ○
   TEACHER_ID, 講師ID, INTEGER, , , ○
   DATE, 日付, DATE, , , ○
   START_TIME, 開始時刻, TIME, , , ○
   RESERVATION_ID, 予約ID, INTEGER
