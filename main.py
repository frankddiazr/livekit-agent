
import subprocess
import sys
from flask import Flask

mode = 'dev'

app = Flask(__name__)


def start_agent():
    try:
        print(f"Starting LiveKit Agent in {mode} mode...")
        python_executable = sys.executable
        subprocess.Popen([python_executable, "agent.py", mode], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception as e:
        print(f"Error starting agent: {e}")


@app.route("/")
def home():
    start_agent()
    return "LiveKit AI Agent is running!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)