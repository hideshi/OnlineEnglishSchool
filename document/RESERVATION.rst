RESERVATION: レッスン予約
=========================

.. csv-table::
   :header: 物理名, 論理名, データ型, 桁数, PK, NOT NULL, 備考
   :widths: 20, 20, 10, 10, 4, 4, 40

   ID, ID, INTEGER, , ○, ○
   STUDENT_ID, 生徒ID, INTEGER, , , ○
   STATUS, ステータス, CHAR, 1, , ○, 1:受講前 2:受講中 3:受講後 4:欠席 5:休講
   TEACHER_EVALUATION_COMMENT, 講師評価コメント, VARCHAR, 1000
   CALL_QUALITY_EVALUATION, 通話品質評価, CHAR, 1, , , 1:最低 2:悪い 3:普通 4:良い 5:最高
