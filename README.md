# EasyAPI

**EasyAPI** is a lightweight Python backend library designed to simplify API development. It provides essential features for building robust web applications with minimal setup.

## Features

- **HTTP Methods Support**  
    Handle different HTTP methods including `GET`, `POST`, and `DELETE`.

- **Routing & Dynamic URLs**  
    Define routes with dynamic URL parameters for flexible endpoint creation.

- **Middleware**  
    - **Global Middleware:** Apply logic (e.g., authentication, logging) to all requests.
    - **Route-Specific Middleware:** Attach middleware to individual routes for fine-grained control.

- **Class-Based Routing**  
    Organize endpoints using class-based views for better structure and reusability.

- **Template Engine Integration**  
    Render dynamic HTML responses using your preferred template engine.

## Example Usage

```python
from easyapi import EasyAPI, route, middleware

app = EasyAPI()

# Global middleware
@app.middleware
def log_request(request, response):
        print(f"{request.method} {request.path}")

# Route with dynamic URL and route-specific middleware
@app.route('/user/<int:user_id>', methods=['GET'])
@middleware(authenticate_user)
def get_user(request, user_id):
        # Logic to fetch user
        pass

# Class-based routing
class ItemAPI:
        @route('/item/<int:item_id>', methods=['GET'])
        def get(self, request, item_id):
                # Logic to fetch item
                pass

app.register(ItemAPI)
```

## Template Engine

EasyAPI supports integration with popular template engines (e.g., Jinja2) for rendering HTML.

```python
@app.route('/hello')
def hello(request):
        return app.render_template('hello.html', name='World')
```

## Future Plans

- **Auto-generate Swagger Docs:**  
    Automatically generate interactive API documentation using Swagger/OpenAPI.

---

Contributions and feedback are welcome!