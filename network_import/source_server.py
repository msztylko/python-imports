from flask import Flask

app = Flask(__name__)

@app.route('/source')
def source():
    content = []
    with open('source_code.py') as f:
        for line in f:
            content.append(line + '\n')
    return ''.join(content)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
