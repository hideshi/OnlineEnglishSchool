STUDENT: 生徒
=============

.. csv-table::
   :header: 物理名, 論理名, データ型, 桁数, PK, NOT NULL, 備考
   :widths: 20, 20, 10, 10, 4, 4, 40

   ID, ID, INTEGER, , ○, ○
   NICK_NAME, ニックネーム, VARCHAR, 40, , ○
   LAST_NAME, 姓, VARCHAR, 40, , ○
   FIRST_NAME, 名, VARCHAR, 40, , ○
   PASSWORD, パスワード, VARCHAR, 200, , ○
   SEX, 性別, CHAR, 1, , ○, 1:男性 2:女性
   BIRTH_DATE, 誕生日, DATE, , , ○
   REGISTERED_DATE, 登録日, DATE, , , ○
   EMAIL_ADDRESS, メールアドレス, VARCHAR, 200, , ○
   SKYPE_ID, SkypeID, VARCHAR, 200, , ○
   INFORMATION, 情報, VARCHAR, 4000
   REG_USER_ID, 登録ユーザID, INTEGER
   REG_TIMESTAMP, 登録タイムスタンプ, TIMESTAMP
   UPD_USER_ID, 更新ユーザID, INTEGER
   UPD_TIMESTAMP, 更新タイムスタンプ, TIMESTAMP
   DELETE_FLG, 削除フラグ, CHAR, 1
