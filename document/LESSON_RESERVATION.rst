LESSON_RESERVATION: レッスン予約
================================

.. csv-table::
   :header: 物理名, 論理名, データ型, 桁数, PK, NOT NULL, 備考
   :widths: 20, 20, 10, 10, 4, 4, 40

   ID, ID, INTEGER, , ○, ○
   STUDENT_ID, 生徒ID, INTEGER, , , ○
   TEACHER_EVALUATION, 講師評価, CHAR, 1, , , 1:良い 2:悪い
   TEACHER_EVALUATION_COMMENT, 講師評価コメント, VARCHAR, 1000
   CALL_QUALITY_EVALUATION, 通話品質評価, CHAR, 1, , , 1:最低 2:悪い 3:普通 4:良い 5:最高
   REG_USER_ID, 登録ユーザID, INTEGER
   REG_TIMESTAMP, 登録タイムスタンプ, TIMESTAMP
   UPD_USER_ID, 更新ユーザID, INTEGER
   UPD_TIMESTAMP, 更新タイムスタンプ, TIMESTAMP
   DELETE_FLG, 削除フラグ, CHAR, 1
