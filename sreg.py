#!/usr/bin/env python
# encoding: utf-8
# author: ff0000team
# website: buzz.beebeeto.com


import sys
import glob
import json
import chardet
import requests
import urlparse
import argparse
import threadpool as tp

from common.color import inBlue, inRed
from common.color import inWhite, inGreen, inYellow
from common.output import output_init, output_finished, output_add

THREADS_NUM = 10

def check(plugin, passport, passport_type):
    '''
    plugin: *.json
    passport: username, email, phone
    passport_type: passport type
    '''
    requests.packages.urllib3.disable_warnings()
    if plugin["request"]["{}_url".format(passport_type)]:
        url = plugin["request"]["{}_url".format(passport_type)].format(passport)
    else:
        return
    app_name = plugin['information']['name']
    category = plugin["information"]["category"]
    website = plugin["information"]["website"]
    judge_yes_keyword = plugin['status']['judge_yes_keyword']
    judge_no_keyword = plugin['status']['judge_no_keyword']
    headers = {
                'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
                'Host': urlparse.urlparse(url).netloc,
                'Referer': url,
                }
    if plugin['request']['method'] == "GET":
        try:
            content = requests.get(url, headers=headers, timeout=8, verify=False).content
            content = unicode(content, "utf-8")
        except Exception, e:
            print inRed('\n[-] %s ::: %s\n' % (app_name, str(e)))
            return
        if judge_yes_keyword in content and judge_no_keyword not in content:
            print u"[{}] {}".format(category, ('%s (%s)' % (app_name, website)))
            icon = plugin['information']['icon']
            desc = plugin['information']['desc']
            output_add(category, app_name, website, passport, passport_type, icon, desc)
        else:
            pass
    elif plugin['request']['method'] == "POST":
        post_data = plugin['request']['post_fields']
        flag = 0
        # if post_data.values().count("") == 1:
        for k, v in post_data.iteritems():
            if v == "":
                post_data[k] = passport
                flag += 1
            elif "{}" in v:
                post_data[k] = v.format(str(passport))
                flag += 1
        if flag < 1:
            print "[-] The POST field can only leave a null value or {}. (%s)" % app_name
            return
        try:
            content = requests.post(url, data=post_data, headers=headers, timeout=8, verify=False).content
            encoding = chardet.detect(content)["encoding"]
            if encoding is None:
                encoding = "utf-8"
            content = unicode(content, encoding)
        except Exception, e:
            print inRed('\n[-] %s ::: %s\n' % (app_name, str(e)))
            return
        if judge_yes_keyword in content and judge_no_keyword not in content:
            print u"[{}] {}".format(category, ('%s (%s)' % (app_name, website)))
            icon = plugin['information']['icon']
            desc = plugin['information']['desc']
            output_add(category, app_name, website, passport, passport_type, icon, desc)
        else:
            pass
    else:
        print u"{}:::Error!".format(plugin['request']['name'])


def main():
    reload(sys)
    sys.setdefaultencoding("utf-8")
    parser = argparse.ArgumentParser(description="Check how many Platforms the User registered.")
    parser.add_argument("-u", action="store", dest="user")
    parser.add_argument("-e", action="store", dest="email")
    parser.add_argument("-c", action="store", dest="cellphone")
    parser_argument = parser.parse_args()
    banner = '''
     .d8888b.
    d88P  Y88b
    Y88b.
     "Y888b.  888d888 .d88b.  .d88b.
        "Y88b.888P"  d8P  Y8bd88P"88b
          "888888    88888888888  888
    Y88b  d88P888    Y8b.    Y88b 888
     "Y8888P" 888     "Y8888  "Y88888
                                  888
                             Y8b d88P
                              "Y88P"
    '''
    all_argument = [parser_argument.cellphone, parser_argument.user, parser_argument.email]
    plugins = glob.glob("./plugins/*.json")
    print inGreen(banner)
    print '[*] App: Search Registration'
    print '[*] Version: V1.0(20150303)'
    print '[*] Website: buzz.beebeeto.com'
    file_name = ""
    if all_argument.count(None) != 2:
        print '\nInput "-h" view the help information.'
        sys.exit(0)
    if parser_argument.cellphone:
        print inRed('\n[+] Phone Checking: %s\n') % parser_argument.cellphone
        file_name = "cellphone_" + str(parser_argument.cellphone)
        output_init(file_name, "Phone: ", str(parser_argument.cellphone))
    if parser_argument.user:
        print inRed('\n[+] Username Checking: %s\n') % parser_argument.user
        file_name = "user_" + str(parser_argument.user)
        output_init(file_name, "UserName: ", str(parser_argument.user))
    if parser_argument.email:
        print inRed('\n[+] Email Checking: %s\n') % parser_argument.email
        file_name = "email_" + str(parser_argument.email)
        output_init(file_name, "E-mail: ", str(parser_argument.email))
    _args = []
    for plugin in plugins:
        with open(plugin) as f:
            try:
                content = json.load(f)
            except Exception, e:
                print e, plugin
                continue
        if parser_argument.cellphone:
            _args.append((([content, unicode(parser_argument.cellphone, "utf-8"), "cellphone"]), {}))
        elif parser_argument.user:
            _args.append((([content, unicode(parser_argument.user, "utf-8"), "user"]), {}))
        elif parser_argument.email:
            _args.append((([content, unicode(parser_argument.email, "utf-8"), "email"]), {}))
    pool = tp.ThreadPool(THREADS_NUM)
    reqs = tp.makeRequests(check, _args)
    [pool.putRequest(req) for req in reqs]
    pool.wait()
    output_finished(file_name)


if __name__ == '__main__':
    main()
