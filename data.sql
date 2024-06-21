show databases;
use test;
show tables;

desc data;


-- INSERT INTO data(omni_upc_nbr,op_cmpny_cd,geo_region_cd,omni_seg_nbr,omni_seg_desc,omni_dept_nbr,omni_dept_desc,
-- omni_catg_grp_nbr,omni_catg_grp_desc,omni_catg_nbr,omni_catg_desc,omni_subcatg_nbr,omni_subcatg_desc,fineline_nbr,
-- fineline_desc,brand_nm,last4yr_purchased_ind,upc_short_desc,upc_long_desc,load_ts,userid,upd_ts) VALUES 
-- ("0590321093530","WMT-US","US",50000,"CLOTHES",34,"WOMENS APPAREL",1056335,"TREND ECOMM WOMENS",1056337,
-- "TOPS TREND ECOMM WOMENS",1056403,"SLVLS TOPS TREND EC WOMENS",0,0,0,0,0,
-- "FREE SHIPPING-Womens Vintage Funny Oktoberfest Print Pattern Festival Fashion Sexy Round Neck Sleeveless Tank Top T-Shirt Blouse,Gray,valentines day gifts",
-- 2024-06-18,"dataproc",2024-06-18);

CREATE TABLE product (

product_id INT PRIMARY KEY,

product_name VARCHAR(255),

category VARCHAR(50),

price DECIMAL(10, 2),

stock_quantity INT

);
INSERT INTO product VALUES (1, "Trousers", "Apparel", 2000, 1000), (2, "Shirts", "Apparel", 1000, 1000);
select * from product;