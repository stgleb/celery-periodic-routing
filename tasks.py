from celery_app import app


@app.task(queue="first")
def first_task():
    """
    Run command: celery -A tasks worker -B -l info -Q first -n worker1
    :return:
    """
    print "Hello, i am second task"


@app.task(queue="second")
def second_task():
    """
    Run command: celery -A tasks worker -B -l info -Q second -n worker2
    :return:
    """
    print "Hello, i am second"


@app.task
def third_task():
    """
    Run command: celery -A tasks worker -B -l info -n worker3
    :return:
    """
    print "Hello, i am third"
