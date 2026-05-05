### Autonomous Data Intelligence Platform
This project demonstrates a path towards production-grade, end-to-end data ecosystem. Mlflow for tracing, clear cost management strategy, in addition to multi agentic ai frameworks are paramount.

#### 🏗️ Architecture Overview
The system follows an enhanced Medallion Architecture:

   1. Ingestion & Landing: Multi-source ingestion into raw storage.
   2. Silver Layer (Processing): Cleaned, standardized data used for Data Science.
   3. Gold Layer (Consumption): Business-level aggregates and feature stores.
   4. GenAI Engine: LLM-powered agents that interpret Gold data for autonomous actions.
   5. BI & Orchestration: Visualization and end-to-end workflow management.

#### 🚀 Key Components

##### 1. Data Ingestion & Governance

* Ingestion: Supports batch and streaming (e.g., Kafka, Flink, or Airbyte) to pull data from APIs, SQL databases, and logs; ideally Zerobus.
* Governance: Implementation of Unity Catalog to manage data lineage, PII masking, and RBAC (Role-Based Access Control).

##### 2. Data Warehousing (Medallion Flow)

* Bronze: Raw, immutable data history.
* Silver: Unified schemas. This layer hosts our Data Science models for feature engineering and predictive analytics (Scikit-learn, XGBoost).
* Gold: Final, high-performance tables optimized for BI tools and AI consumption.

##### 3. GenAI & Autonomous Decisions

* RAG Pipeline: Uses the Gold layer as a "Source of Truth."
* Autonomous Agents: Employs LLMs to analyze trends and trigger external actions (automatically adjusting supply chain orders based on predicted shortages) without manual intervention.

##### 4. Workflow Orchestration

* The core challenge lies in maintaining extensive memory across compute states without degrading execution quality. This serves as a valuable exercise in identifying the limits of compute and the necessity of sound architecture for LLM efficiency.

##### 🛠️ Tech Stack

* Languages: Python, SQL
* Processing: Spark / Databricks 
* Orchestration: Databricks
* GenAI/ML: LLMs, LangChain
* Storage: Unity Catalog / AWS default