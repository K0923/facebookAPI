'''
Author: your name
Date: 2022-01-13 15:47:15
LastEditTime: 2022-01-13 15:59:56
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \facebook-python-business-sdk\create_adset.py
'''

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adset import AdSet
from facebook_business.api import FacebookAdsApi

access_token = 'EAAOCdpZCGu5YBABhzY0XN37HqFnkTGZASYWoTHZCSnP8V8RECyZC3hI2Y1PU00AKOs5DpyKdNLTXrAStB3DmBZAY7P0bBmHoMchkQGcxeuvFvii9hGoOjSpvmYZBtNW3WEvBITYzKDNPqTI7hB6R4ZBAnELuO9EDqwbN07EuZAZCiLFicfeTytspKIGYR5lwEsp5sVXwxKOqaAyPLouiMV0KEHuIZB8Po5s9E8DLARxnGnrLZBMwKGPX3DIj280jDJtftAZD'
app_secret = '3f6fbbe32d077aee53d4ca368bfa90dd'
app_id = '227548106118318'
id = 'act_4509794559124620'
FacebookAdsApi.init(access_token=access_token)

fields = [
]
params = {
  'name': 'My Reach Ad Set',
  'optimization_goal': 'REACH',
  'billing_event': 'IMPRESSIONS',
  'bid_amount': '2',
  'daily_budget': '1000',
  'campaign_id': '23849537065280019',
#   'targeting':{"geo_locations": {"countries":["US"]}, "interests": [{id: 6003139266461, 'name': 'Movies'}]},
  'targeting': {'geo_locations':{'countries':['US']},'facebook_positions':['feed'], "geo_locations": {"countries":["US"]}, "interests": [{"id": 6003139266461, 'name': 'Movies'}]},
  'status': 'PAUSED',
#   'promoted_object': {'page_id':'<pageID>'},
  'start_time': '2021-12-06T04:45:17+0000'
}
print(AdAccount(id).create_ad_set(
  fields=fields,
  params=params,
))

