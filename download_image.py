import requests

def download_image(image):


    '''

    :param image: list of images as links
    :return: no value
    '''

    name=["img1","img2","img3"]
    for link in range(len(image)):
        r = requests.get(image[link])

        with open(name[link]+".jpg", 'wb') as f:
            f.write(r.content)


if __name__ == '__main__':

    links = [ "https://www.goodmorningquote.com/wp-content/uploads/2016/11/beautiful-inspirational-thoughts.jpg",
              "https://images-na.ssl-images-amazon.com/images/I/71j3RDZMD2L._SX425_.jpg",
              "https://www.goodmorningquote.com/wp-content/uploads/2016/11/best-inspirational-thoughts.jpg"
    ]
    download_image(links)

