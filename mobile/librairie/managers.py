# -*- coding: utf-8 -*-
"""
Managers of ``librairie`` application.
"""
from django.db import models

class AuthorOnlineManager(models.Manager):
    """
    Manager that manages online ``Entry`` objects.
    """

    def get_query_set(self):
        return super(AuthorOnlineManager, self).get_query_set().filter(
            status=self.model.SELECT)
