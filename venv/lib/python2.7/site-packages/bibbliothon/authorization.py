#!/usr/bin/env python
# coding:utf-8

# Python imports
import json
import requests

# Bibblio Python imports
from urls import token_url

# Token Endpoint
def get_access_token(client_id, client_secret):
	'''
	Name: token
	Parameters: client_id, client_secret
	Return: dictionary
	'''

	headers = {'Content-Type': 'application/x-www-form-urlencoded'}
	payload = {
		'client_id': client_id,
		'client_secret': client_secret
	}

	request = requests.post(token_url, data=payload, headers=headers)
	if request.status_code == 200:
		token = request.json()
		return token

	return {'status': request.status_code, "message": request.text}
