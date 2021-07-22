
 <p align="center">
 <img src="./Resources/Images/kickstarter_indiegogo.jpeg" alt="Girl in a jacket" width="500" height="300"> 
</p>

<p>&nbsp;</p>

# **Crowdfunding Analysis**
This project attempts to help project creators understand how to market their project on Kickstarter vs Indiegogo. The purpose of this tool is to not only give them  advice on platforms but be able to efficiently market their project and provide supporting data for whichever is the better platform.

---
## **Technologies**
This project leverages python 3.7.9 with the following packages:

* [csv](https://docs.python.org/3/library/csv.html) - This was used to be able to read and write csv files easier and that each csv data are separated by a comma.

* [fire](https://github.com/google/python-fire) - *version 0.4.0* - This allows us to execute any fuction defined in a python file, using the terminal/ Command Line Interface so that you can call the function while on the terminal.

* [Jupyter Lab](https://jupyterlab.readthedocs.io/en/stable/) - *version 2.2.6* - Used to create and share documents that contain live code, equations, visualizations and narrative text.

* [Mapbox API](https://www.mapbox.com/) -  This is used to get API data for this project's data visualization. To have access to Mapbox's API key the user needs to register for an account and save their own keys.

* [matplotlib](https://matplotlib.org/) - For the visualization of crowdfunding data.

* [numpy](https://numpy.org/install/) - This provides the ability to work with arrays and use different mathematical calculations on arrays.

* [pandas](https://pandas.pydata.org/docs/) - For the analysis of crowdfunding data.

* [pathlib](https://docs.python.org/3/library/pathlib.html) - *version 1.0.1* - This was used to locate through the directory or file path. Also, it converts a string and converts that supplied string as a PosixPath that can be utilize by other functions such as reading or writing files to csv files.

* [Plotnine](https://plotnine.readthedocs.io/en/stable/installation.html) - This is a data visualisation package for Python based on the grammar of graphics.

* [pytest](https://docs.pytest.org/en/stable/) - *version 6.2.3* - This was used as a testing tool to allow us to test our user defined functions following the unit testing process of arrange, act and assert. Unit test allows us to make our functionality more robust.

* [python-dotenv library](https://pypi.org/project/python-dotenv/) - *version 0.17.1* - This enables the user to read key-value pairs from an .env file and set them as an environment variables.

* [PyVizlot](https://pyviz.org/) -  Python visualization package that provides a single platform for accessing multiple visualization libraries. Two of the libraries are:

  * [hvplot.pandas](https://hvplot.holoviz.org/user_guide/Introduction.html) - *version 0.7.2* - For the interactive visualization of the crowdfunding data.

  * [plotly.express](https://plotly.com/python/plotly-express/) - *version 4.13.0* - For the visualization of crowdfunding data.

* [questionary](https://github.com/tmbo/questionary) - *version 1.9.0* - For interactive user prompts and dialogs. This was used to create interactive question inputs/options in the terminal for users to answer.

* [Seaborn](https://seaborn.pydata.org/installing.html) - This was used to create statistical grahps.

* [Sqlalchemy ](https://anaconda.org/anaconda/sqlalchemy) - *version 1.3.20* - This is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.

* [Streamlit](https://docs.streamlit.io/en/stable/troubleshooting/clean-install.html#install-streamlit-on-macos-linux) - *version 0.84.2* - This will allow us to view our Crowdfunding Analysis on the web browser.

* [sys Module](https://docs.python.org/3/library/sys.html) - This was used specifically for its sys.exit()funciton which was used to exit the program back to its command prompt. The sys module provides functions and variables used to manipulate different parts of the Python runtime environment. You will learn some of the important features of this module here.

* [Voilà](https://github.com/voila-dashboards/voila) - This will allow us to view our Crowdfunding Analysis on the web browser.

* [Wordcloud](https://pypi.org/project/wordcloud/) - This will allow us to create a wordcloud data visualization technique that is used for representing text data. 

---

## **Installation Guide**
1. On the terminal, under the conda dev environment, install the following packages and dependencies before running the crowdfunding analysis tool:

  ```
    pip install pandas
    pip install plotly
    pip install hvplot
    pip install jupyterlab
    pip install streamlit
    pip install seaborn
    pip install fire
    pip install questionary
    pip install pytest
    pip install python-dotenv
    conda install -c pyviz hvplot
    conda list nodejs
    conda list sqlalchemy
    conda install -c conda-forge plotnine
    conda install -c conda-forge wordcloud
 
  ```

2. To show your crowdfunding analysis tool on your web browser, use `voila` command on the conda dev terminal and while on the correct directory of your crowdfunding analysis application:

    ```voila crowdfunding_analyzer.ipynb```
    * This will pop up on your web browser.

3. To show your file on youryour web browser, use `streamlit run` command on the conda dev terminal and while on the correct directory of your crowdfunding analysis application:
  ```streamlit run [filename.py]```

---

## **Examples**

Sample plots for Kickstarter and Indiegogo.

![Plot Kickstater and Indiegogo](./Resources/Images/plot_ks_indiegogo.gif)

---

## **Usages**
1. Click the crowdfunding_questionary.py and type in the category of your project. So that you can check which platform would work for you better.

    ![Questionary](./Resources/Images/questionary_small.gif)

2. We use the crowdfunding_analyzer.ipynb to get the comparison on Kickstarter versus Indiegogo. It will show data visualization of each main category.

    ![Plot Kickstater and Indiegogo Countries](./Resources/Images/ks_indiegogo_country.gif)


---


## **Contributors**

### UW FinTech Bootcamp

#### Colin Benjamin [![Linkedin](https://i.stack.imgur.com/gVE0j.png)](https://www.linkedin.com/in/colinbenjamin/) &nbsp;&nbsp;&nbsp;| &nbsp;&nbsp;&nbsp; Justine Cho [![Linkedin](https://i.stack.imgur.com/gVE0j.png)](https://www.linkedin.com/in/justinecho) &nbsp;&nbsp;&nbsp;| &nbsp;&nbsp;&nbsp; Christopher Henderson [![Linkedin](https://i.stack.imgur.com/gVE0j.png)](https://www.linkedin.com/in/chris-henderson123/) &nbsp;&nbsp;&nbsp;| &nbsp;&nbsp;&nbsp; Nathan Patterson [![Linkedin](https://i.stack.imgur.com/gVE0j.png)](https://www.linkedin.com/in/natepatterson/) 


---

## **License**

### MIT License

Copyright (c) [2021] [UW Fintech Bootcamp: Colin Benjamin | Justine Cho | Chris Henderson | Nathan Patterson]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
