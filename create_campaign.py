'''
Author: your name
Date: 2022-01-10 15:23:10
LastEditTime: 2022-01-12 20:38:42
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \facebook-python-business-sdk\test.py
'''

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.api import FacebookAdsApi

access_token = 'EAADO9CwI1K4BAA8bdtgPRAkS5D4BVWAcOkDGK15cQ337ZBGFMVwFKsslbHZC9pdlNqypQdKmk4p3SRsIAYWHQVVZASwgiApd5fLrv7K5ZC7SxzmcRCt9SW8TRHAu5396XqhpLH5uTK216NdG5XpZAwxXNK6AQZC7sAhP7DQ4TfwPtVo3y7dqJGAtOiwpojA1aUmAtl7eeq1RtYPZAgL2p3KIqZCF40pZB1DSfZBMUtRUN6cNuyvWhDn2TZAvjfNL0ktWzIZD'
app_secret = '3f6fbbe32d077aee53d4ca368bfa90dd'
app_id = '227548106118318'
id = 'act_4509794559124620'
FacebookAdsApi.init(access_token=access_token)

fields = [
]
params = {
  'name': 'My campaign',
  'objective': 'LINK_CLICKS',
  'status': 'PAUSED',
  'special_ad_categories': [],
}
print(AdAccount(id).create_campaign(
  fields=fields,
  params=params,
))

