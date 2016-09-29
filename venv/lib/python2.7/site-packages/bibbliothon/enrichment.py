
#!/usr/bin/env python
# coding:utf-8

# Python imports
import json
import requests

# Bibblio Python imports
from helpers import construct_content_item_url, construct_content_items_url
from urls import enrichment_url, metadata_url


# Content Item Endpoints
def create_content_item(access_token, payload):
	'''
	Name: create_content_item
	Parameters: access_token, payload (dict)
	Return: dictionary
	'''

	headers = {
		'Content-Type': 'application/json',
		'Authorization': 'Bearer ' + str(access_token)
	}

	request = requests.post(enrichment_url, json=payload, headers=headers)
	if request.status_code == 201:

		content_item = request.json()
		return content_item

	return {'status': request.status_code, "message": request.text}


def get_content_items(access_token, limit, page):
	'''
	Name: get_content_items
	Parameters: access_token, limit (optional), page (optional)
	Return: dictionary
	'''

	headers = {'Authorization': 'Bearer ' + str(access_token)}
	content_items_url =\
		construct_content_items_url(enrichment_url, limit, page)

	request = requests.get(content_items_url, headers=headers)
	if request.status_code == 200:

		content_item = request.json()
		return content_item

	return {'status': request.status_code, "message": request.text}


def get_content_item(access_token, content_item_id):
	'''
	Name: get_content_item
	Parameters: access_token, content_item_id
	Return: dictionary
	'''

	headers = {'Authorization': 'Bearer ' + str(access_token)}
	content_item_url =\
		construct_content_item_url(enrichment_url, content_item_id)

	request = requests.get(content_item_url, headers=headers)
	if request.status_code == 200:

		content_item = request.json()
		return content_item

	return {'status': request.status_code, "message": request.text}


def update_content_item(access_token, content_item_id, payload):
	'''
	Name: update_content_item
	Parameters: access_token, content_item_id, payload (dict)
	Return: dictionary
	'''

	headers = {'Authorization': 'Bearer ' + str(access_token)}
	content_item_url =\
		construct_content_item_url(enrichment_url, content_item_id)

	payload = create_random_payload(payload)
	request = requests.put(content_item_url, json=payload, headers=headers)

	if request.status_code == 200:

		content_item = request.json()
		return content_item

	return {'status': request.status_code, "message": request.text}


def delete_content_item(access_token, content_item_id):
	'''
	Name: delete_content_item
	Parameters: access_token, content_item_id
	Return: dictionary
	'''

	headers = {'Authorization': 'Bearer ' + str(access_token)}
	content_item_url =\
		construct_content_item_url(enrichment_url, content_item_id)

	request = requests.delete(content_item_url, headers=headers)
	return {'status': request.status_code, 'message': request.text}


def metadata(access_token, text): # (Legacy)
    '''
	Name: metadata_only
	Parameters: access_token, text (string)
	Return: dictionary
	'''

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + str(access_token)
	}

    payload = {'text': text}
    request = requests.post(metadata_url, json=payload, headers=headers)
    if request.status_code == 201:
        metadata = request.json()
        return metadata

    return {'status': request.status_code, "message": request.text}
