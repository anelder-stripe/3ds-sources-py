import os
import stripe
import pprint
from flask import Flask, render_template, jsonify, request, Response

STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY")
STRIPE_PUBLISHABLE_KEY = os.environ.get("STRIPE_PUBLISHABLE_KEY")

app = Flask(__name__)
stripe.api_key = STRIPE_SECRET_KEY


@app.route("/")
def index():
    # register_domain(request.host.split(':')[0])
    return render_template("index.html", **{
        "STRIPE_PUBLISHABLE_KEY": STRIPE_PUBLISHABLE_KEY
    })

@app.route("/redirect_complete")
def redirect_complete():
    return "Redirect Complete"

@app.route("/charge", methods=["POST"])
def charge():

    token = request.form.get("token")

    if not token:
        return "ERROR", 400

    # Create Charge
    ch = stripe.Charge.create(
        amount=1099,  # must match the arguments of 3ds
        currency="eur",  # must match the arguments of 3ds
        source=token,
    )

    return jsonify(ch)


if __name__ == "__main__":

    if not STRIPE_SECRET_KEY:
        raise ValueError("Please pass the `STRIPE_SECRET_KEY` envionment variable.")

    if not STRIPE_PUBLISHABLE_KEY:
        raise ValueError("Please pass the `STRIPE_PUBLISHABLE_KEY` envionment variable.")

    app.run(host='0.0.0.0', port=5000, debug=True)
