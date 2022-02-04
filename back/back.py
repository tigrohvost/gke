from flask import Flask
import random

api = Flask(__name__)

@api.route('/random', methods=['GET'])
def get_random():
      return str(random.randint(1,1000))

if __name__ == '__main__':
    api.run() 
