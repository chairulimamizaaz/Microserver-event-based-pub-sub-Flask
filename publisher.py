from flask import Flask, request, jsonify
import pika
import json

app = Flask(__name__)

def publish_message(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.exchange_declare(exchange='events', exchange_type='fanout')
    channel.basic_publish(exchange='events', routing_key='', body=json.dumps(message))
    connection.close()

@app.route('/publish', methods=['POST'])
def publish():
    data = request.json
    publish_message(data)
    return jsonify({"status": "Event published", "data": data}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
