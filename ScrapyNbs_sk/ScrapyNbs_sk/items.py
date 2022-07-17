# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_jsonschema import JsonSchemaItem

class ScrapynbsSkItem(JsonSchemaItem):
    jsonschema = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "title": "Article",
        "description": "Article from nbs.sk",
        "type": "object",
        "properties": {
            "date": {
                "description": "Date of article",
                "type": "string"
            },
            "name": {
                "description": "Name of article",
                "type": "string"
            },
            "url": {
                "description": "Article page url",
                "type": "string"
            },
            "labels": {
                "description": "Tags",
                "type": "string"
            },
            "content": {
                "description": "Article content",
                "type": "string"
            }
        },
        "required": [
            "url"
        ]
    }
