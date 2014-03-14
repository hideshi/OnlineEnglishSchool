TEACHER: 講師
=============

.. csv-table::
   :header: 物理名, 論理名, データ型, 桁数, PK, NOT NULL, 備考
   :widths: 20, 20, 10, 10, 4, 4, 40

   ID, ID, INTEGER, , ○, ○
   NICK_NAME, ニックネーム, VARCHAR, 40, , ○
   FIRST_NAME, 名, VARCHAR, 40, , ○
   MIDDLE_NAME, ミドルネーム, VARCHAR, 40
   LAST_NAME, 姓, VARCHAR, 40, , ○
   PASSWORD, パスワード, VARCHAR, 200, , ○
   SEX, 性別, CHAR, 1, , ○, 1:男性 2:女性
   BIRTH_DATE, 誕生日, DATE, , , ○
   HIRED_DATE, 雇入日, DATE, , , ○
   ADDRESS, 住所, VARCHAR, 400
   TEL, 電話番号, VARCHAR, 20
   EMAIL, メールアドレス, VARCHAR, 200
   BANK_ACCOUNT, 銀行口座, VARCHAR, 200
   SKYPE_ID, SkypeID, VARCHAR, 200
   HOBBY, 趣味, VARCHAR, 100
   UNIVERSITY, 大学, VARCHAR, 100
   COMMENT, コメント, VARCHAR, 400
   AUTHORITY, 権限, CHAR, 1, , ○, 1:管理者 2:一般講師
   URL, URL, VARCHAR, 400
   REG_USER_ID, 登録ユーザID, INTEGER
   REG_TIMESTAMP, 登録タイムスタンプ, TIMESTAMP
   UPD_USER_ID, 更新ユーザID, INTEGER
   UPD_TIMESTAMP, 更新タイムスタンプ, TIMESTAMP
   DELETE_FLG, 削除フラグ, CHAR, 1
