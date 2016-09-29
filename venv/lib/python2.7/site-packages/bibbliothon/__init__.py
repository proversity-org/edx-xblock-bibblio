
#!/usr/bin/env python
# coding:utf-8

access_token = ''
client_id = ''
client_secret = ''

from .authorization import get_access_token
from .discovery import content_recommendations, recommendations
from .enrichment import create_content_item, \
						get_content_item, get_content_items, \
						update_content_item, delete_content_item, \
						metadata


class Discovery:

	@classmethod
	def content_recommendations(self, content_item_id):
		return content_recommendations(access_token, content_item_id)

	@classmethod
	def recommendations(self, payload): # (Legacy)
		return recommendations(access_token, payload)


class Enrichment:

	@classmethod
	def create_content_item(cls, payload):
		return create_content_item(access_token, payload)

	@classmethod
	def get_content_items(cls, limit=None, page=None):
		return get_content_items(access_token, limit, page)

	@classmethod
	def get_content_item(cls, content_item_id):
		return get_content_item(access_token, content_item_id)

	@classmethod
	def update_content_item(cls, content_item_id, payload):
		return update_content_item(
			access_token,
			content_item_id,
			payload
		)

	@classmethod
	def delete_content_item(cls, content_item_id):
		return delete_content_item(access_token, content_item_id)

	@classmethod
	def metadata(cls, text): # (Legacy)
		return metadata(access_token, text)


class Token:

	@classmethod
	def get_access_token(cls):
		return get_access_token(client_id, client_secret)
