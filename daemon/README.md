# Daemon

This is the the program that listens to the input (usually a microphone), transcribes the audio and sends it to the API to be translated and broadcasted to the client browsers.

## Virtual Environment

Create a virtual environment.

```sh
python3 -m venv env
```

then activate it via:

```sh
source env/bin/activate
```

Then install the dependencies:

```sh
pip install -r requirements.txt
```

### External Services

This code relies heavily on Google Cloud services such as:
- Cloud Text-to-Speech API
- Cloud Translation API

You need to make sure that you have a registered account with these two services activated.