from app import app
from flask import request

def received_authentication(msg_event):
    pass

def received_msg(msg_event):
    app.logger.info('received message: {}'.format(msg_event))


def recieved_delivery_confirmation(msg_event):
    pass

def received_postback(msg_event):
    pass

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # pdb.set_trace()
    if request.method == 'POST' and request.json['object'] == 'page':
        data = request.json
        for entry in data['entry']:
            page_id = entry['id']
            time_of_event = entry['time']
            app.logger.info((page_id, time_of_event))
            for msg_event in entry['messaging']:
                if msg_event.get('optin'):
                    received_authentication(msg_event)
                elif msg_event.get('message'):
                    received_msg(msg_event)
                elif msg_event.get('delivery'):
                    recieved_delivery_confirmation(msg_event)
                elif msg_event.get('postback'):
                    received_postback(msg_event)
                else:
                    print('Webhook received unknown messaging event: {}'.format(msg_event))
                return 'ok'

    if request.args['hub.verify_token'] == 'huyarker':
        return request.args['hub.challenge']
    else:
        return 'give me verify token'
