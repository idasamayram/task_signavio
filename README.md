# task_signavio

These scripts are for performing the following tasks according to the documentation:
  1. Authenticates a user against the system
  2. Reads out some diagram by ID
  3. Manipulates a basic property, such as the name of a task and updates the diagram

The scripts are structured in tho following form:

**1. First task structure**

* First,the file containing user-specific variables has been created: [conf.py](conf.py)
* Running the [authentication.py](authentication.py) will send the login requests to Signavio Process Manager and obtains the access token and session ID, the request will be sent by post function, becuase it contains the username and password, so should not be chached or stored in browser history. This requests the headers and form the parameters of the data. The token ID (headers: content-type) will be decoded in utf-8 format and two set of cookie values for session ID and routing the requuest to the authenticator server will be retrieved in the format of JSON document.
Authentication tasks takes place via GET request, this could be done via POSTMAN platform that can execute the requests for Mock servers, here using the Signavio Process Manager Postman collection, we can test the authentication procedure and see whether it has error, the responses are in the form of the status code, e.g: 501 (Unsupported method ('POST')) or 200(Authentication successful)

* After authentication, the tokens can be passed to the client. This can be done via the file [authentication_handover.py](authentication_handover.py). This request is again done by POST which requests headers(Content-type, X-Signavio-ID, and Cookie) and responses to the client by status codes.
* By accessing the server's root URL in browser, the server authenticates client for Signavio Process Manager and opens the Explorer application. 

**2. Second task structure**

* Here using the GET/p/model request, the meta data(info,views,status,parents,subscription,priv) of a diagram cab be read, adding subendpoint to the request can retrieve specific data such as glossaryinfo or subscription of a diagram.

* [data_retriever.py ](data_retriever.py ) uses the GET/p/model/(id)/revisions requests to retrieve a diagram’s list of revisions, together with each diagram revision’s metadata. it requests the Parameters(diagram id) and Request Headers(X-Signavio-ID,Accept, and Cookie) and responses as a JSON array containing the IDs and meta information of all revisions of the corresponding diagram(status code, and response headers). Using the format JSON, the output will be printed as a json object.

**3. Third task structure**

* Using PUT/p/model/(id) request, updates the called diagram, by creating a new diagram revision. Like p/model, this requests the id and request headers(X-Signavio-ID,Accept, Cookie plus content-type), but also Form Parameters(name, parent, comment, json_xml, and svg_xml), then responses as a JSON array with the items related to this model, containing status code and response header(content-type)

* [update_diagram.py ](update_diagram.py) updates the diagram by changing its name, parent and adding a new diagram revision with comment. Given the user variable for the changes need to be made, sets the credentials via authenticate function, then reads the JSON representation of new revision and updates the data according to the user variables, and prints out the result.
