# Whenisdryday

## Description
whenisdryday.in is an email/sms subscription based web service to inform users 
about dry days (Sale of alcohol is prohibited) in India.
And there are a lot of such days.
Copyright (C) 2013  Anirudh singh shekhawat shekhawat.anirudh@gmail.com

## Contributors
will come later.

## Set Up
### Linux
1. Install Python. And also [Python Pip](https://pip.pypa.io/en/latest/installing.html) 
	* On Ubuntu `sudo apt-get install python` and `sudo apt-get install python-pip`
2. Install [Bottle](http://bottlepy.org). It doesnt really need anything other than python.
	* On Ubuntu for instance - `apt-get install bottle` would just do fine.
3. Install [Boto](http://boto.readthedocs.org). It makes sending email via SES very easy.
	* `pip install boto`
4. Python Packages
	*unirest
	*subprocess
5. Database [SQLITE3](https://docs.python.org/2/library/sqlite3.html#sqlite-and-python-types)
	* `sudo apt-get install sqlite3`
6. Edit last LoC of home_page.py. This file loads all web content of the site.
	* For localhost `run(host='localhost',port=8080,reloader=True)`
	* For the Internet `run(host='0.0.0.0',port=80,reloader=True)`

###### If you face any problems, just email me.

## License
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 3 of the License. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details http://www.gnu.org/licenses
