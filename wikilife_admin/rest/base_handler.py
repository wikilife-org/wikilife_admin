# coding=utf-8

from tornado.web import RequestHandler
from wikilife_utils.parsers.json_parser import JSONParser

"""
Common base handler shared amongst all admin handlers
"""


class BaseHandler(RequestHandler):

    _logger = None

    def initialize(self, services):
        RequestHandler.initialize(self)
        self._services = services
        self._logger = self.settings['logger']