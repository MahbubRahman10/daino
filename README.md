# Planspiel Web Engineering Project: Research Data Management

## Introduction
This project focused on Research Data Management as part of the Planspiel Web Engineering course at TU Chemnitz. Our team, Daino, aimed to provide innovative solutions for handling the increasing volume of research publications.

## Team Formation and Collaboration
### Team Introduction: Daino
Daino was a young startup founded by three Web Engineering master's students from TU Chemnitz. Our team was diverse, with members from different backgrounds and cultures, united by a common goal of providing innovative solutions.

### Team Members
- **Dishu Bagga:** Full-stack developer with experience in startups and multinational companies.
- **Md Tajul Islam:** Backend developer with a passion for creativity and leadership.
- **Mahbub Rahman:** Software developer with a focus on long-term vision and learning.

### Team Culture
At Daino, we prioritized innovation and customer satisfaction. Our culture emphasized collaboration, positivity, and continuous improvement. We valued diversity, integrity, and timely delivery of solutions.

### Communication Tools
We utilized various tools for effective communication and collaboration, including Slack, Trello, Jira, Zoom, GitHub, Google Drive, and FileZilla.

## Business and Problem Statement
### Problem Identification
We identified a need for improved research data management solutions, which led us to focus our project on this area.

### Business Model Canvas and SWOT Analysis
We employed business model canvas and SWOT analysis to understand our business design and identify strengths, weaknesses, opportunities, and threats.

### Software Patterns
In our product development, we implemented various software patterns to ensure scalability, efficiency, and maintainability.

## Our Product - Research Data Management 
### Problem Statement
As students or researchers, it was very common practice to search online for research publications. If we looked into the number of publications per year all over the world, we could see that it increased with a very high growth rate. Let’s focus on a chart where we see the number of publications per year and the cumulative number of publications on biochar from 1998 to 2017.

### Our Proposed Solution
After a complete feasible study with that problem, team DAINO was able to create a solution that would be helpful for students, researchers, and educational institutions. We proposed a dynamic research data management dashboard where users would get all types of information related to a research publication with a high number of relevant data. Our survey indicated that every year, the number of research publications increased, and so did the users of these research papers (students or researchers). Therefore, we needed to manage this huge amount of data for a high number of users in such a way that one user could get all kinds of information related to research publication or research area or researcher in a single platform.

## Product Implementation
### Tools and Technology
We set up our environment and how we processed our tasks. Since our product was about research data management, we used different tools and software, such as library tools. So for this scraping, we tried different tools and libraries.

- **Python:** Python was the main tool for scraping data. Python is a high-level, interpreted, interactive, and object-oriented scripting language. Python is designed to be highly readable. We preferred Python because it made web scraping simple to navigate and search through parse trees. Also, Python worked well when scraping large datasets. Python automation saved valuable time and effort and could significantly increase the speed of data extraction. In Python, we wrote and executed the code only once; the scraper worked automatically and collected the data. It saved us a lot of time and energy.
- **Beautiful Soup:** BeautifulSoup was one of the popular libraries provided by Python to scrape data from the web. It generated a parse tree for parsed pages, which could then be used to extract data from HTML. The library had a couple of intuitive functions that we could use to explore the HTML data.
- **Requests:** BeautifulSoup was one of the popular libraries provided by Python to scrape data from the web. It created a parse tree for parsed pages that could be used to extract data. The library had a couple of intuitive functions that we could use to explore the HTML data.
- **lxml:** lxml was a high-performance, production-quality HTML and XML parsing library. It allowed for easy handling of XML and HTML files. Compared to the rest, Python lxml offered an advantage in terms of package functionality. Even fairly large XML files took an invisible amount of time to read and write. Using lxml made data processing easier and much faster. We used this library mostly for collecting data from social sites such as Linkedin.
- **Pandas:** Pandas stood for “Python Data Analysis Library”. Pandas was a fast, powerful, flexible, and easy-to-use data analysis and manipulation tool for python. Pandas allowed importing data from various file formats such as JSON, queries, and Microsoft Excel.

### Implementation
Our project, "Planspiel Web Engineering Project: Research Data Management," addressed the challenge of gathering comprehensive information about researchers and their publications from multiple sources. We aimed to implement effective research data management practices to provide easy access to researchers' publications and skills through a unified interface. Utilizing web scraping technology, we systematically collected data from social networking sites, TU Chemnitz professorship pages, and bibliographies, ensuring the creation of a comprehensive dataset to support our research objectives.

### Prototype
We recognized the challenge of managing large volumes of research data effectively. To address this, we implemented a prototype using an open data portal approach, aiming to organize and represent data in a structured manner. For our data management portal, we chose [CKAN](https://ckan.org/) (Comprehensive Knowledge Archive Network), a leading open-source data management system. [CKAN](https://ckan.org/) offered powerful tools for cataloging, storing, publishing, and accessing data, making it a suitable choice for our project. We set up [CKAN](https://ckan.org/) on our local environment, utilizing Ubuntu, PostgreSQL for DataStore, and Apache Solr for search functionality. We explored different methods for dataset upload, including using the [CKAN](https://ckan.org/) front-end and API. Additionally, we discussed the [CKAN](https://ckan.org/) harvester extension for advanced data imports, although it was not implemented in our project. With [CKAN](https://ckan.org/) as our foundation, we proceeded with the implementation of our product, focusing on creating a user-friendly interface and leveraging [CKAN](https://ckan.org/) features to enhance data management and visualization capabilities.

## University Information
This project was completed as part of the Planspiel Web Engineering course at Technische Universität Chemnitz. It was completed in the winter semester 2021-22.

## Supervisor Information
- **Prof. Dr. Martin Gaedke**
  - Professor, Professorship of Distributed and Self-organizing Systems, Faculty of Computer Science, Technische Universität Chemnitz

- **Valentin Siegert**
  - Researcher, Professorship of Distributed and Self-organizing Systems, Faculty of Computer Science, Technische Universität Chemnitz

- **Christoph Göpfert**
  - Researcher, Professorship of Distributed and Self-organizing Systems, Faculty of Computer Science, Technische Universität Chemnitz

## Conclusion
Our project managed research data efficiently with CKAN, promoting access to publications and knowledge dissemination. This experience underscored the value of teamwork and innovation in addressing challenges.
