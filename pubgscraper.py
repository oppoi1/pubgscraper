#python3
""" 
A pubg inventational web scraper, that checks if you invite button is still 'Opening Soon'.
If the button changes, it will send an E-Mail to your adressee.
"""

import requests, bs4, time, smtplib

#always true -> loop to check if button is still the same.
while True:
    url = "http://en.intelextrememasters.com/season-12/oakland/pubg/"
    #imitate a browser
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    # download the homepage
    request_url = requests.get(url)
    #downloads the website
    request_page = bs4.BeautifulSoup(request_url.text)

    elems = request_page.select('.pubg_button')
    
    if elems[0].getText() == "SIGN UP FOR EU - OPENING SOON!":
        print("Attempting...")
        time.sleep(20) #wait 20seconds
        continue #continue after 20seconds
    else:
        msg = 'Check the Tournament http://en.intelextrememasters.com/season-12/oakland/pubg/'
        from_email = 'your_email'
        to_email = 'to_email'

        #server settings to send your email.
        server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
        server.starttls()
        server.login("your_email", "your_pw")

        print("From: " + from_email)
        print("To: " + str(to_email))
        print("Message: " + msg)

        server.sendmail(from_email, to_email, msg)
        server.quit

        break
