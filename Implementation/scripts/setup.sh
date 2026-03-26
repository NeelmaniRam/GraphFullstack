#!/bin/bash

echo "Setting up backend..."
cd backend
pip install -r requirements.txt

echo "Running data ingestion..."
python ingest/ingest_data.py

echo "Starting backend server..."
uvicorn main:app --reload &

echo "Setting up frontend..."
cd ../frontend
npm install

echo "Starting frontend..."
npm run dev