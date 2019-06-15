# New Theatre Festival Reports

Django-based web app for collecting and displaying data on shows in a theatre festival. 

## In-festival information

- Requirements for the show changeovers
- Information for Front of House staff, linking to an external ticket sales platform 

## After-festival information

- Collect reports on show timings
- Collect reports on audience behaviours
- Collect reports on finance 

# Running locally  

You will need: 
* Django 2.2
* Python 3.6.7 (and Pip) 
* ǸPM (for Bootstrap 4 and SASS)

## Installation 
### Python Virtualenv 
Using your preferred mechanism, create a virtual Python environment. 

```
virtualenv <dir>
``` 

Where `<dir>` is a given directory; such as `venv`
Ensure the Python version is 3.6 (if it is not the default) by running `virtualenv <dir> --python=python3` or similar. 
#### Activate the virtualenv 

```
**Windows**
<virtualenv_dir>/Scripts/activate.bat

**Unix**
source <virtualenv_dir>/bin/activate
``` 
At this point you can check the Python version by running `python --version`. 
#### Install the requirements 

```
cd <dir>
pip install -r requirements.txt 
```
Ubuntu-based users may also need to run `sudo apt install libpq-dev python3-dev`
#### Run the server 
```
python manage.py runserver 
``` 
Pages can be browsed locally at http://localhost:8000/

### Sass
Install npm with
```
npm install
```
And then use either 
```
npm run css_compile
```
to compile, or
```
npm run css_watch
```
to recompile after every save of a Sass file.