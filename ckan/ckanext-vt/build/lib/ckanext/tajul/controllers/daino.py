import logging
import ckan.lib.base as base

class TajulController(base.BaseController):
	
    def aboutcmre(self):
        return base.render('home/aboutcmre.html')
