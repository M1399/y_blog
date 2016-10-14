Requirements

•Python2.7
•Django1.9.9 
•Bootstrap3.3.0  #非必要
•virtualenv 1.11.6
创建虚拟环境 virtualenv ENV
启动虚拟环境
cd ENV
source ./bin/activate


Install

$ git clone https://github.com/M1399/y_blog


Usage

$ cd blog_y
在虚拟环境安装Python依赖
    pip install Django==1.9.9 
    pip install bootstrap-admin==0.3.3
    pip install markdown

$ python manage.py migrate
$ python manage.py makemigrations
$ python manage.py runserver 0.0.0.0:9999


