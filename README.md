# task_signavio

These scripts are for performing the following tasks according to the documentation:
  1. Authenticates a user against the system
  2. Reads out some diagram by ID
  3. Manipulates a basic property, such as the name of a task and updates the diagram

The scripts are structured in tho following form:

* First task structure


* Second task structure  
The file_importer.py file is designed to import all files in a specific floder by providing the directory ID and directory name. 
Firstly, it obtains the access token and session ID by making a POST request using authentication.py script and the cookies and headers are set accordingly
The import_file function gets each file's name and path and makes a POST request with the defined headers, cookies, and file's information
(e.g. file name and directory ID) and prints out the content of the post request. 
Thus, using the import_file function and directory name, the corresponding file would be imported.

* Third task structure
