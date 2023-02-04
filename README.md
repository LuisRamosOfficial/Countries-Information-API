# Countries API built with Django Rest Framework

A RESTful API providing information about countries.
This API provides information about countries and is built using the Django Rest Framework (DRF) library.
## Endpoints

### 1. /names

This endpoint returns a list of all the country names.

#### Request
```javascript
GET /names
```


#### Response

```javascript
200 OK
[
"Afghanistan",
"Albania",
...
]

```

### 2. /country/{name}

This endpoint returns information about a specific country, such as its area, population, urban area, density, and median age. The `{name}` in the endpoint is a dynamic route, representing the name of the country.

#### Request
```
GET /country/{name}
```

#### Response
```
200 OK
{
"Area": 652230,
"Population": 37410163,
"Urban Area": 23817,
"Density": 56.9,
"Median Age": 30.1
}
```


## Examples

Get information about Afghanistan:
```
GET /country/Afghanistan
```

------
```
200 OK
{
"Area": 652230,
"Population": 37410163,
"Urban Area": 23817,
"Density": 56.9,
"Median Age": 30.1
}
```

## Benefits of Using Django Rest Framework

DRF provides a lot of features and tools out of the box that make building RESTful APIs easier and more efficient. Some of the key benefits of using DRF include:

- Simple, serialization-focused approach to defining API behavior.
- Robust and flexible request parsing.
- Support for request and response content negotiation.
- Support for authentication policies, including OAuth1a and OAuth2.
- Support for multiple authentication policies and per-view authentication policies.
- Support for multiple renderers, including JSON and XML.

With DRF, you can focus on building the functionality of your API and leave the details of handling requests and responses to the framework.