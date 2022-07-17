# nbs.sk spider
Scrapy crawler using requests module to scrape data from nbs.sk website. The result is saved in a sqlite3 database. Using FastAPI the database is loaded and the items are listed when using endpoints.
# Installation
To install and run this project we need
1. Clone the project  
    **git clone https://github.com/ddhad/nbs-sk**
2. Activate virtual environment
3. Install the project packages  
    **pip install scrapy scrapy-jsonschema fastapi uvicorn**
# Pipelines
1. Validates the entire item based on a given JSON Schema  
**'scrapy_jsonschema.JsonSchemaValidatePipeline': 100,**  
2. Stores the output data in a SQLite database  
**'ScrapyNbs_sk.pipelines.ScrapynbsSkPipeline': 300,**
# How to run
1. Run spider  
    **scrapy crawl <spider_name>**
2. Run server  
    **uvicorn <name_of_file>:<name_of_FastAPI_variable> --reload**  
    In this case use  
**uvicorn working:app --reload**
