STUDENT: 生徒
=============

.. csv-table::
   :header: 論理名, 物理名, データ型, 桁数, PK, NOT NULL, 備考
   :widths: 20, 20, 10, 10, 4, 4, 40

   ID,ID,INTEGER,,○,○
   ニックネーム,NICK_NAME,VARCHAR,40,,○
   姓,LAST_NAME,VARCHAR,40,,○
   名,FIRST_NAME,VARCHAR,40,,○
   パスワード,PASSWORD,VARCHAR,200,,○
   性別,SEX,CHAR,1,,○,1:男性 2:女性
   誕生日,BIRTH_DATE,DATE,,,○
   登録日,REGISTERED_DATE,DATE,,,○
   締め日,CUTOFF_DATE,INTEGER
   メールアドレス,EMAIL_ADDRESS,VARCHAR,200,,○
   SkypeID,SKYPE_ID,VARCHAR,200,,○
   ステータス,STATUS,CHAR,1,,○,1:体験入会 2:休会中 3:退会 4:プランＡ 5:プランＢ 6:プランＣ
   情報,INFORMATION,VARCHAR,4000
   登録ユーザID,REG_USER_ID,INTEGER
   登録タイムスタンプ,REG_TIMESTAMP,TIMESTAMP
   更新ユーザID,UPD_USER_ID,INTEGER
   更新タイムスタンプ,UPD_TIMESTAMP,TIMESTAMP
   削除フラグ,DELETE_FLG,CHAR,1
