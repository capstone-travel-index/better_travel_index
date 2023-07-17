# Better Travel Guide
https://github.com/capstone-travel-index/better_travel_index/files/12067891/Untitled.presentation.pdf



## Overview
The Better Travel Guide is a user-friendly tool built on Tableau dashboards, utilizing several .csv tables as data sources (previously sourced from a SQL database). The accompanying notebooks handle data cleaning, structuring, and analysis to prepare the data for visualization in Tableau. In addition to data normalization and analysis, the notebooks also incorporate comprehensive data analysis procedures.
<br/><br/>
Users can input their desired "percentage of their yearly footprint budget allocated to the trip," "daily spending at the destination," and select cities for comparison against the recommendation table. The tool generates three columns of information: the carbon footprint associated with traveling to the chosen destination using the selected mode of transportation, estimated daily costs, and the Responsibility Index. The Responsibility Index is a key performance indicator that encompasses environmental, social, and governance indicators of the destination, as well as the aforementioned carbon footprint.
<br/><br/>
Additionally, the tool features a map highlighting the countries containing cities listed in the recommendation table. Users can seamlessly switch between dashboards dedicated to plane, car, and train travel options, with each dashboard providing specific Responsibility Index scores and carbon footprint values for every city.
<br/><br/>
The Better Travel Guide is the culmination of a 4-member team's 4-week effort as their capstone project.



## Data Sources
In this project we utilized multiple data source:

ESG DATA
<br/>
[The World Bank - ESG Data](https://esgdata.worldbank.org/data/download?lang=en)
<br/>
[University of Gothenburg - Environmental Indicators Dataset](https://www.gu.se/en/quality-government/qog-data/data-downloads/environmental-indicators-dataset)

LGBTQIA+ RIGHTS DATA
<br/>
[Spartacus - Gay Travel Index](https://data.world/makeovermonday/2023w2/workspace/file?filename=GTI_2012-2021.xlsx)

TRAVEL DATA
<br/>
[DESTATIS - Statistik über die touristische Nachfrage](https://www-genesis.destatis.de/genesis/online?sequenz=statistikTabellen&selectionname=45413#abreadcrumb)
<br/>
[UNWTO - Key Tourism Statistics](https://www.unwto.org/tourism-statistics/key-tourism-statistics)

CO2 TRAVEL FOOTPRINT
<br/>
[Mein Klimaschutz - CO2 durch Verkehrsmittel im Vergleich](https://www.mein-klimaschutz.de/unterwegs/a/einkauf/welches-verkehrsmittel-verursacht-im-vergleich-mehr-co2/)

CITIES LIVING COSTS DATA
<br/>
[Numbeo - API](https://www.numbeo.com/common/api.jsp)

APARTMENTS COSTS DATA
<br/>
[Inside Airbnb](http://insideairbnb.com/get-the-data/)
<br/>
[Currency Converter by API-Ninjas](https://rapidapi.com/apininjas/api/currency-converter-by-api-ninjas)



## Technologies
This project was created with:
</br>
- Project Management & Version Controll:
    - Git 2.39.2
    - Github 3.8.5
<br><br>
- Analytics and algorithm coding:
    - VS Code 1.77.3
    - Python 3.9.16
    - Numpy 1.23.5
    - Pandas 1.5.0
    - Seaborn 0.12.2
    - Matplotlib 3.7.1
<br><br>
- Data Base Management:
    - DBeaver 23.0.4
    - PostgreSQL 15.2
<br></br>
- Visualisation:
    - Google Slides
    - Tableau 2023.2.0
