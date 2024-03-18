#for new page view
import routes.mapper
#from ckanext.tajul.base import BaseController

#for api call in python
from urllib.request import urlopen as uReq

#access ckan plugins
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

#extends this action method
from .logic import action, auth
from ckanext.tajul.logic.action.get import resource_search, tag_list, group_list, data_list

from ckan.common import config
'''from ckanext.datastore.interfaces import IDatastore
from ckanext.datastore.backend import (
    DatastoreBackend, InvalidDataError
)
import logging
import ckan.logic as logic
import ckanext.datastore.logic.schema as dsschema
import ckan.lib.dictization as dictization
import ckan.lib.dictization.model_dictize as model_dictize
import ckan.lib.dictization.model_save as model_save
import ckan.lib.navl.dictization_functions
import ckan.lib.navl.validators as validators
import ckan.lib.search as search

log = logging.getLogger(__name__)

_validate = ckan.lib.navl.dictization_functions.validate
_get_action = logic.get_action
_check_access = logic.check_access
NotFound = logic.NotFound
ValidationError = logic.ValidationError
_get_or_bust = logic.get_or_bust

WHITELISTED_RESOURCES = ['_table_metadata']
try:
    from ckanext.datasolr.interfaces import IDataSolr
except ImportError:
    pass'''

#import ckanclient
#ckan = ckanclient.CkanClient(api_key='6044b316-cbf5-4718-99cf-d60f7a77d0ee')
#log = logging.getLogger('ckan.logic')

#from ckanext.tajul.api_call import get_data

u = 'http://localhost:5000/api/3/action/datastore_upsert'
ckan_api_key = '71e2aebb-f605-4ad3-8d63-aa32f5be0bae'
resource_id = '019e8492-3363-4db6-beee-adfb1ca0b365'

def group_create(context, data_dict=None):

    # Get the value of the ckan.iauthfunctions.users_can_create_groups
    # setting from the CKAN config file as a string, or False if the setting
    # isn't in the config file.
    #print("Hi")
    users_can_create_groups = config.get(
        'ckan.iauthfunctions.users_can_create_groups', False)

    # Convert the value from a string to a boolean.
    users_can_create_groups = toolkit.asbool(users_can_create_groups)

    if users_can_create_groups:
        return {'success': True}
    else:
        return {'success': False,
                'msg': 'Only sysadmins can create groups'}



def promoted_blocks():

    groups = toolkit.get_action('group_list')(
        data_dict={'sort': 'package_count desc', 'all_fields': True})
    
    #groups = groups
    # Get the tag list.
    #tag_list = toolkit.get_action('data_list')(
        #data_dict={'sort': 'package_count desc', 'all_fields': True})
    #print(tag_list)
    
    return groups
	
def most_popular_groups():
    '''Return a sorted list of the groups with the most datasets.'''

    # Get a list of all the site's groups from CKAN, sorted by number of
    # datasets.
    #print(toolkit.get_action('group_list')(data_dict={'sort': 'package_count desc', 'all_fields': True}))
    groups = toolkit.get_action('group_list')(
        data_dict={'sort': 'package_count desc', 'all_fields': True})

    # Truncate the list to the 10 most popular groups only.
    groups = groups[:5]

    return groups

def most_popular_organizations():
    '''Return a sorted list of the groups with the most datasets.'''

    # Get a list of all the site's groups from CKAN, sorted by number of
    # datasets.
    organizations = toolkit.get_action('organization_list')(
        data_dict={'sort': 'package_count desc', 'all_fields': True})

    # Truncate the list to the 10 most popular groups only.
    organizations = organizations[:5]

    return organizations
      
def _is_resource(obj):
    """
    Check if a dict describes a resource.
    This is a very simple, duck-typing style test that only checks
    whether the dict contains an ``package_id`` entry.
    """
    return 'package_id' in obj

#filter views
def _remove_linebreaks(string):
    '''Convert a string to be usable in JavaScript'''
    return str(string).replace('\n', '')
    
def _get_filter_values(resource):
    ''' Tries to get out filter values so they can appear in dropdown list.
    Leaves input as text box when the table is too big or there are too many
    distinct values.  Current limits are 5000 rows in table and 500 distict
    values.'''

    data = {
        'resource_id': resource['id'],
        'limit': 5001
    }
    result = p.toolkit.get_action('datastore_search')({}, data)
    # do not try to get filter values if there are too many rows.
    if len(result.get('records', [])) == 5001:
        return {}

    filter_values = {}
    for field in result.get('fields', []):
        if field['type'] != 'text':
            continue
        distinct_values = set()
        for row in result.get('records', []):
            distinct_values.add(row[field['id']])
        # keep as input if there are too many distinct values.
        if len(distinct_values) > 500:
            continue
        filter_values[field['id']] = [{'id': value, 'text': value}
                                      for value
                                      in sorted(list(distinct_values))]
    print(filter_values)
    return filter_values
        
class TajulPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    #plugins.implements(plugins.IConfigurable)
    plugins.implements(plugins.IAuthFunctions)
    plugins.implements(plugins.IActions)
    #plugins.implements(IDatastoreBackend)
    #plugins.implements(plugins.IDatastoreBackend)
    plugins.implements(plugins.IPackageController, inherit=True)
    plugins.implements(plugins.IResourceController, inherit=True)
    plugins.implements(plugins.IFacets, inherit=True)
    plugins.implements(plugins.IRoutes, inherit=True)
    plugins.implements(plugins.ITemplateHelpers)
    #plugins.implements(IDatastore)
    '''try:
        plugins.implements(IDataSolr)
    except NameError:
        pass'''
        
    # IConfigurer
    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('public','tajul')
    #mapping new view
    def before_map(self, map):
    	map.connect('tajul', '/tajul', controller='ckanext.tajul.controllers.tajul:TajulController', action='tajul')
    	map.connect('tajul', '/tajul/{id}', controller='ckanext.tajul.controllers.tajul:TajulController', action='tajul_search')
    	return route_map
        
    def after_map(self, route_map):
        return route_map
            
    #IFacets
    def dataset_facets(self, facets_dict, package_type):
    	#print(facets_dict)
    	#print(package_type)
    	return facets_dict
    	
    #IPackageController    
    def before_search(self, search_params): #before the search results appears
        return search_params    
    def after_search(self, search_results, search_params): #before the search results appears -> in the dataset page how the results will appears
    	return search_results
    	
    #IResourceController	
    def before_create(resource_id, context, data_dict): #before creating=uploading any dataset=resource 
    	return data_dict
    def after_create(resource_id, context, data_dict): #after creating any resource -> we can access resource_id / url of the new dataset=resource
    	return data_dict
    	
    #IAuthFunctions	
    def get_auth_functions(self):
        return {'group_create': group_create}
        
    #IActions
    def get_actions(self):
        return {'resource_search': resource_search,'group_list': group_list,'tag_list': tag_list, 'data_list': data_list}
    
    #IDatastore    
    '''def datastore_validate(self, context, data_dict, fields_types):
        return data_dict
    def datastore_search(self, context, data_dict, all_field_ids, query_dict):
        backend = DatastoreBackend.get_active_backend()
        schema = context.get('schema', dsschema.datastore_search_schema())
        data_dict, errors = _validate(data_dict, schema, context)
        print(data_dict)
        if errors:
                raise p.toolkit.ValidationError(errors)

        res_id = data_dict['resource_id']

        if data_dict['resource_id'] not in WHITELISTED_RESOURCES:
                res_exists, real_id = backend.resource_id_from_alias(res_id)
                if not res_exists:
                        raise p.toolkit.ObjectNotFound(p.toolkit._('Resource "{0}" was not found.'.format(res_id)))
                if real_id:
                        data_dict['resource_id'] = real_id
                
                plugins.toolkit.check_access('datastore_search', context, data_dict)

        result = backend.search(context, data_dict)
        result.pop('id', None)
        result.pop('connection_url', None)
        return data_dict'''
    
    #IDataSolr
    '''def datasolr_validate(self, context, data_dict, fields_types):
        return self.datastore_validate(context, data_dict, fields_types)'''
        
    #ITemplateHelpers           
    def get_helpers(self):
        '''Register the most_popular_groups() function above as a template
        helper function.

        '''
        # Template helper function names should begin with the name of the
        # extension they belong to, to avoid clashing with functions from
        # other extensions.
        return {'tajul_most_popular_organizations': most_popular_organizations,'tajul_most_popular_groups': most_popular_groups, 'tajul_promoted_blocks': promoted_blocks, 'remove_linebreaks': _remove_linebreaks,'get_filter_values': _get_filter_values}
