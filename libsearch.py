# -*- coding: utf8 -*-

import urllib
import urllib2
import re

def gen_search_in_university(url, url_values, keyword_re, return_found=True):
    def search(ISBN):
#        print url_values
#        print url_values.format(ISBN=ISBN)
        page = search_in_university(url, url_values.format(ISBN=ISBN))
#        print page
        if re.search(keyword_re, page):
            return True if return_found is True else False
        else:
            return False if return_found is True else True

    return search

def search_in_university(url, url_values):
    full_url = url + '?' + url_values
#    print full_url
    try: 
        resp = urllib2.urlopen(full_url)
        page = resp.read()
        return page
    except:
        return ''


def search_in_IU(ISBN):

    '''
     印地安那大學伯明頓分校  Indiana University–Bloomington
    '''
    url = 'http://iucat.iu.edu/catalog'
    data = {}
    data ['utf8'] = '✓'
    data ['q'] = ISBN
    data ['search_field'] = 'all_fields'
    data ['commit'] = 'search'
    
    url_values = urllib.urlencode(data)
    full_url = url + '?' + url_values
    resp = urllib2.urlopen(full_url)
    page = resp.read()
#    print page
    
    if re.search('No items found', page):
        return False
    else:
        return True

def search_in_Illinois(ISBN):
    
    '''
    伊利諾大學厄巴納香檳分校  University of Illinois–Urbana-Champaign
      http://vufind.carli.illinois.edu/vf-uiu/ 
    '''

    url = 'http://vufind.carli.illinois.edu/vf-uiu/'
    
    data = {}
    data ['lookfor'] = ISBN
    data ['type'] = 'isn'
    data ['start_over'] = '1'
    data ['submit'] = 'Find'

    url_values = urllib.urlencode(data)
    full_url = url + '?' + url_values
    resp = urllib2.urlopen(full_url)
    page = resp.read()
#    print page
    
    if page.find('did not match any resources') == -1:
        return True
    else:
        return False

def search_in_UW(ISBN):
    
    '''
     華盛頓大學  University of Washington
     http://alliance-primo.hosted.exlibrisgroup.com/primo_library/libweb/action/search.do?mode=Basic&vid=UW&tab=default_tab&

     Match rule: key word 'Available in the Library' appeared in the page
    '''

    url = 'http://alliance-primo.hosted.exlibrisgroup.com/primo_library/libweb/action/search.do'
    url_values = 'fn=search&ct=search&initialSearch=true&mode=Basic&tab=default_tab&indx=1&dum=true&srt=rank&vid=UW&frbg=&tb=t&vl%28freeText0%29={ISBN}&scp.scps=scope%3A%28NZ%29%2Cscope%3A%28UW%29%2Cprimo_central_multiple_fe'.format(ISBN\
            = ISBN)

    full_url = url + '?' + url_values
    resp = urllib2.urlopen(full_url)
    page = resp.read()
#    print page
    
    if re.search('Available in the Library', page):
        return True
    else:
        return False

def search_in_SYR(ISBN):
    '''
    雪城大學  Syracuse University
    http://summit.syr.edu/vwebv/searchBasic 

    Key word: Search resulted in no hits
    '''

    url = 'http://summit.syr.edu/vwebv/search'
    url_values  = 'searchArg={ISBN}&searchCode=GKEY%5E*&limitTo=none&recCount=50&searchType=1&page.search.search.button=Search'.format(ISBN = ISBN)


    full_url = url + '?' + url_values
    resp = urllib2.urlopen(full_url)
    page = resp.read()
#    print page
    
    if re.search(' Search resulted in no hits', page):
        return False
    else:
        return True


def search_in_UMICH(ISBN):

    '''
    密西根大學安娜堡分校  University of Michigan–Ann Arbor
    http://mirlyn.lib.umich.edu/ 
    '''

    url = 'http://mirlyn.lib.umich.edu/Search/Home'
    url_values =\
    'checkspelling=true&inst=all&showsearchonly=false&oft=false&lookfor={ISBN}&type=all&submit=Find&use_dismax=1'.format(ISBN=ISBN)
    page = search_in_university(url, url_values);
    
    #print page
    if re.search('did not match any resources', page): 
        return False
    else:
        return True





def search_in_UTEXAS(ISBN):
    '''
    德州大學奧斯汀分校  University of Texas–Austin 
    http://catalog.lib.utexas.edu/search/
    '''
    url = 'http://catalog.lib.utexas.edu/search/i' 
    url_values = 'SEARCH={ISBN}&searchscope=29&sortdropdown=-'.format(ISBN=ISBN)
    page = search_in_university(url, url_values);
    if re.search('No matches found', page):
        return False
    else:
        return True




def search_in_IUB(ISBN):
    '''
     印地安那大學伯明頓分校  Indiana University–Bloomington   
    '''
    url = 'http://libraries.iub.edu/search/ebsco'
    url_values = 'keywords={ISBN}&type=AllFields&amount=brief'.format(ISBN=ISBN)

    page = search_in_university(url, url_values)
    #print page

    if re.search('Your search did not match any resources.', page):
        return False
    else:
        return True


def search_in_SIMMONS(ISBN):
    '''
    西蒙學院  Simmons College        
    http://www.simmons.edu/library/ 
    '''

    url = 'http://www.simmons.edu/library/'
    url_values =\
    'keywords=sid=e3f8f555-2d6e-4fad-93a7-3ea51b803752%40sessionmgr198&vid=0&hid=123&bquery={ISBN}&bdata=JmNsaTA9RlQxJmNsdjA9WSZ0eXBlPTAmc2l0ZT1lZHMtbGl2ZSZzY29wZT1zaXRl'.format(ISBN=ISBN)

    page = search_in_university(url, url_values)
    #print page

    if re.search('Your search did not match any resources.', page):
        return False
    elif re.search('<p class="caption">Book', page):
        return True
    else: 
        return False

def search_in_DREXEL(ISBN):
    '''
    卓克索大學  Drexel University  
    http://innoserv.library.drexel.edu/ 
    '''
    url = 'http://innoserv.library.drexel.edu/search~S9/'
    url_values = \
    'searchtype=i&searcharg={ISBN}&searchscope=9&SORT=D&extended=0&SUBMIT=Search&searchlimits=&searchorigarg=i{ISBN}'.format(ISBN=ISBN)

    page = search_in_university(url, url_values)

    #print page
    if re.search('No matches found', page):
        return False
    else:
        return True



# 北卡羅萊納大學帕克分校  
# University of North Carolina–Chapel Hill      		  
# http://search.lib.unc.edu/search.jsp 

search_UNC = gen_search_in_university('http://search.lib.unc.edu/search',\
        'Ntt={ISBN}&Ntk=ISBN&Nty=1', 'Format.*\n.*Book', return_found=True)


# 羅格斯大學新新伯朗士威分校  
# Rutgers–New Brunswick       		 
# http://www.libraries.rutgers.edu/

RUTGERS_url = ('https://www-iris-rutgers-edu.proxy.libraries.rutgers.edu'
               '/uhtbin/cgisirsi/0/0/0/123')

values = ('?srchfield1=GENERAL^SUBJECT^GENERAL^^words%20anywhere&'
          'searchdata1={ISBN}&library=ALL')

search_RUTGERS = gen_search_in_university(RUTGERS_url, values, 
                     'found no matches in any library', return_found=False)


            

