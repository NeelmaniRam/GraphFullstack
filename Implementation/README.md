# Context Graph System with LLM-Powered Query Interface

## 🚀 Overview

In real-world enterprise systems, business data is fragmented across multiple tables such as orders, deliveries, invoices, and payments. This makes it difficult to trace relationships and derive insights.

This project solves that problem by:

* Converting structured data into a **graph-based representation**
* Enabling **interactive graph exploration**
* Allowing users to query the system using **natural language**
* Dynamically translating queries into **SQL**
* Returning **data-backed responses (no hallucinations)**

---

## 🧠 Key Features

* 🔗 **Graph Modeling of Business Data**
* 📊 **Interactive Graph Visualization**
* 💬 **Natural Language Query Interface**
* ⚡ **Dynamic NL → SQL Translation using LLM**
* ✅ **Grounded Responses from Real Data**
* 🛡️ **Guardrails to restrict irrelevant queries**

---

## 🏗️ Architecture

```
Frontend (React)
   ├── Graph View (React Flow)
   └── Chat Interface

Backend (FastAPI)
   ├── Query Service (NL → SQL → Result)
   ├── Graph Service
   ├── LLM Service
   └── Guardrails

Database
   └── SQLite (Normalized Tables)

Graph Layer
   └── NetworkX (In-Memory Graph)
```

---

## 📊 Graph Data Modeling

### Node Types

* Customer
* Sales Order
* Sales Order Item
* Product
* Delivery
* Billing (Invoice)
* Accounting (Payment)

---

### Relationships (Edges)

* Customer → Sales Order
* Sales Order → Sales Order Item
* Sales Order Item → Product
* Sales Order → Delivery
* Delivery → Billing
* Billing → Accounting

---

### Example Flow

```
Customer → Order → Delivery → Billing → Payment
                  ↓
               Product
```

---

## 🗄️ Database Design

The raw dataset is denormalized and is transformed into structured tables:

* `customers`
* `products`
* `sales_orders`
* `sales_order_items`
* `deliveries`
* `billing`
* `accounting`

This normalization ensures:

* Efficient querying
* Clear relationships
* Scalability

---

## 🤖 LLM Integration Strategy

### 1. Natural Language → SQL

The LLM converts user queries into SQL using a structured prompt:

* Schema-aware prompting
* Strict rules to avoid hallucination
* Only allowed tables and columns

---

### 2. SQL Result → Natural Language

Query results are passed back to the LLM to generate:

* Clear explanations
* Data-backed insights
* Human-readable responses

---

### Example

**User Query:**

```
Which orders were delivered but not billed?
```

**Generated SQL:**

```sql
SELECT o.order_id
FROM sales_orders o
LEFT JOIN deliveries d ON o.order_id = d.order_id
LEFT JOIN billing b ON d.delivery_id = b.delivery_id
WHERE d.delivery_id IS NOT NULL
AND b.billing_id IS NULL;
```

---

## 🛡️ Guardrails

To ensure safe and relevant usage:

* Only dataset-related queries are allowed
* Irrelevant queries (e.g., jokes, poems) are rejected

**Example:**

```
User: Write me a poem  
Response: This system is designed to answer dataset-related queries only.
```

---

## 📊 Graph Visualization

* Built using **React Flow**
* Supports:

  * Node expansion
  * Relationship exploration
  * (Optional) Highlighting query results

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone <repo-link>
cd context-graph-system
```

---

### 2. Backend Setup

```bash
cd backend
pip install -r requirements.txt
```

---

### 3. Load Dataset

```bash
python ingest/ingest_data.py
```

---

### 4. Start Backend

```bash
uvicorn main:app --reload
```

---

### 5. Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

---

## 📦 Tech Stack

### Backend

* FastAPI
* SQLite
* NetworkX

### Frontend

* React
* React Flow

### LLM

* Groq / Gemini (Free Tier APIs)

---

## ⚖️ Design Decisions & Tradeoffs

### Why SQLite?

* Lightweight and fast
* No setup overhead
* Sufficient for structured queries

---

### Why Not Neo4j?

* Adds complexity
* Not necessary for assignment scope
* NetworkX is sufficient for graph visualization

---

### Why SQL Instead of Graph Queries?

* Easier LLM generation
* More reliable
* Better control over execution

---

## 🔥 Challenges & Solutions

### Challenge: Denormalized Dataset

**Solution:** Built preprocessing pipeline to normalize into relational tables

---

### Challenge: LLM Hallucination

**Solution:**

* Strict prompt constraints
* Schema grounding
* Post-validation of SQL

---

### Challenge: Broken Data Flows

**Solution:**

* Designed queries to detect missing links
* Enabled flow tracing

---

## ⭐ Future Improvements

* Graph highlighting based on query results
* Streaming responses from LLM
* Conversation memory
* Advanced graph analytics (clustering, centrality)
* Hybrid search (semantic + structured)

---

## 📁 Project Structure

```
backend/
frontend/
data/
scripts/
logs/
README.md
```

---

## 🧪 Example Queries Supported

* Which products have the highest billing count?
* Trace the full flow of a billing document
* Identify incomplete sales flows
* Which customers have the most orders?

---

## 📌 Conclusion

This project demonstrates how to combine:

* Data engineering
* Graph modeling
* Backend systems
* LLM-powered interfaces

to build an intelligent, real-world data exploration system.

---

## 🙌 Acknowledgment

This project was built as part of a Forward Deployed Engineer assignment to demonstrate system design, AI integration, and rapid prototyping skills.

---
