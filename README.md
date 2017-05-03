# Web-Scraping-by-Python
Develop the python script to scrape data from the website and load into the MySQL database.

Hello World! This is my first python project.
The program is to scrape the restaurant information from https://offpeak.my/ and insert into MySQL database.
And I use the Windows Task Scheduler to set time to run this python script to scrape the data from the website.
Note: Actually I tried to use the python apscheduler library to create the scheduler before but it didn't work. Anyway I will try later.

Anyway, I'm welcome to share my source code to the public. Any feedback or suggestion, please let me know.
Finally, I wrote this program for the education purpose only. I don't have intention to scrape the data from this website to any commercial benefit.

Note: Due to this program is to connect to the MySQL Database. So you have to install the mySQL database on you computer first. Then you need to create the database and table as following script so that you can run the python script.

CREATE TABLE `restaurant` (
  `restaurant_id` int(11) NOT NULL AUTO_INCREMENT,
  `restaurant_name` varchar(150) DEFAULT NULL,
  `restaurant_location` varchar(150) DEFAULT NULL,
  `bookings` varchar(100) DEFAULT NULL,
  `scrape_date` datetime DEFAULT NULL,
  PRIMARY KEY (`restaurant_id`)
) ENGINE=InnoDB AUTO_INCREMENT=115 DEFAULT CHARSET=latin1;

