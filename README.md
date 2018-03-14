To serve, execute the following in a suitable shell (replacing all words within ' ').

$ python3 -m venv 'site name'

$ cd 'site name'

$ source ./bin/activate

$ git clone 'this url'

$ cd ucsb-hep-lab

$ pip3 install --upgrade pip

$ pip3 install -r requirements.txt

$ python3 manage.py makemigrations

$ python3 manage.py migrate

$ python3 manage.py runserver 8080

Then navigate to localhost:8080 in a web browser.

Don't forget to activate the virtual environment whenever using the inerpreter.
