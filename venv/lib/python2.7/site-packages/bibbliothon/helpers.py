
#!/usr/bin/env python
# coding:utf-8

# Helpers
def construct_content_items_url(enrichment_url, limit, page):

	limit_query = "limit="
	has_limit = False
	if limit:

		try:
			limit_int = int(limit)
			limit_query += str(limit)
			has_limit = True

		except Exception as e:
			pass

	page_query = "page="
	has_page = False
	if page:

		try:
			page_int = int(page)
			page_query += str(page_int)
			has_page = True

		except Exception as e:

			pass

	new_enrichment_url = enrichment_url
	if has_limit:

		new_enrichment_url += '?' + limit_query
		if has_page:

			new_enrichment_url += '&' + page_query

	elif has_page:

		new_enrichment_url += '?' + page_query

	return new_enrichment_url


def construct_content_item_url(enrichment_url, content_item_id):

	return enrichment_url + '/' + str(content_item_id)


def construct_content_recommendations_url(enrichment_url, content_item_id):

	return enrichment_url + '/' + str(content_item_id) + '/recommendations'
