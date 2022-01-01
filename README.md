how to organize a python project
how build a database cache layer (ttl, eviction policy)
backend security (encyption & ssl termination, rate limiting / dos attack, etc...)
logging service
how to write unit tests in python

dataclass

server concepts
https://realpython.com/api-integration-in-python/
https://www.bogotobogo.com/python/python_http_web_services.php
https://www.afternerd.com/blog/python-http-server/

performing http requests in python
https://www.nylas.com/blog/use-python-requests-module-rest-apis/
https://www.datacamp.com/community/tutorials/making-http-requests-in-python
https://www.freecodecamp.org/news/how-to-interact-with-web-services-using-python/


-> Gateway handles incoming requests
-> Route object built
-> mapped to proper place via the 'router' (router holds the functions. mapper calls the functions)
-> only the model can access the database (i.e. insertion ... or if a 'get' then has to go through cache)


Gateway benifits
- reduces roundtrip
- security layer


Keep in mind that we have to use a global variable to store the list of items because its state must be shared across all operations.
