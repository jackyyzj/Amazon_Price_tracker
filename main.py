from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

my_email = "yzjccy123456@gmail.com"
password = ""
port = 587

URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
response = requests.get(URL, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
									  "Accept-Language":"zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"})

soup = BeautifulSoup(response.text, "lxml")

price = soup.find(name="span",class_="a-offscreen")
float_price = float(price.getText().split("$")[1])
item_title = soup.find(name="span",id="productTitle").getText().strip()
item_link = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
buy_price = 200

if float_price < buy_price:
	with smtplib.SMTP("smtp.gmail.com", port = port) as connection:
		connection.starttls()
		connection.login(user = my_email, password = password)
		connection.sendmail(from_addr= my_email, to_addrs= my_email,
							msg = f"Subject:Amazon Price Alert!\n\n {item_title}"
								  f"is now {float_price}\n {item_link}".encode('utf-8'))


