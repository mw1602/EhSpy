from flask import Flask, render_template
import os

app = Flask(__name__, static_url_path='')

@app.route('/', methods=['GET'])
@app.route('/maps', methods=['GET'])
def homepage():
    return render_template('maps.html', key=os.environ["google_maps_api_key"])

if __name__ == "__main__":
    app.run(debug=True)



