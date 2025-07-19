
# Challenge 1 – SQL: Active Clients and Revenue

### Questions:

1. Write a query to list the clients who were active in the last 6 months.  

2. Calculate the total revenue and average ticket per client in this period.  

3. (Bonus) List the top 5 clients with the highest revenue growth comparing the last 6 months to the 6 months before that.  

# Challenge 2 – Pandas: Exploratory Analysis using Pandas

### Tasks:

1. Load the data with Pandas, and create a new column called `dias_desde_ultima_compra` (assuming current date = "2025-07-17").

2. Create a boolean column `possivel_churn`, which is True if the customer hasn’t made a purchase in the last 180 days.

3. Calculate the average `total_gasto` for clients marked as `possivel_churn == True`.

# Challenge 3 – Pandas: Monthly Revenue Analysis

### Tasks:

1. Create a column `mes_ano` in the format "YYYY-MM".

2. Calculate total revenue per month.

3. Generate a line chart showing monthly revenue evolution.

# Challenge 4 – Pandas: Most Sold Products

You have two DataFrames: `vendas` and `produtos`.

1. Merge the tables using `merge`.

2. Calculate total sold per product (`quantidade * preco_unitario`).

3. List products from most sold to least sold.

# Challenge 5 – Detect Duplicates and Clean Data
You received a marketing leads file containing errors.

### Tasks:
1. Identify and remove duplicate records based on the email.

2. Standardize the names to title case (e.g., Ana, Bruno Lima) using .str.title().

3. Check for invalid or missing dates.

# Challenge 6 – Conversion Rate by Marketing Channel
You have the following DataFrame:

### Tasks:
1. Calculate the conversion rate per channel (fez_compra == True / visitou_site == True).

2. Sort the channels from highest to lowest conversion rate.

3. Create a bar chart with the results.
