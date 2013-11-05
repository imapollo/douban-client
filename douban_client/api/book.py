# -*- coding: utf-8 -*-

from .subject import Subject

class Book(Subject):

    target = 'book'

    def __repr__(self):
        return '<DoubanAPI Book>'

    def isbn(self, isbn_id):
        return self._get('/v2/book/isbn/%s'%isbn_id)

    def get(self, id):
        return self._get('/v2/book/%s'%id)

    def list(self, user_id):
        return self._get('/v2/book/user/%s/collections'%user_id)['collections']

    def list_all(self, user_id):
        list = self._get('/v2/book/user/%s/collections?count=100'%user_id)
        total = list['total']
        list = list['collections']
        for start in range (100, total, 100):
            list = list + self._get('/v2/book/user/%s/collections?count=100&start=%s' % (user_id,start) )['collections']
        return list
