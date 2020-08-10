from flask import Flask, render_template, request, Response
import requests
from better_profanity import profanity
import json
# from chat import bott

app=Flask(__name__)

@app.route('/')
def hello():
  return render_template('bot.html')

@app.route('/response', methods=['GET','POST'])
def resp():
  msg = request.form.get('msg')
  res = bott.my_bot.get_response(msg)
  return render_template('botresponse.html',reply=res)

@app.route('/predict/<text>', methods=['GET'])
def predict(text):
    prof=profanity.censor(text)
    return prof

@app.route('/profa', methods=['POST','GET'])
def profa():
  custom_badwords=["aand", "aandu", "balatkar", "beti chod", "bhadva", "bhadve", "bhandve", "bhootni ke", "bhosad", "bhosadi ke", "boobe", "chakke", "chinaal", "chinki", "chod", "chodu", "chodu bhagat", "chooche", "choochi", "choot", "choot ke baal", "chootia", "chootiya", "chuche", "chuchi", "chudai khanaa", "chudan chudai", "chut", "chut ke baal", "chut ke dhakkan", "chut maarli", "chutad", "chutadd", "chutan", "chutia", "chutiya", "gaand", "gaandfat", "gaandmasti", "gaandufad", "gandu", "gashti", "gasti", "ghassa", "ghasti", "harami", "haramzade", "hawas", "hawas ke pujari", "hijda", "hijra", "jhant", "jhant chaatu", "jhant ke baal", "jhantu", "kamine", "kaminey", "kanjar", "kutta", "kutta kamina", "kutte ki aulad", "kutte ki jat", "kuttiya", "loda", "lodu", "lund", "lund choos", "lund khajoor", "lundtopi", "lundure", "maa ki chut", "maal", "madar chod", "mooh mein le", "mutth", "najayaz", "najayaz aulaad", "najayaz paidaish", "paki", "pataka", "patakha", "raand", "randi", "saala", "saale", "saala kutta", "saali kutti", "saali randi", "suar", "suar ki aulad", "tatte", "tatti", "teri maa ka bhosada", "teri maa ka boba chusu", "teri maa ki chut", "tharak", "tharki","Aai ghalya", "Aye Jhaatu", "Badak Zawarya", "Bhadavya", "Bhikaar Chot", "Bin gotyaachya", "Bulli chokya", "Chinaal maichya", "Chut Marichya", "Foknicha", "Gand khaya", "Gandit Ghuslo", "Gandoo", "Jhavadya", "Laudu", "Lavadya", "Muttha", "Paadar Gandichya", "Phodree Pisat", "Raandichya", "Shebnya", "Telkat Randi", "Tuji aiee chi gaand", "Tuzya aai chi Phodree", "Tuzya aii zavneya tuzya baapla", "Tuzya bapacha pay adakla sandasat.", "Yeda lavdya", "aai chi gand", "aai javada", "aaichya gavat pay", "ai zawlee", "akkar mashi", "ayica dana", "chinal", "chut marichya", "fodri pisaat", "fokanchidy", "khargatya gandicha", "lal gandya", "madarchod", "madarchoth", "pachi bota bhundyat", "phodarphatya", "puchi", "shattya", "tondaat gay", "tujha aila kutryawani zawin", "tuji ai mutli madkyat phala-phala", "tuza baap dhandewala", "tuzi aai padli madkyat", "tuzi aai padli tuzya tondat", "tuzua aaichi pucchi viskatli 40 ekrat", "tuzya aaicha foda", "tuzya aaicha lavda", "tuzya aaichi gand", "tuzya aaichi pucchi", "tuzya aaichya gandit mungya", "tuzya aaichya pucchila chavla kutra", "tuzya aaichya pucchila chavla sap", "tuzya aaila zavla kala kutra", "yadzavya", "zavadya", "zavnya"]
  profanity.add_censor_words(custom_badwords)
  ls = request.form['text']
  txt=json.loads(ls)
  res=[]
  for i in txt:
    prof=profanity.censor(i)
    if(i==prof):
      res.append(0)
    else:
      res.append(1)
  '''
  res=txt[0]
  '''
  return Response(json.dumps(res),  mimetype='application/json')

@app.route('/form/<name>')
def form(name):
   return render_template('student.html',name=name)

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'GET':
      result = request.form
      ten=10
      return render_template("result.html",result = result)

if __name__ == '__main__':
   app.run(debug = True)

'''
git add .
git commit -m "deploy 2"
git push heroku master

from chat import bott
bott.my_bot.get_response('तुमचा दिवस कसा होता')

  msg = request.form.get('msg')
  #res=bott()
  #msg='नाव काय आहे ?'
  my_bot = ChatBot(name='PyBot', read_only=True,
                   logic_adapters=['chatterbot.logic.MathematicalEvaluation',
                                   'chatterbot.logic.BestMatch'])
  small_talk = ['तुझं नाव काय','रामराम मी बंड्या',
                'तू कसा','मी ठीक आहे',
                'वेळ काय','वेळ बराच उशीर झाला आहे',
                'सूर्य उगवतो','सूर्य पुर्वेकडे उगवतो',
                'राहण्यासाठी सर्वोत्तम शहर','मुंबई',
                'भारताची राजधानी काय','भारताची राजधानी दिल्ली आहे',
                'दररोज एक आहे?','नवीन दिवस']
  small_talk2=['तुमचा दिवस कसा होता','माझा दिवस चांगला होता',
                'आवडता विषय कोणता','NLP माझा आवडता विषय आहे']
  list_trainer = ListTrainer(my_bot)
  for item in (small_talk,small_talk2):
      list_trainer.train(item)
  res = my_bot.get_response(msg)
  return render_template('botresponse.html',reply=res)'''
