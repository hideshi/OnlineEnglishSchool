PRICE_PACKAGE: 料金プラン
=========================

.. csv-table::
   :header: 論理名, 物理名, データ型, 桁数, PK, NOT NULL, 備考
   :widths: 20, 20, 10, 10, 4, 4, 40

   ID,ID,INTEGER,,○,○
   名称,NAME,VARCHAR,100,,○
   価格,PRICE,INTEGER,,,○
   適用開始日,APPLICATION_START_DATE,DATE,,,○
   適用終了日,APPLICATION_END_DATE,DATE,,,○
   公開フラグ,PUBLIC_FLG,BOOLEAN,,,○
   後継プラン,SUCCSSOR_PACKAGE,INTEGER
   登録ユーザID,REG_USER_ID,INTEGER
   登録タイムスタンプ,REG_TIMESTAMP,TIMESTAMP
   更新ユーザID,UPD_USER_ID,INTEGER
   更新タイムスタンプ,UPD_TIMESTAMP,TIMESTAMP
   削除フラグ,DELETE_FLG,CHAR,1
