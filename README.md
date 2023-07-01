# Project README

This is a Flask project that provides a simple CRUD (Create, Read, Update, Delete) functionality for managing product inventory. The project uses SQLAlchemy as an ORM (Object-Relational Mapping) tool to interact with a PostgreSQL database.

## Installation

1. Clone the repository to your local machine.

2. Ensure you have Python 3.x installed on your system.

3. Install the required dependencies by running the following command in your terminal:

pip install -r requirements.txt

4. Set up a PostgreSQL database. You can install PostgreSQL from the official website (https://www.postgresql.org/) and create a database named `crudsi`.

5. Update the `SQLALCHEMY_DATABASE_URI` in the `app.py` file with your PostgreSQL connection details (e.g., username, password, host, port).

6. Run the Flask application by executing the following command:

python app.py


7. Access the application by visiting `http://localhost:8000` in your web browser.

## Usage

The application provides the following routes:

- `/`: Displays a list of all products in the inventory.

- `/cadastrar`: Allows you to add a new product to the inventory.

- `/remover`: Allows you to remove a product from the inventory.

- `/editar`: Allows you to edit the details of a product in the inventory.

### Adding a Product

To add a product to the inventory, follow these steps:

1. Visit the `/cadastrar` route.

2. Fill out the form with the product details, including the product name, description, price, and quantity.

3. Click the "Cadastrar" button to submit the form.

4. The product will be added to the inventory, and you will be redirected back to the `/cadastrar` page with a success message.

### Removing a Product

To remove a product from the inventory, follow these steps:

1. Visit the `/remover` route.

2. Fill out the form with the product name and quantity to be removed.

3. Click the "Remover" button to submit the form.

4. If the product exists in the inventory and the specified quantity is available, the product will be removed, and you will be redirected back to the `/remover` page.

5. If the product does not exist in the inventory or the specified quantity is greater than the available quantity, an appropriate error message will be displayed.

### Editing a Product

To edit the details of a product in the inventory, follow these steps:

1. Visit the `/editar` route.

2. Fill out the form with the product name and the updated details (e.g., quantity, price).

3. Click the "Editar" button to submit the form.

4. If the product exists in the inventory, its details will be updated with the provided information, and you will be redirected back to the `/editar` page.

## Contributing

Contributions to this project are welcome. If you find any issues or want to suggest improvements, please create a new issue on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).

