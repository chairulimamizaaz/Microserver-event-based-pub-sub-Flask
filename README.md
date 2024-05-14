docker run -d --hostname my-rabbit --name some-rabbit -p 5672:5672 -p 15672:15672 rabbitmq:3-management

env\Scripts\activate

$env:FLASK_APP = "publisher.py"
flask run

python subscriber.py
