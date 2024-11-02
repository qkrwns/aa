from ..models import Lost
from ..models import Chatting, db
from flask import Flask, Blueprint, url_for, request
import json
from ..encoder import AlchemyEncoder
from datetime import datetime

bp = Blueprint('main', __name__, url_prefix='/')

@bp.get('/losts')
def index_lost():
    lost_list = Lost.query.order_by(Lost.lost_date.desc()).all()
    res = json.dumps(lost_list, cls=AlchemyEncoder)
    return res

@bp.get('/losts/<int:lost_id>')
def detail(lost_id):
    lost=Lost.query.get(lost_id)
    res = json.dumps(lost, cls=AlchemyEncoder)
    return res

@bp.get('/losts/<int:lost_id>/chattings')
def detail_chattings(lost_id):
    lost=Lost.query.get(lost_id)
    chatting_list = Chatting.query.filter_by(lost_id=lost_id).all()
    isMaster = True
    args = request.args
    password = args['password']
    if lost.password != password:
        isMaster =  False
    if isMaster == False:
        for chatting in chatting_list:
            chatting.type = 3-chatting.type
    res = json.dumps(chatting_list, cls=AlchemyEncoder)
    return res

@bp.post('/losts')
def create_lost():
    res = request.json
    bicycle = res['bicycle']
    location = res['location']
    content = res['content']
    lost_date = res['lost_date']
    lost_time = datetime.strptime(lost_date, '%Y-%m-%dT%H:%M')
    password = res['password']
    lost = Lost(bicycle=bicycle, location=location, content=content, lost_date=lost_time, password=password)

    db.session.add(lost)
    db.session.commit()

    return { "success": True}

@bp.get('/chattings')
def index():
    chatting_list = Chatting.query.order_by(Chatting.desc()).all()
    res = json.dumps(chatting_list, cls=AlchemyEncoder)
    return res

@bp.post('/chattings/<int:lost_id>')
def create(lost_id):
    lost = Lost.query.get_or_404(lost_id)
    res = request.json
    content = res['content']
    password = res['password']
    if lost.password == password:
        type = 1
    else:
        type = 2

    #lost_id = 1
    print(res)
    chatting =Chatting(content=content, type=type, lost_id=lost_id)
    
    db.session.add(chatting)
    db.session.commit() 
    
    return { "success": True}


