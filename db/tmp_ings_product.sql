WITH RECURSIVE product_details(product_id, path, row_order, level) AS (
	select d.product_id, a.adjective || '' as path, d.row_order, 
	       (select max(row_order) from data_product_detail where product_id = d.product_id) as level
	  from data_product_detail d
	       inner join data_word_adjective a 
	           on (d.adjective_id = a.adjective_id)
	 where d.row_order = 0
    union all
	select pd.product_id, pd.path || ' ' || a.adjective as path, 
	       d.row_order, pd.level
	  from product_details pd
	       inner join data_product_detail d 
	           on (pd.product_id = d.product_id 
	               and pd.row_order + 1 = d.row_order)
	       inner join data_word_adjective a 
	           on (d.adjective_id = a.adjective_id)
  )
  insert into ings_product (product_id, ingredient, category_id) 
select p.product_id, n.noun || ' ' || coalesce(pd.path, '') as product, 1 as category_id
  from data_product p
       inner join data_word_noun n on (p.noun_id = n.noun_id)
       left outer join product_details pd on (p.product_id = pd.product_id)
 where pd.level is null or pd.level = pd.row_order;
