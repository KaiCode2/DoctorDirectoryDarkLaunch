from flask import Flask, jsonify




DATA = [
    {
    'name': 'asthma',
    'catergory': 'respiratory',
    'description': 'lorem ipsum',
    'link': 'http://www.cfpc.ca/uploadedFiles/Resources/_PDFs/Asthma2014_EN.pdf'
    },
    {
    'name': 'breast cancer',
    'catergory': 'cancer',
    'description': 'lorem ipsum',
    'link': 'http://www.cfpc.ca/uploadedFiles/Resources/Resource_Items/Patients/BreastCancer_EN.pdf'
    },
    {
    'name': 'depression',
    'catergory': 'mental illness',
    'description': 'lorem ipsum',
    'link': 'http://www.cfpc.ca/ProjectAssets/Templates/Resource.aspx?id=3707'
    }
]




DEBUG = True
PORT = 8000
HOST = '0.0.0.0'

app = Flask(__name__)
app.secret_key = 'adLSKHfailuSHBdiscilhgdlfahiuwedscn,zishelfahweif;hcxz.vihaw'

@app.errorhandler(404)
def page_not_found(error):
    return '404: Page not found'

@app.route('/all')
def all():
	return jsonify(header='handouts', results=DATA)

@app.route('/<illness>')
def route(illness):
    for entry in DATA:
        if entry['name'] == illness:
            return jsonify(header='results', results=entry)
    return page_not_found(404)


if __name__ == '__main__':
	app.run(host=HOST, port=PORT)
