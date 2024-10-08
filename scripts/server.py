from flask import Flask, request, jsonify
import logging
import os
import json

from swen_crypto import password_encrypt

app = Flask(__name__)


@app.route("/", methods=['POST'])
def handler():
    content = request.json
    with open("/tmp/output/passwords.txt", 'a') as f:
        content_bytes = json.dumps(content).encode()
        print(content_bytes)
        enc_bytes = password_encrypt(content_bytes, os.environ['KEY'])
        f.write(enc_bytes.decode("utf-8"))
        f.write('\n')
    app.logger.info("got a request")
    return jsonify({"response": "ok"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
