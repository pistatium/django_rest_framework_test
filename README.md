# Django REST Frameworkを試してみた

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
