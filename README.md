# Droggo
Meet Droggo, a pet-bot that manages your remote repositories

![alt text](https://vignette.wikia.nocookie.net/howtotrainyourdragon/images/1/11/ToothlessHttyd2Remder.png/revision/latest?cb=20180407215412)

#### What can Droggo do?
Currently, Droggo can</br>

* do a find and replace text edit on a selected common file, and then make a pull request with the changes
  * for every repo you own on github
  * for every repo in an organisation
  
WIP features</br>
* Github Enterprise support

Planned features</br>
* Add file
* Remove file
* Direct push to default branch

#### Droggo use cases
Droggo makes a great pet for Jenkins, to orchastrate common changes across repos to the JENKINSFILE so you don't have to. 

For example, you want to edit the version number of a Jenkins library for all repositories you own.

`Library(My-Lib@v0.1)` &rarr; `Library(My-Lib@v0.2)`

You tell droggo to do it for you
```
py droggo.py --fetch JENKINSFILE --find Library(My-Lib@v0.1) --rep Library(My-Lib@v0.2) -u githubUsername:githubPassword
```

To do it for an organisation you have write access to
```
py droggo.py --fetch JENKINSFILE --from deBestOrg --find Library(My-Lib@v0.1) --rep Library(My-Lib@v0.2) -u githubUsername:githubPassword
```

Order of parameters dont matter.

## Get Droggo
Clone this repo or download as Zip. Releases coming soon, work in production.

### Installation

```
cd path/to/droggo
pip install -r requirements.txt
```
