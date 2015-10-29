-- Table: data_word_noun

-- DROP TABLE data_word_noun;

CREATE TABLE data_word_noun
(
  noun_id integer NOT NULL, -- Первичный ключ
  noun character varying(50) NOT NULL, -- Наименование
  plural_number boolean NOT NULL DEFAULT false, -- Существительное во множественном числе (true/false, по умолчанию false)
  gram_gender "char" NOT NULL, -- Род существительного
  CONSTRAINT data_word_noun_pk PRIMARY KEY (noun_id),
  CONSTRAINT data_word_noun_uq UNIQUE (noun)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE data_word_noun
  OWNER TO fm;
COMMENT ON TABLE data_word_noun
  IS 'Словарь наименований с указанием рода и числа.';
COMMENT ON COLUMN data_word_noun.noun_id IS 'Первичный ключ';
COMMENT ON COLUMN data_word_noun.noun IS 'Наименование';
COMMENT ON COLUMN data_word_noun.plural_number IS 'Существительное во множественном числе (true/false, по умолчанию false)';
COMMENT ON COLUMN data_word_noun.gram_gender IS 'Род существительного';

-- Table: data_word_adjective

-- DROP TABLE data_word_adjective;

CREATE TABLE data_word_adjective
(
  adjective_id integer NOT NULL, -- Первичный ключ
  adjective character varying(50) NOT NULL,
  CONSTRAINT data_word_adjective_pk PRIMARY KEY (adjective_id),
  CONSTRAINT data_word_adjective_uq UNIQUE (adjective)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE data_word_adjective
  OWNER TO fm;
COMMENT ON TABLE data_word_adjective
  IS 'Словарь прилагательных';
COMMENT ON COLUMN data_word_adjective.adjective_id IS 'Первичный ключ';

-- Table: data_product

-- DROP TABLE data_product;

CREATE TABLE data_product
(
  product_id integer NOT NULL,
  noun_id integer NOT NULL,
  CONSTRAINT data_product_pk PRIMARY KEY (product_id),
  CONSTRAINT data_product_fk_noun FOREIGN KEY (noun_id)
      REFERENCES data_word_noun (noun_id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=FALSE
);
ALTER TABLE data_product
  OWNER TO fm;
COMMENT ON TABLE data_product
  IS 'Таблица продуктов-сущностей';

-- Table: data_product_detail

-- DROP TABLE data_product_detail;

CREATE TABLE data_product_detail
(
  product_id integer NOT NULL,
  adjective_id integer NOT NULL,
  row_order integer NOT NULL DEFAULT 0,
  CONSTRAINT data_product_detail_pk PRIMARY KEY (product_id, adjective_id),
  CONSTRAINT data_product_detail_fk_adjective FOREIGN KEY (adjective_id)
      REFERENCES data_word_adjective (adjective_id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT data_product_detail_fk_product FOREIGN KEY (product_id)
      REFERENCES data_product (product_id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT data_product_detail_uq_order UNIQUE (product_id, row_order)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE data_product_detail
  OWNER TO fm;

-- Table: ings_category

-- DROP TABLE ings_category;

CREATE TABLE ings_category
(
  category_id integer NOT NULL,
  category character varying(250) NOT NULL,
  CONSTRAINT ings_category_pk PRIMARY KEY (category_id),
  CONSTRAINT ings_category_uq UNIQUE (category)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE ings_category
  OWNER TO fm;
COMMENT ON TABLE ings_category
  IS 'Категории ингредиентов';

-- Table: ings_product

-- DROP TABLE ings_product;

CREATE TABLE ings_product
(
  product_id integer NOT NULL,
  category_id integer NOT NULL,
  ingredient character varying(500) NOT NULL,
  parent_id integer,
  is_abstract boolean NOT NULL DEFAULT false,
  CONSTRAINT ings_product_pk PRIMARY KEY (product_id),
  CONSTRAINT ings_product_fk_category FOREIGN KEY (category_id)
      REFERENCES ings_category (category_id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT ings_product_fk_parent FOREIGN KEY (parent_id)
      REFERENCES ings_product (product_id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT ings_product_fk_product FOREIGN KEY (product_id)
      REFERENCES data_product (product_id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=FALSE
);
ALTER TABLE ings_product
  OWNER TO fm;
COMMENT ON TABLE ings_product
  IS 'Таблица ингредиентов';
