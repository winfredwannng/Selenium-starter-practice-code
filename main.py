from time import sleep

import testcases.basic.test_user_login
from testcases import testcase1
from testcases import testcase02
from selenium import  webdriver
from util import util
from testcases.basic import test_user_login
from testcases.basic import test_admin_login
from testcases.basic import test_category
from testcases.basic import test_article
from testcases.unittest.test_category import TestCategory

if __name__ == '__main__':
    login = test_admin_login.TestAdminLogin()
    login.test_admin_login_code_ok()
    case = TestCategory(login)
    case.test_add_category_ok()
    # case = test_article.TestArticle(login)
    # #case.test_add_ok()
    # case.test_delete_ok()

    # case = testcases.basic.test_admin_login.TestAdminLogin()
    # case.test_admin_login_code_ok()
    # case = testcases.basic.test_user_login.TestUserLogin()
    # case.test_user_login_username_ok()
    # login = test_admin_login.TestAdminLogin()
    # login.test_admin_login_code_ok()
    # case = test_category.TestCategory(login)
    # case.test_add_category_ok()

