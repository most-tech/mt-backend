from flask import Blueprint
from mt_backend.models import Question

searcher = Blueprint('searcher', __name__)



@searcher.route("/search/<request>",methods = ['GET'])
def search(request):
    question = Question.from_get(request)
    return question.to_json()