I faced a similar issue on Mac OS but I moved in another way. I used Virtual Environments.

First, create the virtual environment

python3 -m venv django-env

Then, use this environment

source django-env/bin/activate

Next, install django

python -m pip install django

Finally test django is working

django-admin startproject mysite