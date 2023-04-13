# test_task_iSi_Technology

<details><summary> 📄 The task:</summary>

BackEnd iSi Technology test task<br>
(Simple chat)<br>
We need to provide an application with 2 models:<br>
● Thread (fields - participants, created, updated)<br>
● Message (fields - sender, text, thread, created, is_read)<br>
Thread can’t have more than 2 participants.<br>
1. Implement REST endpoints for:<br>
● creation (if a thread with particular users exists - just return it.);<br>
● removing a thread;<br>
● retrieving the list of threads for any user;<br>
● creation of a message and retrieving message list for the thread;<br>
● marking the message as read;<br>
● retrieving a number of unread messages for the user.<br>
2. Customize Django admin.<br>
3. Provide pagination(LimitOffsetPagination) where it is needed.<br>
4. Validation in URLs is required, comments are welcome.<br>
5. Add a README.md file with a description of how to run the test task.<br>
6. Create a dump of a database to load test data.<br>
7. Give access to the project in the GIT repository. (Public Access)<br>
Requirements:<br>
Djangо, DRF<br>
authentication Simple JWT or Django Token;<br>
database – SQLite<br>
</details>
<details><summary>📸 Screenshots:</summary>

![Image alt](https://github.com/Lioniys/test_task_iSi_Technology/raw/main/screen/1.png)
![Image alt](https://github.com/Lioniys/test_task_iSi_Technology/raw/main/screen/2.png)
![Image alt](https://github.com/Lioniys/test_task_iSi_Technology/raw/main/screen/3.png)
![Image alt](https://github.com/Lioniys/test_task_iSi_Technology/raw/main/screen/4.png)
![Image alt](https://github.com/Lioniys/test_task_iSi_Technology/raw/main/screen/5.png)
![Image alt](https://github.com/Lioniys/test_task_iSi_Technology/raw/main/screen/7.png)
![Image alt](https://github.com/Lioniys/test_task_iSi_Technology/raw/main/screen/6.png)
</details>
<details><summary>⏱ Quick start:</summary>

```commandline
pip install -r requirements.txt
python chat/manage.py runserver
```
Username: admin<br>
Password: admin<br>
Username: test1<br>
Password: test1test1<br>
Username: test2<br>
Password: test2test2<br>
</details>