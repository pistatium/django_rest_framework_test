# Django REST Frameworkを試してみた

[Django REST Frameworkを使って爆速でAPIを実装する](http://qiita.com/kimihiro_n/items/86e0a9e619720e57ecd8)

http://qiita.com/kimihiro_n/items/86e0a9e619720e57ecd8


* Djangoのセットアップ
* `Blog` Appの作成
* Django REST APIの組み込み

## Setup

```bash
mkvirtualenv django_rest_framework_test --python=`which python3`
pip install -r requirements.txt
cd src/django_rest_fraamework_test
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
