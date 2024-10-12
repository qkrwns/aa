from ..models import Lost
from ..models import Chatting
from flask import Blueprint, url_for, request
import json
from ..encoder import AlchemyEncoder
from datetime import datetime
from werkzeug.utils import redirect
from .. import db

bp = Blueprint('main', __name__, url_prefix='/')

@bp.get('/losts')
def index():
    lost_list = Lost.query.order_by(Lost.lost_date.desc()).all()
    res = json.dumps(lost_list, cls=AlchemyEncoder)
    return res
    
@bp.get('/losts/<int:lost_id>')
def detail(lost_id):
    lost=Lost.query.get(lost_id)
    res = json.dumps(lost, cls=AlchemyEncoder)
    return res

@bp.post('/losts')
def create():
    bicycle = request.form['bicycle']
    content = request.form['content']
    lost_date = datetime.now()
    lost = Lost(bicycle=bicycle, content=content, lost_date=lost_date)

    db.session.add(lost)
    db.session.commit()

    return { "success": True}

@bp.get('/chattings')
def index():
    chatting_list = Chatting.query.order_by(Chatting.desc()).all()
    res = json.dumps(chatting_list, cls=AlchemyEncoder)
    return res

@bp.post('/chattings')
def create():
    content = request.form['content']
    type = request.form['type']
    lost_id = 1
    chatting =Chatting(content=content, type=type, lost_id=lost_id)
    
    db.session.add(Chatting)
    db.session.commit() 