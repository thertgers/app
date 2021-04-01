Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
choco install mysql mysql-connector python git -y
mysql -u root -e "create schema notes"
python pip install django django-crispy-forms
git clone https://github.com/thertgers/app.git
cd 'C:\Program Files\Git\app'
python manage.py migrate
python manage.py loaddata inital_data.json
python manage.py runserver