import os
import io
import json
import tarfile
import requests

BASE_URL = 'https://ipolcore.ipol.im/cp'

def get_session__does_not_work():
    session = requests.Session()

    r = session.get(f'{BASE_URL}/login')
    r.raise_for_status()

    tokenline = next(l for l in r.content.decode('utf-8').splitlines() if 'csrfmiddlewaretoken' in l)
    token = tokenline.split('value=\'')[1]
    token = token.split('\'')[0]

    payload = {
        'username': os.environ["IPOL_USERNAME"],
        'password': os.environ["IPOL_PASSWORD"],
        'remember': False,
        'csrfmiddlewaretoken': token,
    }
    r = session.post(f'{BASE_URL}/login', data=payload)
    r.raise_for_status()
    print(r, r.content.decode('utf-8').replace('\\n', ''))
    print(r.cookies)

    return session

def get_session():
    import browser_cookie3
    cookiejar = browser_cookie3.firefox(domain_name='ipolcore.ipol.im')

    session = requests.Session()
    session.cookies = cookiejar

    try:
        token = next(c.value for c in session.cookies if c.name == 'csrftoken')
    except StopIteration as e:
        print(cookiejar)
        raise e

    return session, token

def cli_ddl(demoid, ddl):
    session, token = get_session()
    url = f'{BASE_URL}/ajax_save_demoinfo_ddl/'
    ddl = json.loads(open(ddl).read())
    data = {
        'demoid': demoid,
        'ddlJSON': json.dumps(ddl, indent=4),
    }
    headers = {
        'X-CSRFToken': token,
        'X-Requested-With': 'XMLHttpRequest',
    }
    r = session.post(url, data=data, headers=headers)
    r.raise_for_status()

def cli_demoextras(demoid, directory):
    session, token = get_session()
    url = f'{BASE_URL}/add_demo_extra_to_demo/{demoid}/'
    data = {
        'csrfmiddlewaretoken': token,
    }

    with io.BytesIO() as buf:
        with tarfile.open(fileobj=buf, mode='w') as tar:
            tar.add(directory, arcname='.')
        demoextras = buf.getvalue()
    open('.demoextras.tar', 'wb').write(demoextras)

    files = {'myfile': demoextras}
    headers = {
        'referer': f'{BASE_URL}/demo_extras_of_demo/{demoid}/',
        'X-CSRFToken': token,
    }
    r = session.post(url, files=files, data=data, headers=headers)
    r.raise_for_status()

if __name__ == '__main__':
    import fire
    fire.Fire({'ddl': cli_ddl, 'demoextras': cli_demoextras})

