# task_signavio

These scripts are for performing the following tasks according to the documentation:
  1. Authenticates a user against the system
  2. Reads out some diagram by ID
  3. Manipulates a basic property, such as the name of a task and updates the diagram

The scripts are structured in tho following form:

**1. First task structure**

* First,the file containing user-specific variables has been created: [conf.py](conf.py)
Running the [authentication.py](authentication.py) will send the login requests to Signavio Process Manager and obtains the access token and session ID, the request will be sent by post function, becuase it contains the username and password, so should not be chached or stored in browser history. This requests the headers and form the parameters of the data. The token ID (headers: content-type) will be decoded in utf-8 format and two set of cookie values for session ID and routing the requuest to the authenticator server will be retrieved in the format of JSON document.
Authentication tasks takes place via GET request, this could be done via POSTMAN platform that can execute the requests for Mock servers, here using the Signavio Process Manager Postman collection, we can test the authentication procedure and see whether it has error, the responses are in the form of the status code, e.g: 501 (Unsupported method ('POST')) or 200(Authentication successful)

* After authentication, the tokens can be passed to the client. This can be done via the file [authentication_handover.py](authentication_handover.py). This request is again done by POST which requests headers(Content-type, X-Signavio-ID, and Cookie) and responses to the client by status codes.
* By accessing the server's root URL in browser, the server authenticates client for Signavio Process Manager and opens the Explorer application. 

**2. Second task structure**

The [file_importer.py](file_importer.py) file is designed to import all files in a specific floder by providing the directory ID and directory name.  
* Firstly, it obtains the access token and session ID by making a POST request using [authentication.py](authentication.py) script and the cookies and headers are set accordingly.
* The import_file function gets each file's name and path and makes a POST request with the defined headers, cookies, and file's information
(e.g. file name and directory ID) and prints out the content of the post request. 
* Thus, using the import_file function and directory name, the corresponding file would be imported.

**3. Third task structure**


