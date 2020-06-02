"""
How to run?
$ python parser.py
"""
from parser.application.usecase import ParseHtmlUsecase


html_repository = None
structured_data_factory = None
structured_data_repository = None

parse_html_usecae = ParseHtmlUsecase(html_repository, structured_data_factory, structured_data_repository)
parse_html_usecae.parse()
