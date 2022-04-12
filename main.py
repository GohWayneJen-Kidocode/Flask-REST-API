from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(name = {name}, views = {views}, likes = {likes}"

#cdb.create_all()

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="The name of the video is required", required=True)
video_put_args.add_argument("views", type=int, help="The amount views on the video is required", required=True)
video_put_args.add_argument("likes", type=int, help="The amount likes on the video is required", required=True)

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="The name of the video is required")
video_update_args.add_argument("views", type=int, help="The amount views on the video is required")
video_update_args.add_argument("likes", type=int, help="The amount likes on the video is required")

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.String,
    'likes': fields.String
}

class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Video with that ID could not be found.")
        return result

    @marshal_with(resource_fields)
    def put(self, video_id):
        args = video_put_args.parse_args()
        video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])    
        if video:
            abort(409, message="This video id has already been taken.")
        db.session.add(video)
        db.session.commit()
        return video, 201

    @marshal_with(resource_fields)
    def patch(self, video_id):
        args = video_update_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Your video could not be found and cannot be updated.")
        if args['name']:
            result.name = args['name']
        if args['views']:
            result.views = args['views']
        if args['views']:
            result.likes = args['likes']
    
        db.session.commit()
        return result

    def delete(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="This video does not exist and cannot be deleted")
        del result[video_id]
        return '', 204

api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)

#took like an hour to do all this code and delete b4 commit pls maofjsdnbhlofj