from flask import Flask, request, jsonify

app = Flask(__name__)

PASSWORD = "ДОНОВИЯ_ВЛАСТВУЕТ!"  # same as in your HTML

@app.route("/validate_login", methods=["POST"])
def validate():
    data = request.get_json()

    user_password = data.get("password", "")
    user_token = data.get("token", "")

    # Validate password
    if user_password != PASSWORD:
        return jsonify(success=False)

    # Read root-only token file
    try:
        with open("/bin/tkn", "r") as f:
            correct_token = f.read().strip()
    except Exception as e:
        return jsonify(success=False)

    # Validate token
    if user_token == correct_token:
        return jsonify(success=True)

    return jsonify(success=False)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
