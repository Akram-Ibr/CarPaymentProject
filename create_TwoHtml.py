import os

os.makedirs("templates", exist_ok=True)

index_html = """<!DOCTYPE html>
<html>
<head>
    <title>Car Loan Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            display: flex;
            justify-content: center;
            padding: 40px;
        }
        .form-container {
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            width: 400px;
        }
        h1 {
            text-align: center;
            color: #333;
        }
        label {
            display: block;
            margin-top: 15px;
            font-weight: bold;
            color: #555;
        }
        input, select {
            width: 100%;
            padding: 8px;
            margin-top: 5px;
            border: 1px solid #ccc;
            border-radius: 5px;
            box-sizing: border-box;
        }
        button {
            width: 100%;
            padding: 10px;
            margin-top: 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h1>Car Loan Calculator</h1>
        <form action="/calculate" method="POST">
            
            <label>ZIP Code:</label>
            <input type="text" name="zip_code" required>
            
            <label>County Tax Rate (e.g. 0.01):</label>
            <input type="text" name="county_tax_rate" required>
            
            <label>Credit Score:</label>
            <input type="text" name="credit_score" required>
            
            <label>Loan Type:</label>
            <select name="loan_type">
                <option value="new">New</option>
                <option value="used">Used</option>
            </select>
            
            <label>Car Price:</label>
            <input type="text" name="car_price" required>
            
            <label>Down Payment:</label>
            <input type="text" name="down_payment" required>
            
            <label>Trade-In Value:</label>
            <input type="text" name="trade_in_value" required>
            
            <label>Dealership Markup:</label>
            <input type="text" name="dealer_markup" required>
            
            <label>Loan Term (years):</label>
            <input type="text" name="term_years" required>
            
            <label>Dealership Fee:</label>
            <input type="text" name="dealership_fee" required>
            
            <label>Title Fee:</label>
            <input type="text" name="title_fee" required>
            
            <button type="submit">Calculate</button>
        </form>
    </div>
</body>
</html>
"""

results_html = """<!DOCTYPE html>
<html>
<head>
    <title>Your Loan Results</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            display: flex;
            justify-content: center;
            padding: 40px;
        }
        .results-container {
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            width: 400px;
        }
        h1 {
            text-align: center;
            color: #333;
        }
        p {
            font-size: 16px;
            color: #444;
        }
        a {
            display: inline-block;
            margin-top: 20px;
            text-decoration: none;
            color: white;
            background-color: #4CAF50;
            padding: 10px 15px;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="results-container">
        <h1>Your Loan Summary</h1>
        <p><strong>Location:</strong> {{ city }}, {{ state }}</p>
        <p><strong>Estimated APR:</strong> {{ apr }}%</p>
        <p><strong>Loan Amount:</strong> ${{ loan_amount }}</p>
        <p><strong>Monthly Payment:</strong> ${{ monthly_payment }}</p>
        <p><strong>Total Interest Paid:</strong> ${{ total_interest }}</p>
        
        <a href="/">Calculate Another</a>
    </div>
</body>
</html>
"""

error_html = """<!DOCTYPE html>
<html>
<head>
    <title>Error</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            display: flex;
            justify-content: center;
            padding: 40px;
        }
        .error-container {
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            width: 400px;
            text-align: center;
        }
        h1 { color: #c0392b; }
        a {
            display: inline-block;
            margin-top: 20px;
            text-decoration: none;
            color: white;
            background-color: #4CAF50;
            padding: 10px 15px;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="error-container">
        <h1>Invalid Input</h1>
        <p>{{ error_message }}</p>
        <a href="/">Go Back</a>
    </div>
</body>
</html>
"""

with open("templates/index.html", "w") as f:
    f.write(index_html)

with open("templates/results.html", "w") as f:
    f.write(results_html)

with open("templates/error.html", "w") as f:
    f.write(error_html)

print("HTML files created successfully.")