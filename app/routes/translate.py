from flask import Blueprint
from flask import request,jsonify
from app.core.create_response import create_response

translate = Blueprint('translate', __name__)


from tencentcloud.common.common_client import CommonClient
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile

from config import Config

# 更新
@translate.route('/', methods=['POST'])
def transLateStr():
    try:
      cred = credential.Credential(Config.TENCENT_CLOUD_APPID, Config.TENCENT_CLOUD_SECRET)
    
      httpProfile = HttpProfile()
      httpProfile.endpoint = "tmt.tencentcloudapi.com"
      clientProfile = ClientProfile()
      clientProfile.httpProfile = httpProfile

      data = request.get_json()

      common_client = CommonClient("tmt", "2018-03-21", cred, "ap-beijing", profile=clientProfile)

      data['ProjectId'] = 0

      res = common_client.call_json("TextTranslate",data)


      return  create_response(message='成功', success=True, data=res['Response']), 200
    
    except TencentCloudSDKException as err:
      print(err)
      return  create_response(message=jsonify(err), success=False, data=None), 400
       
  



 