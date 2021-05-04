from requests_html import HTMLSession
from selenium import webdriver
import os
import time
import csv
import re


# options = webdriver.ChromeOptions()
# options.add_argument(
#     'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
#     (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36')
# options.add_argument('accept=accept: ')
# options.add_argument('--disable-blink-features=AutomationControlled')
# # options.add_argument("user-data-dir=chrome_data\\")
# # options.add_argument(r"user-data-dir=C:\Users\Workspace\AppData\Local\Google\Chrome\User Data")
# # options.add_argument("--profile-directory=Default")
# # options.add_argument("--disable-extensions")
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')

# driver = webdriver.Chrome(
#     executable_path=os.path.join('chromedriver', 'chromedriver.exe'),
#     options=options
# )


# # Сохраняем ссылки на список деталей
# def save_list_links(list_links):
# 	with open('list_links.csv', 'a', encoding='utf-8', newline='') as links_csv:
# 		for line in list_links:
# 			array = line.split(',')
# 			writer = csv.writer(links_csv)
# 			writer.writerow(list(array))

# # Получаем ссылки на список деталей
# list_links = []
# URL = 'https://luftmaster.lt/'
# session = HTMLSession()
# r = session.get(URL)
# print(r.status_code)
# for q in range(1,50):
# 	try:
# 		j = r.html.xpath(f'//*[@id="woocommerce_product_categories-2"]/ul/li[{q}]/ul', first=True)
# 		if j is None:
# 			link = r.html.xpath(f'//*[@id="woocommerce_product_categories-2"]/ul/li[{q}]/a/@href', first=True)
# 			if link is not None:
# 				list_links.append(link)

# 		else:
# 			for a in range(1,21):
# 				w = r.html.xpath(f'//*[@id="woocommerce_product_categories-2"]/ul/li[{q}]/ul/li[{a}]/ul', first=True)
# 				if w is None:
# 					try:
# 						link = r.html.xpath(f'//*[@id="woocommerce_product_categories-2"]/ul/li[{q}]/ul/li[{a}]/a/@href', first=True)
# 						if link is not None:
# 							list_links.append(link)

# 					except:
# 						link = r.html.xpath(f'//*[@id="woocommerce_product_categories-2"]/ul/li[{q}]/ul/li/a/@href', first=True)
# 						if link is not None:
# 							list_links.append(link)

# 				else:
# 					for t in range(1,21):
# 						try:
# 							link = r.html.xpath(f'//*[@id="woocommerce_product_categories-2"]/ul/li[{q}]/ul/li[{a}]/ul/li[{t}]/a/@href', first=True)
# 							if link is not None:
# 								list_links.append(link)

# 						except:
# 							link = r.html.xpath(f'//*[@id="woocommerce_product_categories-2"]/ul/li[{q}]/ul/li[{a}]/ul/li/a/@href', first=True)
# 							if link is not None:
# 								list_links.append(link)

# 	except Exception as e:
# 				print(e)

# save_list_links(list_links)


# def read_links_list_from_file():  # Open file with company links (not necessary)
#     try:
#         with open('list_links.csv', 'r', newline='') as csv_read:
#             reader = csv.reader(csv_read)
#             company_links = []
#             for row in reader:
#                 company_links.append(row)
#             return company_links
#     except Exception as e:
#         print(e)
#         print("Can't read the file 'links_list.csv'")


# links_list_read = read_links_list_from_file()

# def save_links(list_links):
#   with open('links.csv', 'a', encoding='utf-8', newline='') as links_csv:
#       for line in list_links:
#           array = line.split(',')
#           writer = csv.writer(links_csv)
#           writer.writerow(list(array))

# product_links = []
# try:
#     for i in range(92):
#         listt = links_list_read[i][0]
#         driver.get(listt)
#         for x in range(1,20):
#             try:
#                 product_link = driver.find_element_by_xpath(f'/html/body/div[4]/div[4]/div[2]/div/div/div[4]/div[{x}]/div[2]/div[1]/h3/a').get_attribute('href')
#                 product_links.append(product_link)
#             except Exception as e:
#                 pass
# except Exception as e:
#     print(e)
# finally:
#     driver.close()
#     driver.quit()

# save_links(product_links)



def read_links_from_file():  # Open file with company links (not necessary)
	try:
		with open('links.csv', 'r', newline='') as csv_read:
			reader = csv.reader(csv_read)
			company_links = []
			for row in reader:
				company_links.append(row)
			return company_links
	except Exception as e:
		print(e)
		print("Can't read the file 'links_list.csv'")



def save_result(row):
    with open('result.csv', 'a', encoding='utf-8', newline='') as links_csv:
        writer = csv.writer(links_csv, delimiter=';')
        writer.writerow(row)





links = read_links_from_file()
for q in range(26):
	session = HTMLSession()
	r = session.get(links[q][0])
	print(r.status_code)
	print(links[q][0])
	try:
		product_title = r.html.find('h1.product_title', first=True).text
	except:
		product_title = ' '
	try:
		price = r.html.find('p.price', first=True).text
	except:
		price = ' '
	try:
		short_description = r.html.find('div.woocommerce-product-details__short-description')[0].text
	except:
		short_description = ' '
	try:
		categories = r.html.find('span.posted_in', first=True).text
		categories = categories.split(':')[1].strip()
	except:
		categories = ' '
	try:
		tags = r.html.find('span.tagged_as', first=True).text
		tags = tags.split(':')[1].strip()
	except:
		tags = ' '
	try:
		description = r.html.find('#tab-description > table > tbody', first=True).text.split('\n')
		if 'Pagaminta:' in description:
			country_made = description[3].strip()
		else:
			country_made = ' '
		if 'Kodas:' in description:
			code = description[5].strip()
		else:
			code = ' '
		if 'Metai:' in description:
			year = description[7].strip()
		else:
			year = ' '
		if 'Originalus prekės OEM kodas:' in description:
			oem_code = description[9].strip()
		else:
			oem_code = ' '
		alt_description = ' '
	except:
		alt_description = r.html.find('div.woocommerce-Tabs-panel')[0].text
	try:
		delivery = r.html.find('div.woocommerce-Tabs-panel')[1].text
		delivery = delivery.split('\n', 1)[1].strip()
	except Exception as e:
		delivery = ' '
	short_description = short_description.split('\n')
	if 'PREKĖ YRA SANDĖLYJE' in short_description:
		in_stock = 'IN STOCK'
	else:
		in_stock = 'OUT OF STOCK'
	if 'Gamintojas' in short_description[0].split(':'):
		made_in = short_description[0].split(':')[1].strip()
	else:
		made_in = ' '
	try:
		if 'Garantija' in short_description[1].split(':'):
			varranty = short_description[1].split(':')[1].strip()
		else:
			varranty = ' '
	except:
		varranty = ' '
	save_result([product_title,price,categories,tags,country_made,code,year,oem_code,alt_description,delivery,in_stock,made_in,varranty])

