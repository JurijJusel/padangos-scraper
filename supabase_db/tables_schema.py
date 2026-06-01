#-- WARNING: This schema is for context only and is not meant to be run.
#-- Table order and constraints may not be valid for execution.

#CREATE TABLE public.tires_base (
#  id bigint GENERATED ALWAYS AS IDENTITY NOT NULL,
#  brand text,
#  model text,
#  product_class text,
#  price numeric,
#  wet_grip text,
#  fuel_effect text,
#  noise text,
#  remaining_quantity smallint,
#  url text,
#  CONSTRAINT tires_base_pkey PRIMARY KEY (id)
#);

#CREATE TABLE public.technical_info (
#  tires_id bigint GENERATED ALWAYS AS IDENTITY NOT NULL,
#  width smallint,
#  height smallint,
#  diameter smallint,
#  product_code text,
#  product_season text,
#  load_index smallint,
#  speed_index text,
#  reinforced text,
#  runflat text,
#  transport_type text,
#  construction_type text,
#  CONSTRAINT technical_info_pkey PRIMARY KEY (tires_id),
#  CONSTRAINT technical_info_tires_id_fkey FOREIGN KEY (tires_id) REFERENCES public.tires_base(id)
#);
