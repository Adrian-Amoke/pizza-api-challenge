# Running the Flask App

To run the Flask app correctly and avoid import errors, use the following command from the project root directory:

```bash
python -m server.app
```

Alternatively, you can use the provided run script:

```bash
./run.sh
```

Make sure the script has execute permissions:

```bash
chmod +x run.sh
```

Do NOT run the app by executing `server/app.py` directly, as it will cause import errors due to relative imports.

# Running Flask-Migrate Commands

To run Flask-Migrate commands such as database migrations, make sure to set the `FLASK_APP` environment variable to `server.app`. For example:

```bash
FLASK_APP=server.app flask db init
FLASK_APP=server.app flask db migrate
FLASK_APP=server.app flask db upgrade
```

You can also run these commands with the environment variable set inline, or export it in your shell session before running the commands.

If you use the provided `run.sh` script, it already sets `FLASK_APP=server.app` for running the app, but you need to set it similarly when running migration commands.
