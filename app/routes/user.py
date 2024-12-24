from flask import Blueprint
from flask import request, jsonify
user = Blueprint('user', __name__)

from app.models import db, User



# 更新
@user.route('/update', methods=['POST'])
def update():
    data = request.get_json()

    user = db.get_or_404(User,data['id'] )

    user.avatar = data['avatar'] or user.avatar

    user.nickname = data['nickname'] or user.nickname


    db.session.commit()

    return  jsonify({'message': 'User update successfully!'}), 200

# 删除
@user.route('/delete', methods=['GET'])
def delete():
    id = request.args.get('id')

    user = db.get_or_404(User,id )

    db.session.delete(user)

    db.session.commit()

    return  jsonify({'message': 'User deleted successfully!'}), 200


# 详情
@user.route('/getOne',  methods=['GET'])
def getOne():
    id = request.args.get('id')

    user = db.get_or_404(User,id)

    return  jsonify(user.to_dict()), 200

# 所有数据
@user.route('/all',  methods=['POST'])
def getAll():
    
    data = request.get_json()

    username = data.get('username')

    email = data.get('email')

    # 开始查询
    query = User.query
    
    # 根据条件动态添加过滤
    if username:
        query = query.filter(User.username.like(f"%{username}%"))
    if email:
        query = query.filter(User.email.like(f"%{email}%"))

    users = query.all()

        
    list= [user.to_dict() for user in users]
    
    return  jsonify(list), 200