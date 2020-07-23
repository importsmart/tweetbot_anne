import tweepy

api_key = ""
sec_api_key = ""

token = ""
sec_token = ""

auth = tweepy.OAuthHandler(api_key, sec_api_key)
auth.set_access_token(token, sec_token)

api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)
    
l = open("letter.txt", "r")
text = l.read()

i = open("iter.txt", "r+")
start = int(i.read())

text = text[start:start+280]
lettext = text.split('\l')[0]

txt = lettext.split('\n')
txtlen = len(txt)
txt = ' '.join(txt[:txtlen-1])

totlen = len(txt)
i.seek(0)

if len(text.split('\l')) > 1:
	i.write(str(start + totlen + 4))
else:
	i.write(str(start + totlen + 1))

l.close()
i.close()
    
api.update_status(txt)
