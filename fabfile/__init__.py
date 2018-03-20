from . import common
from . import install

from fabric.decorators import task
from fabric.state import env

env.repository = "https://github.com/aidanak/deploy_test.git"
env.repository_ssh = "git@github.com:aidanak/deploy_test.git"
env.repo_name = "deploy_test"
env.user = "ubuntu"
env.key_filename = "~/deploy_test.pem"
env.hosts = ["18.218.177.156"]
env.nginx_conf = "deploy_test.conf"
