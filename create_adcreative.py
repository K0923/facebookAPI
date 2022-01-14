'''
Author: your name
Date: 2022-01-13 20:11:05
LastEditTime: 2022-01-13 20:11:05
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \facebook-python-business-sdk\create_adcreative.py
'''


from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adcreative import AdCreative
from facebook_business.api import FacebookAdsApi

access_token = 'EAAOCdpZCGu5YBAKnFmwSuZCaaIs8kd4W7x42lDm3ZBLm8NrU0PqNIDzUtwImxd4BPzkG05eQLVRs1wTXG0fyEUMl5Qyw5DC0Yq9gNDOOsfgsOD177lh9TQDetXhfZBuKeKDPGIqU6xzhyIfF3mSZB1uqWgnZB5Cbi4oZCRJdfl2IXWTpkVuLZBRtflRFtR43WnF65yQija92K0fs87XhZAErbDwJPpnVcax8bqAsyccoYhb9GfqrodRXT6bKO2CZAIOZAAZD'
app_secret = '3f6fbbe32d077aee53d4ca368bfa90dd'
app_id = '227548106118318'
id = 'act_4509794559124620'
FacebookAdsApi.init(access_token=access_token)

fields = [
]
params = {
  'name': 'Sample Creative',
  'object_story_spec': {'page_id':'100272569225581','link_data':{'link':'https:\/\/facebook.com\/100272569225581','message':'try it out'}},
}
print (AdAccount(id).create_ad_creative(
  fields=fields,
  params=params,
))

