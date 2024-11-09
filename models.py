#from . import db
from . import db
# 모델 만들었으니까, 이제 분실목록 등록, 삭제, 조회하는 API를 만들어야돼

class Lost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bicycle = db.Column(db.String(200), nullable=False)
    lost_date = db.Column(db.DateTime(), nullable=False)
    location = db.Column(db.String(200), nullable = False)
    content = db.Column(db.Text(), nullable=False)
    password = db.Column(db.String(), nullable=False)
    lat = db.Column(db.Double(), nullable=False)
    lng = db.Column(db.Double(), nullable=False)

class Chatting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text(), nullable=False)
    type = db.Column(db.Integer, nullable=False)
    
    lost_id = db.Column(db.Integer, db.ForeignKey('lost.id', ondelete='CASCADE'))
    lost = db.relationship('Lost', backref=db.backref('chatting_set'))
