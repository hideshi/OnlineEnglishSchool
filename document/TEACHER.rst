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
   SKYPE_ID, SkypeID, VARCHAR, 200, , ○
   HOBBY, 趣味, VARCHAR, 100
   UNIVERSITY, 大学, VARCHAR, 100
   COMMENT, コメント, VARCHAR, 400
   URL, URL, VARCHAR, 400
   TOEIC, TOEIC, BOOLEAN, 1
   KIDS, キッズ, BOOLEAN, 1
   FREE_TALK, フリートーク, BOOLEAN, 1
   JAPANESE_OK, 日本語OK, BOOLEAN, 1
   BUSINESS_ENGLISH, ビジネス英語, BOOLEAN, 1
