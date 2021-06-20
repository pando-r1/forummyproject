#create fixtures
python manage.py dumpdata home.Category > category.json
python manage.py dumpdata home.Post > post.json

#load fixtures
python manage.py loaddata home/fixtures/category.json
python manage.py loaddata home/fixtures/post.json