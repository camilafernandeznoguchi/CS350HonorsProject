CREATE TABLE Product (
  product_id varchar(10),
  detail varchar(500),
  price int,
  PRIMARY KEY (product_id)
);
copy Product from '/Users/camilafernandez/Desktop/CS350HonorsProject/data/Productos.csv' delimiter ',' csv;

CREATE TABLE Client (
  client_id varchar (8),
  name varchar (255),
  surname varchar (255),
  address varchar (500),
  phone int,
  PRIMARY KEY (client_id)
);
copy Client from '/Users/camilafernandez/Desktop/CS350HonorsProject/data/cliente_1000.csv' delimiter ',' csv;

CREATE TABLE Store (
  store_id varchar(10),
  address varchar(500),
  PRIMARY KEY (store_id)
);
copy Store from '/Users/camilafernandez/Desktop/CS350HonorsProject/data/store.csv' delimiter ',' csv;

CREATE TABLE "Order" (
  order_id varchar(10),
  order_date date,
  client_id varchar (8),
  PRIMARY KEY (order_id),
  FOREIGN KEY (client_id) REFERENCES Client (client_id)
);
copy "Order" from '/Users/camilafernandez/Desktop/CS350HonorsProject/data/Pedido_1000.csv' delimiter ',' csv;

CREATE TABLE Mattress (
  product_id varchar(10),
  filling varchar(255),
  size varchar(15),
  PRIMARY KEY (product_id),
  FOREIGN KEY (product_id) REFERENCES Product (product_id)
);
copy Mattress from '/Users/camilafernandez/Desktop/CS350HonorsProject/data/Colchones.csv' delimiter ',' csv;

CREATE TABLE Order_Product(
  order_id varchar(11),
  product_id varchar (10),
  store_id varchar(10),
  quantity int,
  PRIMARY KEY (order_id, product_id, store_id),
  FOREIGN KEY (order_id) REFERENCES "Order" (order_id),
  FOREIGN KEY (product_id) REFERENCES Product (product_id),
  FOREIGN KEY (store_id) REFERENCES Store (store_id)
);
copy Order_Product from '/Users/camilafernandez/Desktop/CS350HonorsProject/data/Tiene_1000.csv' delimiter ',' csv;

CREATE TABLE Couch(
  product_id varchar(10),
  model varchar(255),
  PRIMARY KEY (product_id),
  FOREIGN KEY (product_id) REFERENCES Product (product_id)
);
copy Couch from '/Users/camilafernandez/Desktop/CS350HonorsProject/data/Sofas.csv' delimiter ',' csv;

CREATE TABLE Natural_Person (
  client_id varchar (8),
  PRIMARY KEY (client_id),
  FOREIGN KEY (client_id) REFERENCES Client (client_id)
);
copy Natural_Person from '/Users/camilafernandez/Desktop/CS350HonorsProject/data/PersonaNatural_1000.csv' delimiter ',' csv;

CREATE TABLE Pillow (
  product_id varchar(10),
  filling varchar(255),
  PRIMARY KEY (product_id),
  FOREIGN KEY (product_id) REFERENCES Product (product_id)
);
copy Pillow from '/Users/camilafernandez/Desktop/CS350HonorsProject/data/Almohada.csv' delimiter ',' csv;

CREATE TABLE Legal_Representative (
  client_id varchar (8),
  PRIMARY KEY (client_id),
  FOREIGN KEY (client_id) REFERENCES Client (client_id)
);
copy Legal_Representative from '/Users/camilafernandez/Desktop/CS350HonorsProject/data/Representante_1000.csv' delimiter ',' csv;

CREATE TABLE Juridical_Person (
  ruc varchar (11),
  name varchar (255),
  address varchar (500),
  representative_id varchar (8),
  phone varchar (9),
  PRIMARY KEY (ruc, representative_id),
  FOREIGN KEY (representative_id) REFERENCES Legal_Representative (client_id)
);
copy Juridical_Person from '/Users/camilafernandez/Desktop/CS350HonorsProject/data/personaJuridica_1000.csv' delimiter ',' csv;

CREATE TABLE Catalogue (
  product_id varchar(10),
  store_id varchar(10),
  stock int,
  PRIMARY KEY (product_id, store_id),
  FOREIGN KEY (product_id) REFERENCES Product (product_id),
  FOREIGN KEY (store_id) REFERENCES Store (store_id)
);
copy Catalogue from '/Users/camilafernandez/Desktop/CS350HonorsProject/data/Catalogo.csv' delimiter ',' csv;