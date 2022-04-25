# task_signavio

These scripts are for performing the following tasks according to the documentation:
  1. Authenticates a user against the system
  2. Reads out some diagram by ID
  3. Manipulates a basic property, such as the name of a task and updates the diagram

The scripts are structured in tho following form:

**1. First task structure**
First,the file containing user-specific variables has been created: conf.py
Running the authentication.py will send the login requests to Signavio Process Manager and obtains the access token and session ID, the request will be sent by post function, becuase it contains the username and password, so should not be chached or stored in browser history. The token ID will be decoded in utf-8 format and two set of cookie values for session ID and routing the requuest will be retrieved in the format of JSON document.
Authentication tasks takes place 

**2. Second task structure** 
The [file_importer.py](file_importer.py) file is designed to import all files in a specific floder by providing the directory ID and directory name.  
* Firstly, it obtains the access token and session ID by making a POST request using [authentication.py](authentication.py) script and the cookies and headers are set accordingly.
* The import_file function gets each file's name and path and makes a POST request with the defined headers, cookies, and file's information
(e.g. file name and directory ID) and prints out the content of the post request. 
* Thus, using the import_file function and directory name, the corresponding file would be imported.

**3. Third task structure**
