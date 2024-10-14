import requests
url = "https://gsom.spbu.ru/en/"
response = requests.get(url)
content = response.text
png_count = content.count('.png')
print(f"Number of png pictures on the link is: {png_count}")

import requests
url = "https://gsom.spbu.ru/en/"
response = requests.get(url)
if response.status_code == 200:
    content = response.text
    png_index = content.find('.png')
    if png_index != -1:
        start_index = content.rfind('"', 0, png_index) + 1
        relative_link = content[start_index:png_index + 4] 
        full_url = "https://gsom.spbu.ru" + relative_link
        print(f"Found image URL: {full_url}")
        img_response = requests.get(full_url)
        if img_response.status_code == 200:
            with open("downloaded_image.png", "wb") as file:
                file.write(img_response.content)
            print("Image downloaded successfully.")
        else:
            print("Failed to download image.")
    else:
        print("No .png image found in the webpage.")
else:
    print("Failed to retrieve the webpage.")