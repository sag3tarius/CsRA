#!/usr/bin/env python3
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

PASSWORD = "ДОНОВИЯ_ВЛАСТВУЕТ!"

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Read the incoming JSON
        length = int(self.headers.get('Content-Length'))
        data = json.loads(self.rfile.read(length).decode())

        user_password = data.get("password", "")
        user_token = data.get("token", "")

        # Check password
        if user_password != PASSWORD:
            self.respond({"success": False})
            return

        # Read the token from /bin/tkn
        try:
            with open("/bin/tkn", "r") as f:
                correct_token = f.read().strip()
        except:
            self.respond({"success": False})
            return

        # Compare token
        if user_token == correct_token:
            self.respond({"success": True})
        else:
            self.respond({"success": False})

    def respond(self, payload):
        response = json.dumps(payload).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response)

def run():
    server = HTTPServer(("0.0.0.0", 8080), Handler)
    server.serve_forever()

if __name__ == "__main__":
    run()
