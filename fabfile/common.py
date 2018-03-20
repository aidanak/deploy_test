from fabric.decorators import task
from fabric.operations import sudo, run, get
from fabric.state import env


@task
def gunicorn_logs():
    run("tail -f /var/log/gunicorn/deploy_test.log")


@task
def git_pull():
    """
    """
    run("cd ~/{}/; git pull".format(env.repo_name))


@task
def build_front():
    """
    """
    run("cd ~/{}/front/; npm install; npm run build;".format(env.repo_name))


@task
def update_supervisor():
    sudo("cp -r ~/{}/configs/supervisor/* /etc/supervisor/conf.d".format(env.repo_name))
    sudo("""supervisorctl reread;
            supervisorctl restart deploy_test;
            supervisorctl update;
            supervisorctl status;
        """)


@task
def update_nginx(is_first_launch=False):
    sudo("cp ~/{0}/configs/nginx/{1} /etc/nginx/sites-available".format(
         env.repo_name, env.nginx_conf))
    if is_first_launch:
        sudo("ln -s /etc/nginx/sites-available/{0} /etc/nginx/sites-enabled/{0}".format(env.nginx_conf))
    sudo("service nginx restart")


@task
def restart():
    run("cd ~/{} && . ./run.sh".format(env.repo_name))
    update_supervisor()
    update_nginx()
