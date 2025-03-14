-- Create schema and table
CREATE TABLE "gear_vault_schema"."equipment" (
  "ID" integer PRIMARY KEY,
  "CATEGORY" text,
  "NAME" text,
  "BRAND" text,
  "MODEL" text,
  "STORE" text,
  "SIZE" text,
  "UNIT" integer,
  "PURCHASE_DATE" date,
  "NOTES" text
)

-- Modify the ID column to auto-increment
ALTER TABLE gear_vault_schema.equipment 
  ALTER COLUMN "ID" SET DATA TYPE integer
  -- ALTER COLUMN "ID" SET DEFAULT nextval('gear_vault_schema.equipment_id_seq'::regclass);

-- If the sequence does not exist, create it
CREATE SEQUENCE IF NOT EXISTS gear_vault_schema.equipment_id_seq 
  START 1;