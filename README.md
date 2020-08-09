# Flask_APIs
Created APIs using Flask

1. Download and install Python 3. Set Environment variables.
2. pip install Flask.
3. Go to the folder where app.py file is available. Run command "python app.py" to start the API server.
4. Open Postman and import collection.json file. Go to Manage Environment and import environment.json.
5. Run this collection. 


To run collection from the commandline:
1. Download and install Node. 
2. Verify node and npm are installed.
3. Run command to install newman -> "npm install -g newman"
4. Go to the folder where collection.json and environment.json files are available.
5. Run command on the commandline -> newman run <collectionanme>.json -e <environment>.json
