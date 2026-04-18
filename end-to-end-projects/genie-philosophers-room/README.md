### Genie Space

This project uses Genie to process source files from gutenberg.org, including images and tables. The core challenge lies in developing effective parsing techniques for large datasets in .txt and .epub formats using both batch and streaming loads. Ultimately, this tool aims to support decision-making within the Genie Space ecosystem

#### Genie suggested setup 
1) Semantic Understanding: It leverages metadata from Unity Catalog, including table/column names, descriptions, and primary/foreign key relationships to understand data context
2) Knowledge Store: Domain experts can "curate" a Genie space by adding sample SQL queries, text instructions, and column-level synonyms to help the AI understand company-specific jargon.
3) Supported Objects: Managed tables, external tables, foreign tables (via Lakehouse Federation), views, materialized views, and Metric Views.
4) Data Types: It supports standard SQL types registered in Unity Catalog, including String, Date, Numeric (Decimal/Integer), and Date and Time.
5) File Uploads: users can blend local CSV and Excel files with governed Unity Catalog data for ad-hoc analysis


///