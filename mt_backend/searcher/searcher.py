from flask import Blueprint,request
from mt_backend.models import Question

searcher = Blueprint('searcher', __name__)



# @searcher.route("/search/<request>",methods = ['GET'])
# def search(request):
#     question = Question.from_get(request)
#     return question.to_json()

@searcher.route("/search",methods = ['POST'])
def search():
    data = request.json
    question = Question(header=data["label"], body=data["querry"])
    return question.to_json()