import requests
import re
import os


def DownloadImageFromURL(image_url, save_path):
	f = open(save_path,'wb')
	f.write(requests.get(image_url).content)
	f.close()


def FindImageInURL(url):
	r = requests.get(url)
	return re.findall('src=".+?\.jpg', r.text) + re.findall('src=".+?\.png', r.text)


def RipImagesFromUrl(url,save_path_base):
	image_urls = FindImageInURL(url)

	base_unique_suffix = 1

	while(os.path.exists(save_path_base+"_"+str(base_unique_suffix))):
		base_unique_suffix += 1

	unique_save_path_base = save_path_base+"_"+str(base_unique_suffix)

	os.makedirs(unique_save_path_base)

	for image_id in range(len(image_urls)):
		image_url = image_urls[image_id].replace("src=","").replace('"','')

		extension = image_url[-4:]
		
		save_path = os.path.join(unique_save_path_base,str(image_id)+"."+extension)
		try:
			DownloadImageFromURL(image_url, save_path)
		except:
			pass

url = "https://www.thesun.co.uk/news/2665370/washington-turned-into-war-zone-as-running-street-battles-rage-between-anti-trump-protesters-and-police/"


urls = []

urls.append("https://www.bing.com/images/search?q=violent+protest&qs=n&form=QBILPG&pq=violent+protest&sc=8-14&sp=-1&sk=")
#urls.append("http://mashable.com/2016/09/21/charlotte-violent-protest-photos/#I5wz34lzYPqX ")
#urls.append("https://www.google.co.uk/search?q=violent+protest+images+england")


output_path = os.path.join("images","rip")

for url in urls:
	RipImagesFromUrl(url,output_path)