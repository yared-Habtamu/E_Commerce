# E-Commerce Backend API

This project is a Django-based backend API for an e-commerce application. It provides endpoints for managing products, categories, reviews, shopping carts, and orders. The API is built using Django Rest Framework and includes filtering, searching, and ordering capabilities.

## Features

- **Product Management**: Add, view, update, and delete products.
- **Category Management**: Organize products into categories.
- **Reviews**: Users can leave reviews for products, including ratings and comments.
- **Shopping Cart**: Users can add products to their cart and manage quantities.
- **Orders**: Users can place orders, with detailed order items and total price.
- **Filtering and Searching**: Filter products by category, price, etc., and search by name or description.
- **Authentication**: Token-based authentication for user-related operations.

## Models

### Category
- `name`: Name of the category (unique).

### Product
- `name`: Name of the product.
- `description`: Description of the product.
- `price`: Price of the product.
- `category`: Foreign key to the `Category` model.
- `stock_quantity`: Quantity of the product in stock.
- `image_url`: Optional URL for the product image.
- `created_date`: Timestamp of product creation.

### Review
- `product`: Foreign key to the `Product` model.
- `user`: Foreign key to the `User` model.
- `rating`: Rating given by the user.
- `comment`: Review comment.
- `created_date`: Timestamp of review creation.

### Cart
- `user`: Foreign key to the `User` model.
- `product`: Foreign key to the `Product` model.
- `quantity`: Quantity of the product in the cart.
- `added_date`: Timestamp when the product was added to the cart.

### Order
- `user`: Foreign key to the `User` model.
- `products`: Many-to-many relation with the `Product` model through `OrderItem`.
- `total_price`: Total price of the order.
- `created_date`: Timestamp of order creation.

### OrderItem
- `order`: Foreign key to the `Order` model.
- `product`: Foreign key to the `Product` model.
- `quantity`: Quantity of the product in the order.
- `price`: Price of the product in the order.

## API Endpoints

### Product Endpoints
- `GET /api/products/`: List all products.
- `POST /api/products/`: Create a new product.
- `GET /api/products/<int:pk>/`: Retrieve a product by ID.
- `PUT /api/products/<int:pk>/`: Update a product by ID.
- `DELETE /api/products/<int:pk>/`: Delete a product by ID.

### Review Endpoints
- `GET /api/reviews/`: List all reviews.
- `POST /api/reviews/`: Create a new review.

### Cart Endpoints
- `GET /api/cart/`: View the user's cart.
- `POST /api/cart/`: Add a product to the cart.

### Order Endpoints
- `GET /api/orders/`: List all orders.
- `POST /api/orders/`: Create a new order.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yared-Habtamu/E_Commerce.git
   cd E_Commerce
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Configuration

- **Database**: Uses SQLite by default. Update `DATABASES` in `settings.py` for production.
- **Static Files**: Configure `STATIC_URL` and `STATIC_ROOT` for deployment.
- **Authentication**: Token-based authentication enabled via `rest_framework.authentication.TokenAuthentication`.

## Dependencies

Key dependencies include:
- Django
- Django Rest Framework
- django-filter
- gunicorn

For a complete list, see `requirements.txt`.

## Deployment

1. Ensure `DEBUG` is set to `False` in `settings.py`.
2. Set up a production-ready database (e.g., PostgreSQL).
3. Use `gunicorn` or another WSGI server to serve the application.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Author

Developed by Yared Habtamu.

Some sources and ideas are also added using the integration of ChatGPT.
