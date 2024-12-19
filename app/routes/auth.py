
from flask import Flask, request, jsonify, Blueprint, session

from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

import requests

from app.core.create_response import create_response

from datetime import datetime, timedelta, timezone

auth = Blueprint('auth', __name__)

from config import Config

from app.models import db, User, Auth


"""
微信小程序注册/登录
"""
@auth.route('/login', methods=['POST'])
def login():

    data = request.get_json()

    if not data['code']:

        return create_response(message='缺少 code 参数',success=False), 200
 
    url = f"https://api.weixin.qq.com/sns/jscode2session?appid={Config.WX_APPID}&secret={Config.WX_APP_SECRET}&js_code={data['code']}&grant_type=authorization_code"

    response = requests.get(url)

    res = response.json()

    if 'errcode' in res:
        return create_response(message=str(res),success=False) , 200
    
    openid = res['openid']
    session_key = res['session_key']
    expires_at = res["expires_in"]

    # 自定义登录态（使用 openid 生成 JWT Token）
    access_token = create_access_token(identity={'openid': openid})

    user= db.session.query(User).filter_by(openid=openid).first()
    
    if not user:
        user = User(openid=openid, nickname=data['nickname'] ,avatar=data['avatar'])
        db.session.add(user)
        db.session.commit()

    token_entry =  db.session.query(Auth).filter_by(user_id=user.id).first()

   
    if token_entry: 
        token_entry.token = access_token
        token_entry.expires_at = expires_at
        db.session.commit()
    else:
        state = Auth(user_id = user.id, token = access_token,expires_at =expires_at)
        db.session.add(state)
        db.session.commit()
   
    return create_response(message="登录成功", data={"token": access_token }) 



"""退出登录

"""
@auth.route('/logout', methods=['POST'])
# 需要登录的token
@jwt_required()
def logout():
    current_user = get_jwt_identity()

    openid = current_user.get("openid")

    user = User.query.filter_by(openid=openid).first()

    if not user: 
       return  create_response(message="用户不存在", success=False),200
    
    auth_entry = Auth.query.filter_by(user_id= user.id).first()

    db.session.delete(auth_entry)

    db.session.commit()

    return create_response(message="退出登录成功", success=True),200