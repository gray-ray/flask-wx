from flask import jsonify


def create_response(code=200,message="success", data = None, success = True): 
  """ 创建统一返回格式
  
  Keyword arguments:
  argument -- description
  Return: JSON响应
  """

  response = {
    "code": code,
    "message": message,
    "data": data,
    "success": success
  }
  return jsonify(response)


  