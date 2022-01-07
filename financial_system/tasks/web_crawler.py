import logging
import requests

from financial_system.utils.conversor import convert_real_to_dolar

from bs4 import BeautifulSoup
from pyramid_celery import celery_app as app



logger = logging.getLogger()


@app.task(bind=True, name="uol_data", queue="web_crawler")
def google_crawler(self):
    
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
    
    # Url to get dollar from Google Search
    google_URL = "https://www.google.com/search?q=dollar+exchange+rate&sxsrf=AOaemvKKXeyL7wqkrf-_B4OHaw7fX7NE8g%3A1641351708557&source=hp&ei=HArVYYDsH5DL1sQPr_ygmAM&iflsig=ALs-wAMAAAAAYdUYLGJeb5F_A4lbupiPodtH2Yb09gxO&ved=0ahUKEwiA6qbMz5n1AhWQpZUCHS8-CDMQ4dUDCAc&uact=5&oq=dollar+exchange+rate&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgUIABDLATIFCAAQywEyBQgAEMsBMgUIABDLATIFCAAQywEyBQgAEMsBMgUIABDLATIFCAAQywEyBQgAEMsBUABYAGCFBmgAcAB4AIABtgGIAbYBkgEDMC4xmAEAoAECoAEB&sclient=gws-wiz"
    page = requests.get(google_URL, headers=headers)
    
    # Parse the page content
    soup = BeautifulSoup(page.content, "html.parser")
    
    # Find the tag and class name that contains info about dollar value
    span = soup.find("span", class_="DFlfde SwHCTb")

    dollar_value = convert_real_to_dolar(span.text)
    
    # Endpoint to save data on my database
    endpoint_URL = "http://localhost:6543/api/v1/dolars"
    
    response = requests.post(endpoint_URL, json={"price": float(dollar_value)})
    
    if response.status_code == 201:
        logger.info("Dollar value saved")
        return
    else:
        logger.error("Can't save dollar value")
        return
