OFFICE: オフィス
================

.. csv-table::
   :header: 論理名, 物理名, データ型, 桁数, PK, NOT NULL, 備考
   :widths: 20, 20, 10, 10, 4, 4, 40

   ID,ID,INTEGER,,○,○
   名称,NAME,VARCHAR,100,,○
   郵便番号,ZIP_CODE,VARCHAR,20
   住所,ADDRESS,VARCHAR,400
   電話番号,TEL,VARCHAR,20
   SkypeID,SKYPE_ID,VARCHAR,200
   登録ユーザID,REG_USER_ID,INTEGER
   登録タイムスタンプ,REG_TIMESTAMP,TIMESTAMP
   更新ユーザID,UPD_USER_ID,INTEGER
   更新タイムスタンプ,UPD_TIMESTAMP,TIMESTAMP
   削除フラグ,DELETE_FLG,CHAR,1
