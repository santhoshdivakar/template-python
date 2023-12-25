import os
from flask import Flask, send_from_directory, render_template, redirect, Response

app = Flask(__name__)

port = int(os.environ.get("PORT", 5000))

@app.route('/api/<path:path>')
def serve_api(path):
    # send 200 OK
    return Response(f"Hello from {path}", status=200)


@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

@app.route('/')
def home():
   return send_from_directory('client/public', 'index.html')

@app.route('/<path:path>')
def all_routes(path):
    return send_from_directory('client/public', path)

if __name__ == "__main__":
    app.run(port=port)