import json
import time

def iterate(num, browser):
    ''' LOADS ALL THE SUPRRESSED ID's INTO A LIST '''
    id_list = []
    for page in range(1,num + 1):
        link = "https://gem.godaddy.com/suppressed_audience_members.json?page=" + str(page) +  "&list_id=suppressed"
        site = browser.get(link)
        unformatted_json = browser.find_element_by_tag_name("pre").text
        clean_json = json.loads(unformatted_json)
        results = clean_json["result"]["audience"]
        for res in results:
            id_list.append(res['id'])
    return id_list

def unsubscribe(user, browser, cookies):
    ''' TAKE IN AN ID THEN UNSUBSCRIBE VIA SELENIUM CLICKS '''
    link = "https://gem.godaddy.com/audience_members/" + str(user)
    browser.get(link)
    browser.find_element_by_class_name("accepted").click()
    time.sleep(1)
    browser.find_element_by_xpath("/html/body/div[2]/div[3]/div/footer/form/p/span[2]/button/span").click()
