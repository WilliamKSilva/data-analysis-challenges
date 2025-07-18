-- Challenge 1 – SQL: Active Clients and Revenue
-- Questions:

-- 1. Write a query to list the clients who were active in the last 6 months.  
-- Solution:
SELECT * FROM clientes as tc
INNER JOIN vendas tv ON tv.id_cliente = tc.id_cliente
WHERE
	tv.data_venda BETWEEN (NOW() - INTERVAL '6 months') AND NOW();

-- 2. Calculate the total revenue and average ticket per client in this period
SELECT
SUM(tv.valor_venda) as receita_total,
ROUND(SUM(tv.valor_venda) / COUNT(tc.id_cliente)::NUMERIC, 2) as ticket_medio
FROM vendas as tv
INNER JOIN clientes tc ON tc.id_cliente = tv.id_cliente
WHERE
    tv.data_venda BETWEEN (NOW() - INTERVAL '6 months') AND NOW();

-- 3. (Bonus) List the top 5 clients with the highest revenue growth comparing the last 6 months to the 6 months before that.
SELECT six_months_revenue.nome, six_months_revenue.receita - twelve_months_revenue.receita crescimento_receita FROM (
    SELECT
    tc.id_cliente,
    tc.nome,
    SUM(tv.valor_venda) receita
FROM clientes as tc
INNER JOIN vendas tv ON tv.id_cliente = tc.id_cliente
    WHERE
    tv.data_venda BETWEEN (NOW() - INTERVAL '6 months') AND NOW()
GROUP BY tc.id_cliente, tc.nome
) as six_months_revenue
JOIN (
    SELECT
    tc.id_cliente,
    tc.nome,
    SUM(tv.valor_venda) receita
    FROM clientes as tc
    INNER JOIN vendas tv ON tv.id_cliente = tc.id_cliente
    WHERE
        tv.data_venda BETWEEN (NOW() - INTERVAL '12 months') AND (NOW() - INTERVAL '6 months')
        OR tv.data_venda BETWEEN (NOW() - INTERVAL '6 months') AND NOW()
    GROUP BY tc.id_cliente, tc.nome
) as twelve_months_revenue ON six_months_revenue.id_cliente = twelve_months_revenue.id_cliente
ORDER BY six_months_revenue.receita - twelve_months_revenue.receita ASC;