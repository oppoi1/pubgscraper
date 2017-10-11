#python3
""" 
A pubg inventational web scraper, that checks if you invite button is still 'Opening Soon'.
If the button changes it will send an E-Mail to your adressee.
"""

import requests, bs4, time, smtplib

#always true -> checks all the time, will use timesleep later
while True:
    url = "http://en.intelextrememasters.com/season-12/oakland/pubg/"
    #imitate a browser
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    # download the homepage
    res = requests.get(url)
    #downloads the website
    page = bs4.BeautifulSoup(res.text)

    elems = page.select('.pubg_button')
    
    if elems[0].getText() == "SIGN UP FOR EU - OPENING SOON!":
        print("Attempting...")
        time.sleep(20) #wait 20seconds
        continue #continue after 20seconds
    else:
        msg = 'Check the Tournament http://en.intelextrememasters.com/season-12/oakland/pubg/'
        from_email = 'your_email'
        to_email = 'to_email'

        server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
        server.starttls()
        server.login("your_email", "your_pw")

        print("From: " + from_email)
        print("To: " + str(to_email))
        print("Message: " + msg)

        server.sendmail(from_email, to_email, msg)
        server.quit

        break
