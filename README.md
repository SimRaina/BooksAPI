# Flask_APIs
Created APIs using Flask

Prerequisite: a) Download and install Python 3. 
              b) Set Environment variables in your local system.
              c) pip install Flask.
1. Download this GitHub repo on your local system.
2. Go to the folder where app.py file is available. 
3. Open CMD and run command "python app.py" to start the API server.
In this code repo you will also find collection and environment json files.
4. Open Postman and import collection.json file. 
5. Go to Manage Environment and import environment.json.
5. Run this collection on postman as per the SimRaina QA YouTube video.


To run collection from the commandline:
1. Download and install Node. 
2. Verify node and npm are installed.
3. Run command to install newman -> "npm install -g newman"
4. Go to the folder where collection.json and environment.json files are available.
5. Run command on the commandline -> newman run <collectionanme>.json -e <environment>.json
