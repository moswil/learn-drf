# APIViews

- Uses standard HTTP Methods for functions, i.e., get, post, put, patch, delete...
- Gives us most control over the our application logic:
  - Perfect for the case of implementing complex logic
  - Calling other APIs
  - Working with local files.
- Manually mapping URLs to `urls.py`

## When to use APIViews:

1. You need complete/full control over the logic. Such as running very complicated algorithm, or updating multiple data sources in one API call.
2. Processing files and rendering synchronous response. For instance, you are validating a file and returning the response in the same call.
3. You are calling other APIs/services.
4. Accessing local files or data.

# Viewsets

- Uses model operations for functions(list, create, retrieve, update, partial_update, destroy)
- Takes care of a lot of typical logic for you.
- Works pretty well with APIs for standard database operations, CRUD.
- Fastest way to make a database interface.
- Automatically maps URLs using Routers.

## When to use a Viewset:

1. Your APIs need to perform simple CRUD interface to your database.
2. You need quick and simple APIs to manage predefined objects.
3. You need very little to no customization on the logic provided by the DRF.
4. You are working with standard data structures.
