# test_task_iSi_Technology
<details><summary>🏗 Deploy :</summary>


```commandline
docker-compose -f docker-compose.prod.yml up -d --build
docker-compose -f docker-compose.prod.yml exec web python src/manage.py makemigrations --noinput
docker-compose -f docker-compose.prod.yml exec web python src/manage.py migrate --noinput
docker-compose -f docker-compose.prod.yml exec web python src/manage.py collectstatic --no-input --clear
docker-compose -f docker-compose.prod.yml exec web python src/manage.py createsuperuser --noinput
```


</details>

![Image alt](https://github.com/Lioniys/test_task_iSi_Technology/raw/main/screen/1.png)