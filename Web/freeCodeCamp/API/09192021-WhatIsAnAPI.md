# Application Programming Interface

* Postman
* Graphical User Interface (GUI)
* web-based API

## API

* How it is used
* What to expect by using it
* a set of tools designed for software developement
* abstraction of the implementation
* examples (Upper case)
  * JS: toUpperCase()
  * Python: upper()
  * PHP: strtoupper()
  * C#: ToUpper()
  * Java: toUpperCase()
  * Ruby: upcase
* File system

```Python
import os
current_dir = os.getcwd()
for entry in os.listdir(current_dir):
    print(entry)
```

## Remote APIs

* limited space on local devices
* computational power
  * the cloud

### REST (Representational State Transfer)

* style
* a description of the design principles that underpin HTTP and the WWW

#### [Guiding principles](https://restfulapi.net/)

* client-server
  * separates the user interface from data storage
* stateless
  * each request from client to server must contain all of the information necessary to understand the request
  * cannot take advantage of any stored context on the server
  * **session state is kept entirely on the client**
* cacheable
  * requires that the data within a response to a request be implicitly or explicitly labeled as cacheable or non-cacheable
* uniform interface
  * multiple architectural constraints are needed to guide the behavior of components
    * **4 interface constraints**
      * identification of resources
      * manipulation of resources through representations
      * self-descriptive messages
      * hypermedia as the engine of application state
* layered system
  * each layer cannot see beyond the immediate layer with which they are interacting
* code on demand (optional)

#### REST Resource

* any information
* resource identifier
* resource representation: the state of the resource at any particular timestamp
  * data format of a representation: media type

#### Resource Methods

* not just GET/PUT/POST/DELETE

#### The four elements of an HTTP API

* A limited number of fixed, well-known URLs
* The information model of each of its resources
* Some indication of the supported subset of HTTP
* some sort of query syntax that enables efficient access to resource data without fetching whole resources one at a time

### Remote Procedure Calls (RPC)

* an application that is implemented as multiple distributed components
* the API of a service that is used by multiple applications
* the data that is passed between the client and the server is usually encoded in binary formats
  * the RPC style encourages relatively small messages

#### Software is hard to change

* assumptions in the code are broadly distributed and hence difficult to change

#### Integration is a major opportunity and problem

* integrating and augmenting existing systems

## How the Web works

* URL (Universal resource locator)
  * superset term: URI (Universal resource identifier)
* HTTP (HyperText Transfer Protocol)
  * request-response
  * response: HTML (HyperText Markup Language)
  * stateless
    * the client has to send the state along with the request
  * GET: get data from the server
  * POST
    * a form for submitting/posting data to the server
  * query
  * HTTP header fields
  * caches

### RESTful API

* Your program (the client) sends request to the server (using some sort of library)
  * HTTP request: stateless
    * send the state with the request (using headers)
* CRUD: operations on the resources (intention of the request)
  * creating: POST
  * reading: GET
  * updating: PUT
  * deleting: DELETE
* respond body
  * JSON (JavaScript Object Notation)
