import requests
import json

endpoint = "http://localhost:8000/api/"
# data_to_send = {"query": "Hello world"}
# query_data = {"abc":123}
# data_to_send = {}

# HTTP request --> HTML
# REST API HTTP request --> JSON
# Javascript object Notation ~ Python dictionary


get_response = requests.post(endpoint,json = {"title": "Welcome to Jumanji"})  # Use post method
print(get_response.json())

