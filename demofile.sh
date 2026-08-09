
mkdir templates 
python3 scaffold.py textbox forme ombre user_id:references
python3 scaffold.py image forme user_id:references
python3 scaffold.py words content user_id:references
python3 scaffold.py user username country_id:references email password phone
python3 scaffold.py country name
python3 scaffold.py stuff name color form size user_id:references
python3 scaffold.py picturetotext pic:file description user_id:references
python3 scaffold.py texttospeech text speech
