from fabric.api import *

env.hosts = ['118.190.101.204']
env.user = 'root'
env.key_filename = 'fabric_id_rsa'


def deploy():
    with cd('/usr/local/python_code/lianjia_scrapy'):
        run('git pull')
        run('pipenv install')
