import time
from flask import Flask

app = Flask(__name__)

@app.route('/')
def get_index():
    # count = get_hit_count()
    return 'hello23'

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)