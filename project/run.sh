
scrapy_name='YY'

function all_run() {
    scrapy crawl $scrapy_name
    scrapy crawl $scrapy_name
    scrapy crawl $scrapy_name
    scrapy crawl $scrapy_name
    scrapy crawl $scrapy_name
    scrapy crawl $scrapy_name
    scrapy crawl $scrapy_name
    scrapy crawl $scrapy_name
    scrapy crawl $scrapy_name
    scrapy crawl $scrapy_name
    scrapy crawl $scrapy_name
}

function create() {
    scrapy startproject $scrapy_name
}

function run() {
    scrapy crawl $scrapy_name
}

function output_scrapy() {
    scrapy crawl $scrapy_name -o a.json
}

function output_requirs() {
    pip3 freeze > require.txt
}

function send() {
    python3 task.py
}