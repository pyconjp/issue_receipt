# issue_receipt

* PyCon JP Businessチケット・Patronチケット・Tutorialチケットの領収書発行ページです。

* 2018.09.03
  - PyCon JP 2018対応
  - Django2.1.1にアップデート

### データの入れ替え

- `attendee_master_{year}.sqlite3`を`issueReceipt`に配置する

- `issueReceipt/issueReceipt/settings.py`の以下の箇所を配置したファイルに合わせて書き換える

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'attendee_master_{year}.sqlite3')
    }
}
```
  
- migrateする

```
$ python manage.py migrate --fake issuing
$ python manage.py makemigrations issuing
$ python manage.py migrate
```
