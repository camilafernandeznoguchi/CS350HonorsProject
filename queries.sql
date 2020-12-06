/*Find the IDs of all clients who have made an order after 2016.*/
SELECT client_id
FROM "Order"
WHERE order_date > '2016-12-31';

/*Find the IDs of all clients who have bought more than 1 mattress in the same order.*/
SELECT "Order".client_id
FROM "Order"
WHERE 1 < (
        SELECT COUNT(Mattress.product_id)
        FROM Mattress, Order_Product, Client
        WHERE Mattress.product_id = Order_Product.product_id 
            AND Order_Product.order_id = "Order".order_id 
            AND "Order".client_id = Client.client_id)
Order by "Order".client_id;

/*Find which store has the most stock the product with id = 2115020691.*/
SELECT Store.store_id, address
FROM Store
JOIN Catalogue ON Store.store_id = Catalogue.store_id
WHERE product_id = '2115020691' AND stock = (
	SELECT MAX(stock)
	FROM Store
	JOIN Catalogue ON Store.store_id = Catalogue.store_id
	WHERE product_id = '2115020691'
);