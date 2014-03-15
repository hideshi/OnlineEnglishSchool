RESERVATION: 予約
================================

.. csv-table::
   :header: 論理名, 物理名, データ型, 桁数, PK, NOT NULL, 備考
   :widths: 20, 20, 10, 10, 4, 4, 40

   ID,ID,INTEGER,,○,○
   生徒ID,STUDENT_ID,INTEGER,,,○
   レッスンリクエスト,LESSON_REQUEST,VARCHAR,400
   講師評価,TEACHER_EVALUATION,CHAR,1,,,1:良い 2:悪い
   講師評価コメント,TEACHER_EVALUATION_COMMENT,VARCHAR,1000
   通話品質評価,CALL_QUALITY_EVALUATION,CHAR,1,,,1:最低 2:悪い 3:普通 4:良い 5:最高
   登録ユーザID,REG_USER_ID,INTEGER
   登録タイムスタンプ,REG_TIMESTAMP,TIMESTAMP
   更新ユーザID,UPD_USER_ID,INTEGER
   更新タイムスタンプ,UPD_TIMESTAMP,TIMESTAMP
   削除フラグ,DELETE_FLG,CHAR,1
