|Title | Host Pathogen Interaction|
| ------ | ------ |
|Repository-name| [GitHub](https://github.com/cepdnaclk/e17-co328-Host-Pathogen-Interaction)|
|Project page| [BioWeb](https://cepdnaclk.github.io/e17-co328-Host-Pathogen-Interaction/)|
|Frontend| [BioWeb](https://bio2web.herokuapp.com/)|

[comment]: # "This is the standard layout for the project, but you can clean this and use your own template"

#  Inference of host-microbe associations based on metagenomic data

## overview
Finding the diesecs is very challenginig matter. There are many methods available in the filed but the problem these methods are not flow the same procedure. So that we like to develop the software that help to identify the problem using the microbiome samples. The software worked based on the machine learning techniques. It can give more suitable discussion for the user.
## problem
When considering the problems in this field we found some of the major things.
-imited to testing for differential abundance of microbial taxa between group of sample
-They do not allow users to evaluate their predictivity.
-the software resulting from these studies is generally not easily modified or transferred to other classification tasks or data types
-Some tools have identified these many issues
-Specific programming language based
-its give poor user experience
## solutions
we are suggesting a web application integrated with a machine learning framework and statistical methods.it can help user they can analyze their microbiome data without any machine learning knowledge because our software proving the GUI for doing such things
## Team
-  E/17/292, Rilwan M,  [e17292@eng.pdn.ac.lk](mailto:e17292@eng.pdn.ac.lk)
-  E/17/256, Piriyaraj S, [e17256@eng.pdn.ac.lk](mailto:e17256@eng.pdn.ac.lk)
-  E/17/352, Thanujan T, [e17352@eng.pdn.ac.lk](mailto:e17352@eng.pdn.ac.lk)
-  E/17/358, Varnaraj N, [e17358@eng.pdn.ac.lk](mailto:e17358@eng.pdn.ac.lk)



## Links
<!-- - [Project Page](https://cepdnaclk.github.io/e17-3yp) -->
- [Project Repository](https://github.com/cepdnaclk/e17-co328-Host-Pathogen-Interaction)
- [Project Page](https://cepdnaclk.github.io/e17-co328-Host-Pathogen-Interaction/)
- [Department of Computer Engineering](http://www.ce.pdn.ac.lk/)
- [University of Peradeniya](https://eng.pdn.ac.lk/)


## How to run.
- step 01- clone repo
```
git clone https://github.com/cepdnaclk/e17-co328-Host-Pathogen-Interaction.git
```
- step 02 - activate virtual environment<br/>
    run active file in the software/frontend/script<br/>
    A. On Windows(open CMD on script folder)
    ```
    activate.bat
    ```
    B. On linux(open terminal on script folder)
    ```
    source activate
    ```
- step 03 - install modules
    <br/>move to folder Fronted in terminal
    ```
    pip install -r requirements.txt
    ```
- step 04 - database migrations
    move to folder Host_Pathogen_Interaction
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
- step 05 - run server
    ```
    python manage.py runserver
Thank you
    ```
[//]: # (Please refer this to learn more about Markdown syntax)
[//]: # (https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
