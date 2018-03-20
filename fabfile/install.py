from fabric.decorators import task
from fabric.operations import sudo, run
from fabric.state import env


@task
def apt_get_update():
    """
    """
    sudo('apt-get update')


@task
def apt_get(*packages):
    """
    Runs apt-get install command for all provided packages
    """
    sudo('apt-get -y -f install %s' % ' '.join(packages), shell=False)


@task
def add_apt_repository(repository_name):
    sudo('add-apt-repository -y %s' % repository_name)


@task
def install():
    """
    """
    add_apt_repository('ppa:certbot/certbot')
    add_apt_repository('ppa:jonathonf/python-3.6')
    apt_get_update()
    apt_get("certbot")
    apt_get_update()
    apt_get("supervisor", "python-virtualenv", "build-essential", "git",
            "libjpeg-dev", "libfreetype6", "libfreetype6-dev",  "python3.6-dev",
            "zlib1g-dev", "wget", "libcurl4-openssl-dev", "libssl-dev",
            "libffi-dev", "sqlite3", "libpq-dev", "xvfb", "xorg", "postgresql",
            "postgresql-contrib", "python-pip", "wget", "nginx",
            "rabbitmq-server", "npm")
    git_clone()
    run("cd ~/; mkdir -p envs; cd envs; virtualenv {} -p python3.6;".format(env.repo_name))
    run("cd ~/; mkdir -p logs; cd logs; touch gunicorn_supervisor.log")
    sudo("chmod u+x ~/{}/configs/gunicorn/start.sh".format(env.repo_name))
    sudo("""mkdir -p /django_logs;
            mkdir -p /var/log/gunicorn;
            touch /var/log/gunicorn/deploy_test.log""")
    sudo("chown -R {} /static ".format(env.user))
    sudo("chown -R {} /media ".format(env.user))
    sudo("chown -R {} /django_logs ".format(env.user))


@task
def git_clone():
    """
    """
    run("cd ~/; git clone {}".format(env.repository))
