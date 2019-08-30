import requests

def download_image(image):


    '''

    :param image: list of images as links
    :return: no value
    '''


    for link in range(len(image)):
        r = requests.get(image[link])

        with open("python_logo.png", 'wb') as f:

         f.write(r.content)

if __name__ == '__main__':

    links = [ "https://bucketdemotrill.s3-ap-southeast-1.amazonaws.com/1.jpeg_1547107887.jpeg",
                "https://bucketdemotrill.s3-ap-southeast-1.amazonaws.com/1.jpeg_1548664079.jpeg",
                    "https://bucketdemotrill.s3-ap-southeast-1.amazonaws.com/1.jpeg_1549956673.jpeg"]

    download_image(links)