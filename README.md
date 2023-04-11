# test_task_iSi_Technology
<details><summary>🏗 Quick start :</summary>


```commandline
docker-compose -f docker-compose.prod.yml up -d --build
docker-compose -f docker-compose.prod.yml exec web python src/manage.py makemigrations --noinput
docker-compose -f docker-compose.prod.yml exec web python src/manage.py migrate --noinput
docker-compose -f docker-compose.prod.yml exec web python src/manage.py collectstatic --no-input --clear
docker-compose -f docker-compose.prod.yml exec web python src/manage.py createsuperuser --noinput
```


</details>


<details><summary> Screenshots :</summary>


![Image alt](https://github.com/Lioniys/test_task_iSi_Technology/raw/main/screen/1.png)
![Image alt](https://github.com/Lioniys/test_task_iSi_Technology/raw/main/screen/2.png)
![Image alt](https://github.com/Lioniys/test_task_iSi_Technology/raw/main/screen/3.png)
![Image alt](https://github.com/Lioniys/test_task_iSi_Technology/raw/main/screen/4.png)
![Image alt](https://github.com/Lioniys/test_task_iSi_Technology/raw/main/screen/5.png)
![Image alt](https://github.com/Lioniys/test_task_iSi_Technology/raw/main/screen/7.png)
![Image alt](https://github.com/Lioniys/test_task_iSi_Technology/raw/main/screen/6.png)


</details>

