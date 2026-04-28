-- Enable pgvector extension in the realestate database
-- This runs automatically on first container startup

\c realestate;

CREATE EXTENSION IF NOT EXISTS vector;
