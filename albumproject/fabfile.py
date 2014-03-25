from fabric.api import local, lcd


def prepare_deployment(branch_name="master"):
    local("python manage.py test albumproject")
    local("git add -p && git commit")


def deploy():
    with lcd('pwd'):

        # With git...
        local('git pull')

        # With both...
        local('python manage.py migrate albumapp')
        local('python manage.py test albumapp')
        local('python albumproject/wsgi.py')
