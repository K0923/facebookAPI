'''
Author: your name
Date: 2022-01-11 10:39:12
LastEditTime: 2022-01-11 10:39:36
LastEditors: your name
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \facebook-python-business-sdk\SAMPLE_CODE.py
'''
# Copyright 2014 Facebook, Inc.

# You are hereby granted a non-exclusive, worldwide, royalty-free license to
# use, copy, modify, and distribute this software in source code or binary
# form for use in connection with the web services and APIs provided by
# Facebook.

# As with any software that integrates with the Facebook platform, your use
# of this software is subject to the Facebook Developer Principles and
# Policies [http://developers.facebook.com/policy/]. This copyright notice
# shall be included in all copies or substantial portions of the software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adrule import AdRule
from facebook_business.api import FacebookAdsApi

access_token = 'EABAZCTrWFQCoBAKtR5ZAN959SX830qZBqCrHDiXiqcqge4Rz9i3ZC0ZABxbpOhZBivTYrPBZBZBegeriUu5625AQvG8qCWIelbiFp4OhQnyajiDfAcRovydCZCSMZB5NSdoODYFMcP5nmGiK7eHbIIpSe4ez8ugZAuM894toUVobz0ZCsodVJtjZCDPRZATNFIZCDmRKyoZD'
app_secret = 'b745472e1416ba556f02d88af0c39559'
ad_account_id = 'act_3148730582014460'
entity_type = 'CAMPAIGN'
filter_field = 'impressions'
filter_value = '1'
filter_operator = 'GREATER_THAN'
app_id = '4573206912778282'
FacebookAdsApi.init(access_token=access_token)

fields = [
]
params = {
    'name': 'Sample SDK Rule',
    'evaluation_spec': {'evaluation_type': 'TRIGGER', 'trigger': { 'type': 'STATS_CHANGE', 'field': filter_field, 'value': filter_value, 'operator': filter_operator }, 'filters': [ { 'field': 'entity_type', 'value': entity_type, 'operator': 'EQUAL' }, { 'field': 'time_preset', 'value': 'LIFETIME', 'operator': 'EQUAL' } ]},
    'execution_spec': { 'execution_type': 'PING_ENDPOINT', },
}
print(AdAccount(ad_account_id).create_ad_rules_library(
    fields=fields,
    params=params,
))


