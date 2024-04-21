# Generate Dummy Data with Customizable JSON Data

This project allows you to generate a large amount of dummy data based on your customizable JSON data. It's particularly useful when you need to test APIs, responses, or any other functionality that requires a significant amount of data.

## How to Use?

Follow these steps to use this project:

1. Fork and clone this repository to your local machine.
2. Navigate to the cloned directory.
3. Put your customized JSON data inside the `sampleData.json` file.
4. To change the value of a particular key, you can update it from `modifyJson.py` file
5. To change the amount of generate data you can update it from `amountOfData.py` file
6. Open the terminal in the project directory.
7. Run the Python scripts in: `python writeJsonToFile.py`
8. Check the `generatedDummyData.json` file in the project directory for your dummy data.

## Example

Let's assume you have a sample JSON data with the following content:

```json
{
  "id": "1234567890",
  "user_name": "John Doe",
  "email": "john.doe@example.com",
  "product_name": "iPhone 12",
  "price": 999.99,
  "quantity": 1
}
```

and you want to just change the value of `product_name`, `price` and `quantity` to `iPhone 13`, `1000.00` and `2` respectively. You can do this using the `modifyJson.py` script in the project directory.

This updated README provides clear instructions on how to use the project and explains the objective of the project. It also includes an example to help users understand how to use their own data.
