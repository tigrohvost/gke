from flask import Flask, request, render_template_string, jsonify
import datetime
import time
import threading
import requests

front = Flask(__name__)

running = False # to control loop in thread
#running = True # to control loop in thread

value = 0       

def rpi_function():
    global value

    print('start of thread')
    while running: # global variable to stop loop  
        #value += 1
        #url = 'http://127.0.0.1:8000/random'
        url = 'http://flaskapi:5000/random'
        res = requests.get(url)
        value = res.text
        time.sleep(1)
    print('stop of thread')


@front.route('/')
@front.route('/<device>/<action>')
def index(device=None, action=None):
    global running
    global value

    if device:
        if action == 'on':
            if not running:
                print('start')
                running = True
                threading.Thread(target=rpi_function).start()
            else:
                print('already running')
        elif action == 'off':
            if running:
                print('stop')
                running = False  # it should stop thread
            else:
                print('not running')

    return render_template_string('''<!DOCTYPE html>
   <head>
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
   </head>
   <body>
        <a href="/bioR/on">TURN ON</a>  
        <a href="/bioR/off">TURN OFF</a>
        <h1 id="num"></h1>
        <h1 id="time"></h1>
        <script>
            setInterval(function(){$.ajax({
                url: '/update',
                type: 'POST',
                success: function(response) {
                    console.log(response);
                    $("#num").html(response["value"]);
                    $("#time").html(response["time"]);
                },
                error: function(error) {
                    console.log(error);
                }
            })}, 1000);
        </script>
   </body>
</html>
''')

@front.route('/update', methods=['POST'])
def update():
    return jsonify({
        'value': value,
        'time': datetime.datetime.now().strftime("%H:%M:%S"),
    })

#front.run(host='0.0.0.0',port=8001) #debug=True
front.run()
