Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
choco install mysql mysql-connector python git -y
Start-Process "C:\tools\mysql\current\bin\mysql.exe" -ArgumentList '-u root -e "create schema notes"'
py pip install django django-crispy-forms mysqlclient
Start-Process "C:\Program Files\Git\cmd\git.exe" -ArgumentList 'clone https://github.com/thertgers/app.git' -WorkingDirectory $env:USERPROFILE -Wait
cd "$env:USERPROFILE\app"
C:\Python39\python.exe .\manage.py migrate
C:\Python39\python.exe .\manage.py loaddata inital_data.json
C:\Python39\python.exe .\manage.py runserver
start 'http://localhost:8000'