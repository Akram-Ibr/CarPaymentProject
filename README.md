# Car Loan Calculator

A Python and Flask web app that can estimate monthly car payments using real ZIP-code-based tax data — so you can run the numbers before ever stepping into a dealership.

# Features

> Calculates monthly payment, total amount paid, and total interest based on car price, down payment, trade-in value, dealer markup, loan term, and fees
> Looks up the user's state automatically from their ZIP code using a live API
> Estimates APR based on the user's credit score and whether the car is new or used
> Validates user input (credit score range, car price, loan term, etc.) and shows clear error messages for invalid entries

# How to Run

1. Make sure Python is installed
2. Install the required packages:

   pip install flask requests

3. Run the app:

   python app.py

4. Open your browser to http://127.0.0.1:5001

   (If port 5001 is already in use on your machine, change the port number in app.py by one or whatever than works.)

# Built With

> Python
> Flask
> HTML / CSS
> requests library (for live ZIP code lookups)
> pytest (for unit testing)
> JSON (for static tax rate data)

# What I Learned

Coming from AP Computer Science Principles/A in high school, I had originally thought classes and object-oriented programming as basic, simplelike. Building this project let me realize how much more powerful and versatile, that same foundation can become in practice — especially when applying it across two different languages (Python and HTML) and combining them into one combined application.

I also built and tested a command-line version of the calculator first, before adding the Flask web interface — this let me confirm all the core code worked correctly before attempting to leanr and build a web interface on top of it.
