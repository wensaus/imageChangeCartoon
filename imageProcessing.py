import base64

import requests


def get_access_token():
    url = 'https://aip.baidubce.com/oauth/2.0/token'
    params = {
        'grant_type': 'client_credentials',
        'client_id': 'EtqI0YQqionPDxixlBPVfrLv',
        'client_secret': 'x3wZB1euVh30sqKwQx3zUlxSGQMzE7WQ'
    }
    response = requests.post(url, params)
    access_token = eval(response.text)['access_token']
    return access_token


def img_cartoon(img):
    url = 'https://aip.baidubce.com/rest/2.0/image-process/v1/selfie_anime'
    origin_im = open(img, 'rb')
    img = base64.b64encode(origin_im.read())
    origin_im.close()
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    params = {
        'access_token': get_access_token(),
        'image': img,
    }
    response = requests.post(url, data=params, headers=headers)
    if response:
        f = open('C:\\Users\\17746\\Desktop\\images\\result4.jpg', 'wb')
        anime = response.json()['image']
        anime = base64.b64decode(anime)
        f.write(anime)
        f.close()


if __name__ == '__main__':
    img_cartoon('C:\\Users\\17746\\Desktop\\images\\res.jpg')
