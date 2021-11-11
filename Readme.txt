Scrapy tutos
------------
https://towardsdatascience.com/a-minimalist-end-to-end-scrapy-tutorial-part-i-11e350bcdec0
https://www.jitsejan.com/scraping-with-scrapy-and-postgres


Keyring
-------
==> To set/read secrets from command line:
python -m keyring set system username (promt to enter the secret)
python -m keyring get system username (Show the secret in terminal)


==> To set/read secrets from pyton script 
keyring.set_password("system", "username", "password")
keyring.get_password("system", "username")