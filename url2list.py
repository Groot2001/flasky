# coding=utf-8

import urllib.request
from werkzeug.routing import BaseConverter

class ListConverter(BaseConverter):
    def __init__(self,url_map,separator='+'):
        super(ListConverter, self).__init__(url_map)
        self.separator=urllib.request.unquote(separator)

    #自定义转换器需要继承自BaseConverter,且实现to_python和to_url两个方法
    def to_python(self, value):
        return value.split(self.separator)
    def to_url(self, values):
        values2list=[super(BaseConverter,self).to_url(value) for value in values]
        #print('1111{}'.format(self.separator.join(super(BaseConverter,self).to_url(value) for value in values)))
        return self.separator.join(values2list)

if __name__=='__main__':
    '''
    url_list=ListConverter('www.baidu.com','+')
    print('urllist: {}'.format(url_list.separator))
    '''
    pass
