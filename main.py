from flask import Flask, render_template, make_response, session, request
from flask_cors import cross_origin
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length
from io import BytesIO
import ver_code as vc
import func

app = Flask(__name__)
sKey = "8848"  # 操作校验key
page_settings = {
	"title": "核自易查通",
	"CopyRight": "MrDeng",
	"name": "四级模考成绩",
	"webUrl": "https://github.com/Lord2333/flask_search",
	"code": 0,
	"notice": "请输入你的学号进行查询~"
}


class SearchForm(FlaskForm):
	search_key = StringField('查询条件', validators=[DataRequired(str), Length(1, 64)],
	                         render_kw={'type': "text", 'class': "txts", 'id': "name", 'placeholder': u"请输入查询条件",
	                                    'style': "border-radius: 5px"})
	verify_code = StringField('验证码', validators=[DataRequired(), Length(1, 4)],
	                          render_kw={'type': "text", 'class': "txts", 'id': "code", 'placeholder': u"请输入验证码",
	                                     'style': "border-radius: 5px"})


#  首页路由
@app.route("/", methods=['get', 'post'])
@cross_origin()
def home_page():
	form = SearchForm()
	if request.method == 'GET':
		return render_template('./index.html', page_settings=page_settings, form=form)
	else:
		if form.is_submitted():
			verify_code = form.verify_code.data
			if session.get('image').lower() != verify_code.lower():
				page_settings['code'] = 1
				return render_template('./index.html', page_settings=page_settings, form=form)
			else:
				search_key = form.search_key.data
				datas = func.Search(search_key)
				return render_template('./result.html', page_settings=page_settings, data=datas)
		return '000'


#  数据库更新操作接口
@app.route("/update" + sKey)
def update():
	...


@app.route('/ver_code')
def get_code():
	image, code = vc.get_verify_code()
	# 图片以二进制形式写入
	buf = BytesIO()
	image.save(buf, 'jpeg')
	buf_str = buf.getvalue()
	# 把buf_str作为response返回前端，并设置首部字段
	response = make_response(buf_str)
	response.headers['Content-Type'] = 'image/gif'
	# 将验证码字符串储存在session中
	session['image'] = code
	return response


if __name__ == "__main__":
	app.config['SECRET_KEY'] = '8848'
	app.run(debug=True, port=8848)  # 使项目以debug方式运行
