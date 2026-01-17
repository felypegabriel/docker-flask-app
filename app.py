from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Aplicação Python com Flask rodando no Docker!'

if __name__ == '__main__':
    # host='0.0.0.0' 
    app.run(debug=True, host='0.0.0.0', port=5000)
