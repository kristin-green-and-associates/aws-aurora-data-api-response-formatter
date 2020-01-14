# AWS Aurora Data API Response Formatter
Your mission, should you choose to accept it, is to write a Python function that produces a useful JSON API response from Aurora's complicated Data API query response.

Consider the simple table presented in `Role.sql` and the sample data provided in `insertRoles.sql`. Below, I've presented two HTTP methods that would be common for a RESTful API server for any resource.

## GET /roles/{RoleID}

The `getRole.py` script that executes the `getRole.sql` query. Aurora gives us `getRole_actual.json` but we need `getRole_desired.json`.

## GET /roles

This should work for both a single object as well as an array of objects. The `getRoles.py` script that executes the `getRoles.sql` query. Aurora gives us `getRoles_actual.json` but we need `getRoles_desired.json`.
