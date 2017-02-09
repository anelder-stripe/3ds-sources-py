
## Run the demo

This demo can be used with either [ngrok](https://ngrok.io/) or Heroku.  This is a demonstration only and absolutely should *NOT* be used in a production environment.  This has "the bare bones" and does very little in the way of handling edge cases or errors.

To deploy directly to Heroku, click this button:

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

### Step #0: Install the Requirements via PIP

```
pip install -r requirements.txt
```

### Step #1: Turn on your Python web server (listening on localhost:5000)

Replace the keys below and run the following command in your terminal.

```bash
STRIPE_SECRET_KEY=sk_test_XXX STRIPE_PUBLISHABLE_KEY=pk_test_XXX python run.py
```

### Step #2: Route ngrok to host port 5000

Start an ngrok route to your machine.

```bash
ngrok http 5000
```

### Step #3: Access the demo from the browser on your iOS 10+ device

```bash
https://<YOURNGROKADDRESS>.ngrok.io/
```

*NOTE: This is over HTTPS!*
