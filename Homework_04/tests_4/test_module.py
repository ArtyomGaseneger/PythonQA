import requests


def test_received_status(url, status_code):
    received_status = None
    try:
        response = requests.get(url=url)
        response.raise_for_status()
    except requests.ConnectionError:
        received_status = 404
    except requests.HTTPError as e:
        received_status = e.response.status_code
    else:
        received_status = response.status_code
    finally:
        assert received_status == status_code
