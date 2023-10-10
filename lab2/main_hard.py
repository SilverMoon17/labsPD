import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import time;

# Создаем папку dataset, если она не существует
if not os.path.exists('dataset_hard'):
    os.mkdir('dataset_hard')


# Функция для загрузки изображений и сохранения их в подпапке dataset
def download_images(search_query, class_name, num_images=1000):
    # Создаем подпапку с соответствующим именем
    folder_path = os.path.join('dataset_hard', class_name)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    # URL страницы поиска изображений на Yandex
    search_url = f'https://yandex.ru/images/search?text={search_query}&type=photo'

    # Загружаем страницу поиска
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')


    img_a = soup.find_all('a', class_='serp-item__link')
    img_a_urls = [img_href['href'] for img_href in img_a]

    # Находим все ссылки на изображения

    # Счетчик для имен файлов
    file_count = 0

    # Загружаем изображения и сохраняем их
    for a in img_a_urls:
        if file_count >= num_images:
            break

        try:
            search_url_link = f'https://yandex.ru{a}'
            response_image = requests.get(search_url_link)
            soup_image = BeautifulSoup(response_image.text, 'html.parser')
            print(soup_image.prettify())

            img_urls = soup_image.find_all('img', class_='MMImage-Origin')
            img_url = [img['src'] for img in img_urls]
            # Проверяем, есть ли схема в URL изображения
            parsed_url = urlparse(img_url)
            if not parsed_url.scheme:
                img_url = urljoin(search_url, img_url)

            response = requests.get(img_url, stream=True)
            if response.status_code == 200:
                # Генерируем имя файла с ведущими нулями
                filename = str(file_count).zfill(4) + '.jpg'
                file_path = os.path.join(folder_path, filename)

                # Сохраняем изображение
                with open(file_path, 'wb') as file:
                    for chunk in response.iter_content(1024):
                        file.write(chunk)
                file_count += 1
            time.sleep(0.5)
        except Exception as e:
            print(f"Ошибка при загрузке изображения: {e}")



# Загружаем изображения для класса "zebra"
download_images('zebra', 'zebra', num_images=1000)

# Загружаем изображения для класса "bay horse"
download_images('bay_horse', 'bay_horse', num_images=1000)

print("Загрузка изображений завершена.")
