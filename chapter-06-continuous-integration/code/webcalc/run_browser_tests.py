"""Start WebCalc, run headless behave tests, then stop the app.

    python3 run_browser_tests.py

Additional arguments are passed to behave, for example --junit.
Port 8080 must be free. For an already running app use python3 -m behave instead.
"""

from pathlib import Path
import subprocess
import sys
import time
from urllib.error import URLError
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parent
URL = 'http://127.0.0.1:8080'


def app_responds():
    try:
        with urlopen(URL, timeout=1) as response:
            return response.status == 200
    except (URLError, TimeoutError):
        return False


def main():
    if app_responds():
        print('Port 8080 already serves an app. Stop it before using this runner.', file=sys.stderr)
        return 1
    artifacts = ROOT / 'browser-test-artifacts'
    artifacts.mkdir(exist_ok=True)
    with (artifacts / 'app.log').open('w') as log:
        app = subprocess.Popen([sys.executable, 'main.py'], cwd=ROOT,
                               stdout=log, stderr=subprocess.STDOUT)
        try:
            deadline = time.monotonic() + 30
            while not app_responds():
                if app.poll() is not None or time.monotonic() >= deadline:
                    print('App failed to start. See browser-test-artifacts/app.log.', file=sys.stderr)
                    return 1
                time.sleep(0.2)
            result = subprocess.run(
                [sys.executable, '-m', 'behave', '-D', 'headless=true',
                 '-D', f'base_url={URL}', *sys.argv[1:]], cwd=ROOT,
            )
            return result.returncode
        finally:
            app.terminate()
            try:
                app.wait(timeout=5)
            except subprocess.TimeoutExpired:
                app.kill()
                app.wait()


if __name__ == '__main__':
    raise SystemExit(main())
