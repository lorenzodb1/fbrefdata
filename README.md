<p align="center">
  <img src="https://raw.githubusercontent.com/lorenzodb1/fbrefdata/master/docs/_static/logo.png" width="300px"/>
</p>

**FBrefData** is a scraper of football data from [FBref](https://www.fbref.com/en/). The library is forked from 
[SoccerData](https://github.com/probberechts/soccerdata) by [@probberechts](https://github.com/probberechts). 

### Why FBrefData?
While [SoccerData](https://github.com/probberechts/soccerdata) does a great job at scraping data from [FBref](https://www.fbref.com/en/), it has some limitations
that I wanted to address. These limitations are, likely, due to the fact that it was originally built to scrape and
combine data from different sources, which is why this library focuses on [FBref](https://www.fbref.com/en/) only.

Some of the changes I wanted to introduce in **FBrefData** are:
- I wanted to store the dataframes that are obtained from scraping instead of storing the HTML pages themselves, thus 
reducing the amount of disk space required to cache the data;
- I wanted to support all competitions for which [FBref](https://www.fbref.com/en/) provides advance stats data, including the ones in the 
Southern emisphere and the Major League Soccer, and not just the top five European leagues;
- I wanted to remove the leagues selected by default, thus giving the users full control of which leagues they want to
scrape.

**FBrefData** forked from version 1.4.1 of [SoccerData](https://github.com/probberechts/soccerdata) and will start its versioning from 0.1.0. The improvements 
listed above, along with other minor changes, will be officially available starting from version 1.0.0. Nonetheless,
I will still merge improvements made to the FBref module of SoccerData for as long as it's possible.

### Installation
```bash
pip install fbrefdata
```

### Usage
```python
import fbrefdata as fd

# Create scraper class instance for the 2018-2019 Premier League
fbref = fd.FBref('ENG-Premier League', '2018-2019')

# Fetch dataframes
schedule = fbref.read_schedule()
```

### Supported leagues
As of now, **FBrefData** supports the following leagues:

- Argentina: Primera División
- Belgium: Pro League
- Brazil: Série A
- England: Premier League, EFL Championship
- France: Ligue 1, Ligue 2
- Germany: Fußball-Bundesliga, 2. Fußball-Bundesliga
- Italy: Serie A, Serie B
- Mexico: Liga MX
- Netherlands: Eredivisie
- Portugal: Primeira Liga
- Spain: La Liga, Segunda División
- United States/Canada: Major League Soccer
- UEFA: Champions League, Europa League, Europa Conference League
- CONMEBOL: Copa Libertadores

If [FBref](https://www.fbref.com/en/) started providing advanced stats for leagues that aren't supported yet, please open an issue.

---
**Disclaimer:** As this library relies on web scraping, any changes to the scraped websites will break the package. Hence,
do not expect that all code will work all the time. If you spot any bugs, then please
[fork it and start a pull request](https://github.com/lorenzodb1/fbrefdata/blob/master/CONTRIBUTING.rst).
