def page_leads_to_outclick(access_log, page_input, page_output = '/outclick'):
  # implementation goes here
  users = {}
  flows = {}
  success_user = 0
  target_user = 0
  for log in access_log:
    user = log.get("ip")
    page = log.get("url")
    if user in users:
      users[user].append(page)
    else:
      users[user] = [page]
    if page_output in users[user] and page_input in users[user]:
      target_user +=1
    if page_output in users[user]:
      success_user +=1
  return (target_user / success_user) *100

import unittest

class Test(unittest.TestCase):
    access_log = [
        {
            "ip": "1.2.3.1",
            "datetime": "07/Sept/2017:16:05:49 -0500",
            "url": "/"
        },
        {
            "ip": "1.2.3.2",
            "datetime": "07/Sept/2017:16:05:50 -0500",
            "url": "/"
        },
        {
            "ip": "1.2.3.3",
            "datetime": "07/Sept/2017:16:05:51 -0500",
            "url": "/"
        },
        {
            "ip": "1.2.3.4",
            "datetime": "07/Sept/2017:16:05:52 -0500",
            "url": "/"
        },
        {
            "ip": "1.2.3.5",
            "datetime": "07/Sept/2017:16:05:53 -0500",
            "url": "/"
        },
        {
            "ip": "1.2.3.6",
            "datetime": "07/Sept/2017:16:05:54 -0500",
            "url": "/"
        },
        {
            "ip": "1.2.3.7",
            "datetime": "07/Sept/2017:16:05:55 -0500",
            "url": "/"
        },
        {
            "ip": "1.2.3.8",
            "datetime": "07/Sept/2017:16:05:56 -0500",
            "url": "/"
        },
        {
            "ip": "1.2.3.4",
            "datetime": "07/Sept/2017:16:05:57 -0500",
            "url": "/page1"
        },
        {
            "ip": "1.2.3.4",
            "datetime": "07/Sept/2017:16:05:58 -0500",
            "url": "/page2"
        },
        {
            "ip": "1.2.3.4",
            "datetime": "07/Sept/2017:16:05:59 -0500",
            "url": "/page1"
        },
        {
            "ip": "1.2.3.4",
            "datetime": "07/Sept/2017:16:06:00 -0500",
            "url": "/outclick"
        },
        {
            "ip": "1.2.3.1",
            "datetime": "07/Sept/2017:16:06:01 -0500",
            "url": "/page1"
        },
        {
            "ip": "1.2.3.1",
            "datetime": "07/Sept/2017:16:06:02 -0500",
            "url": "/page3"
        },
        {
            "ip": "1.2.3.1",
            "datetime": "07/Sept/2017:16:06:03 -0500",
            "url": "/outclick"
        },
        {
            "ip": "1.2.3.5",
            "datetime": "07/Sept/2017:16:06:04 -0500",
            "url": "/page2"
        },
        {
            "ip": "1.2.3.5",
            "datetime": "07/Sept/2017:16:06:05 -0500",
            "url": "/page1"
        },
        {
            "ip": "1.2.3.5",
            "datetime": "07/Sept/2017:16:06:06 -0500",
            "url": "/outclick"
        },
        {
            "ip": "1.2.3.6",
            "datetime": "07/Sept/2017:16:06:07 -0500",
            "url": "/page2"
        },
        {
            "ip": "1.2.3.8",
            "datetime": "07/Sept/2017:16:06:08 -0500",
            "url": "/page3"
        }]

    def test_page2(self):
        self.assertEqual(page_leads_to_outclick(self.access_log, '/page2', '/outclick'), (2/3 * 100))
