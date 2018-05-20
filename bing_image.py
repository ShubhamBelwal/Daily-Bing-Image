import requests,os,ctypes

bing_url = "http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt="
prefix = "https://www.bing.com"
resolution = "1366x768"
region_code = "en-in"
def get_and_set_wallpaper():
    bing_api = bing_url + region_code
    os.makedirs('Bing',exist_ok=True)
    dir_path = os.path.join(os.getcwd(),"Bing")
    response = requests.get(bing_api).json()
    url = response['images'][0]['urlbase']
    image_url = prefix + url + "_" + resolution + ".jpg"
    res = requests.get(image_url)
    res.raise_for_status()
    imageFile = open(os.path.join('Bing', os.path.basename(image_url)), 'wb')
    imageFile.write(res.content)
    imageFile.close()
    image = os.path.join(dir_path, url.replace("/", " ").split()[-1]) + "_" + resolution + ".jpg"
    SPI_SETDESKWALLPAPER = 0x0014
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image, 0)
    return

if __name__ == "__main__":
    get_and_set_wallpaper()
