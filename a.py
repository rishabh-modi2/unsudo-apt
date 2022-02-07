import praw, os, random, requests, config#, emojis, regex
from time import sleep
#import word

reddit = praw.Reddit(
    client_id="EiSoo9sHoXzHxgyJYSktkw",
    client_secret="fKWTPLAtQF9ljLbQhPRMDvypcMbIag",
    user_agent="z",
    username="dusra_acc3",
    password="rishabh2003",
    ratelimit_seconds=900,
)

a1 = "gandu" or "Gandu"
aa1 = "raat kali ek khwab me aayi aur\nsubeh muth ka karan bani\nHo gayi Bakchodi ab ja padhne"
a2 = "dank" or "Dank"
aa2 = "Instagram Is for Lite porno and babu shona. Reddit is for dank aur Dank Gf ki tareh Hai Kam hi milta hai"
a3 = " chutiya " or " chutiyapa "
aa3 = "Duniya se sab chala jayega,,, Par ye chutiyapa nahi jayega"
#a4 = " Dank "
a4 = "valentine" or "Valentine" or "14 feb" or " 14 Feb"
aa4 = "Valentine ek dhokha hai,,,mere liye toh 14 FEB parents day hai,,Mummy papa ki sewa karunga"
#aa4 = "Instagram Is for Lite porno and babu shona. Reddit is for dank."
a5 = " Ram" or "ram"
aa5 ="Jai Shree Ram,Hamare Sath Shri Raghunath To Kis Baat Ki Chinta hogi"
a6 =" modi"
aa6 = "Modi Hai toh Mumkin Hai"
a7 = " yogi"
aa7 = "Up Me BJP HI layenge Aur Kamal Khilayenga"
a8 = " Porn " or " milf " or " Milf "
aa8 = "Porn DEkhna Swasthya KE liye Sehat Wardhak HAi,,Kamzori ke liye 2 ghante Muth Aur 1 ghante gd road jana jroori hai"
a9 = "instagram"
#aa9 = "if the worst app in world rank exist insta will be on the top"
aa9 = "Reddit Instagram Ka baap Hai"
a10 = "chapri"
aa10 = "Mai Bolta hu Chapri Londo ki KTM mujhe dedo aur inka land kaat ke bech do"
a11 = "lawda"
aa11 = "Best Rule of Chad BOY :- Lawda hilao khush raho aur gb road jao"
a12 = "DANK"
aa12 = "DANk gf ki tareh HAi,,, Har post Ma nahi hota"
a13 = "allah"
aa13 = "JAI SHREE RAM"
a14 = " doggy style " or " Doggy style "
aa14 = "Doggy style ka maza Hi alag hai bc"
a15 = " op " or "Op" or "OP" or "oP"
aa15 = "OP BOLTE chaddi Kholte"
a16 = " shark tank " or " Shark tank "
aa16 = "shark tank wale GB Road ki whores ko export karne wale biz. me invest karenge?"
a17 = " rand " or " Rand " or " randi "
aa17 = "GB road jaye hawas ka turant smadhan paye ya fir russian laye aur hume bhi bullaye"
a18 = " porn "
aa18 = "Porn DEkhna Swasthya KE liye Sehat Wardhak HAi,,Kamzori ke liye 2 ghante Muth Aur 1 ghante gd road jana jroori hai"
a19 = " muth " or " Muth "
aa19 = "Best Rule of Chad BOY :- MUTH maro khush raho"
a20 = " gb road "
aa20 = "Best Rule of Chad BOY :- MUTH maro khush raho aur gb road jao"
a21 = " sucide "
aa21 = "bhai Sucide kare Toh mujhe video call kar lena Mujhe live dekhni hai ek baar"
a22 = "gf" or "GF" or "Gf" or "girlfriend" or "Girlfriend"
aa22 = "Stop lying about having a girlfriend on the internet. You never had a girlfriend and will never ever have a girlfriend in future. In fact, You will die alone that too virgin playing PUBG mobile with offline bots."
a23 = "normie" or "Normie" or "noormie"
aa23 = "normie londe haye haye... band karo bhai band karo ye chutiyapa band karo"
a24 = "sex" or "Sex" or "virgin"
aa24 = "Gb road jaye kaali/gulabi chut paye \n aur apni tadap ka turant samadhan paye \n discount ke liye use kare coupon no.  dankmeme69696ganddo"
a25 = "pakistan" or "Pakistan"
aa25 = "I'm not gay but l'm pakistani and honestly I'm not even going to lie sometimes I have fantasies where a big dicked Afghan kidnaps me off the streets of Peshawar and keeps me locked under a staircase on a leash. He feeds me once every day and forces me to wear dresses and makeup and little chastity cages on my penis to humiliate me. I imagine that he slowly degrades me further and further until I have no pride left and then he finally comes up behind me as I sleep on the dirty cracked marble floor and tears my little pink panties that he made me wear straight off of my bussy. I imagine that my weak, starved body feels a jolt of pain as he inserts his monster fucking cock deep into my anus. I moan in a mix of pain and pleasure as he slowly starts pushing and pulling his penis inside my ass. I pretend I don't like it and want him to stop, but secretly I love being his little bussy Twink paki slave. He enjoys himself for a while before my anus gets all warm, he is cumming inside me. He pulls out his huge cock and inserts it straight into my mouth, I gargle on it as he starts humping my mouth. My spit trying desperately to escape my mouth as It starts foaming. He again thrust and thrusts until he cums Inside my mouth, his cum tasting sweet like nectar. I imagine him then at the end slowly dropping the act, calling me his little slave, and cuddling me until I fall asleep, and I imagine myself waking up with a butt plug in my ass, my anus us only for him to use. Can anyone else relate to this?"

a26 = "Gay" or "gay"
aa26 = "Jis tareh gf/londiyo ki kami chal rahi hai Aisa Lagta hai ek din puri duniya gay ban jayegi,,,, Londiya lao be kahi se"
a27 = " akela " or " Akela " or " akelapan " or " dukh "
aa27 = "Padhle Bsdk jake ,, bada aaya akele pan ka gyan chodne wala"
a28 = " chut " or " Chut " or " gand "
aa28 = "Gb road jaye kaali/gulabi chut paye \n aur apni tadap ka turant samadhan paye \n discount ke liye use kare coupon no.  dankmeme69696ganddo"
a29 = "rahul" or "Rahul"
aa29 = "ye sab dogla-pan hai"
a30 = "ashneer" or "Ashneer"
aa30 = "Ye sab dogla pan HAI"
a31 = "hawas" or "Hawas" or "Hawasi" or "hawasi"
aa31 = "Bc duniya ko agar hawasiyo ka sthal kaha jaye toh theek rahega.\nyaha har londa apni gf ke liye hilata hai aur ye log bolte hai **India is Immature for sex-education**"
a32 = "russian"
aa32 = "Russian lao hawas ka instant samadhan pao"
a33 = "ranvijay" or "Ranvijay"
aa33 = "ranvijay:- Ye lijiye humara 2 kodi ka course aur apne aap ko upgrade kijiye"
a34 = "kotha"
aa34 = " kothe ka rate kya chalra hai?"
a35 = "introvert" or "dukh"
aa35 = "mai bhi introvert hu bhai, akela rehna pasand karta hu, akela ho gaya iss puri duniya me mai, jayada friends bhi nahi hai mere, samajh bhi nahi aata apne akelepan se kaise dur hou"
a35 = " bot "
aa35 = "Sala jaha dekho vahi Bots nazar aate hai. aisa lagta hai insaano se jayada bot hai reddit par"
a36 = " navel "
aa36 = "perfect chubby navel konse kothe pe milegi? aaj tak bas navel dekhi hai kabhi touch nahi kari, mai aur mera dukh"
a37 = "bsdk" or "Bsdk" or "bhosdike"
aa37 = "Bsdk ka matlab **Bohot saaf dil ka** hota hai. Ha Bhai Bohot shareef Baccha Hu, Pornhub pe bhi sirf math padhta hu"
a38 = " oyo " or " Oyo " or ' OYO '
aa38 = "HA Bhai Gf ne Grp Studies ke liye oyo me bulaya Hai. Kya matlab condom lekar jau sath me"
a39 = "repost" or "reposter" or "Repost" or "Reposter"
aa39 = "#IndianDankMemes KI Dhara 6969 ke tehet **Repost** Karne wale ka Ling kaat Kar Kutto Ko khila diya jayega\n\n###If this is a repost upvote this comment otherwise reply **oc**"
a40 = "motherfucker" or " mf "
aa40 = "Bhai Ma toh maa hoti hai teri ho meri ho ya kisi aur ki,,aise kisiko gaali nahi dete isse chutiya lodu gandu hijda ... kuch bhi bol de kar mc mat bol"
a41 = "AutoModerator" or "automoderator" or " automod"
aa41 = "Chutiya Sa bot, Sale ko theek se code bhi nahi kara sirf 4-5 word janta hai"
a42 = " bts" or " Bts" or " BTS "
aa42 = "Use **Gay** wprd insted of bts(6kke)"
a43 = "ma chuda" or "maa chuda" or "Maa chuda" or "Maa Chuda"
aa43 = "I am Not a muslim who can fuck own mum and sisters so i can not do this sorry,,,Agar tu apni chudana chahta hai to mera lund taiyar hai"
a44 = "tanmay"
aa44 = "tanamy bhat haye haye"
#s = random.randint(60,600)
def comment():
  s = 0
  with open("reply_comment.txt", "r") as f:
          comments_replied_to = f.read()
          comments_replied_to = f.read()
          comments_replied_to = comments_replied_to.split("\n")
          comments_replied_to = filter(None, comments_replied_to)
  i = 0
  try:
    for comment in reddit.subreddit('IndianDankMemes').stream.comments():
      i += 1
      #print(i, end='\r')
      #print(comment.body, end='\r')
      if i > 105:
#           if comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
#             def split_count(text):

#                 emoji_list = []
#                 data = regex.findall(r'\X', text)
#                 for word in data:
#                     if emoji.is_emoji(word):
#                       comment.reply("emoji detected,, Comment rejected")
#                     if any(char in emoji.UNICODE_EMOJI['en'] for char in word):
#                         emoji_list.append(word)
#                 return emoji_list
#                 counter = split_count(line[0])
#                 print(' '.join(emoji for emoji in counter))
#                 #print(word)
#                 #if emoji.is_emoji(word):
#                 #  comment.reply("emoji detected,, Comment rejected")
#                 #  print("emoji detected")
          if a1 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
            sleep(45)
            comment.reply(aa1)
            #print(comment.id)
            #sleep(s)
            #print(comment.id)
            #print(i)
            comment.upvote()
          if a2 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
            sleep(45)
            comment.reply(aa2)
            #print(comment.id)
            #sleep(s)
            #print(comment.id)
            #print(i)
            comment.upvote()
          if a3 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
            sleep(45)
            comment.reply(aa3)
            #print(comment.id)
            #sleep(s)
            #print(comment.id)
            #print(i)
            comment.upvote()
          if a4 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
            sleep(45)
            comment.reply(aa4)
            #sleep(s)
            #print(comment.id)
            #print(i)
            comment.upvote()
            #print(comment.id)
          if a5 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
            sleep(45)
            comment.reply(aa5)
            #sleep(s)
            #print(comment.id)
            #print(i)
            comment.upvote()
            #print(comment.id)
          if a6 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
            sleep(45)
            comment.reply(aa6)
            #sleep(s)
            #print(comment.id)
            #print(i)
            comment.upvote()
            #print(comment.id)
          if a7 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
            sleep(45)
            comment.reply(aa7)
            #sleep(s)
            #print(comment.id)
            #print(i)
            comment.upvote()
            #print(comment.id)
          if a8 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
            sleep(45)
            comment.reply(aa8)
            #sleep(s)
            #print(comment.id)
            #print(i)
            comment.upvote()
            #print(comment.id)
          if a9 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
            sleep(45)
            comment.reply(aa9)
            #sleep(s)
            #print(comment.id)
            #print(i)
            comment.upvote()
            #print(comment.id)
          if a10 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
            sleep(45)
            comment.reply(aa10)
            #sleep(s)
            #print(comment.id)
            #print(i)
            comment.upvote()
            #print(comment.id)
          if a11 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
            sleep(45)
            comment.reply(aa11)
            #sleep(s)
            #print(comment.id)
            #print(i)
            comment.upvote()
            #print(comment.id)
          if a12 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
            sleep(45)
            comment.reply(aa12)
            #sleep(s)
            #print(comment.id)
            #print(i)
            comment.upvote()
            #print(comment.id)
          if a13 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
            sleep(45)
            comment.reply(aa13)
            #sleep(s)
            #print(comment.id)
            #print(i)
            comment.upvote()
            #print(comment.id)
          if a14 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
            sleep(45)
            comment.reply(aa14)
            #sleep(s)
            #print(comment.id)
            #print(i)
            comment.upvote()
            #print(comment.id)
          if a15 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
            sleep(45)
            comment.reply(aa15)
            #sleep(s)
            #print(comment.id)
            #print(i)
            comment.upvote()
            #print(comment.id)
          if a16 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
            sleep(45)
            comment.reply(aa16)
            #sleep(s)
            #print(comment.id)
            #print(i)
            comment.upvote()
            #print(comment.id)
          if a17 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
            sleep(45)
            comment.reply(aa17)
            #sleep(s)
            #print(comment.id)
            #print(i)
            comment.upvote()
            #print(comment.id)
          if a18 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
            sleep(45)
            comment.reply(aa18)
            #sleep(s)
            #print(comment.id)
            #print(i)
            comment.upvote()
            #print(comment.id)
          if a19 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
            sleep(45)
            comment.reply(aa19)
            #sleep(s)
            #print(comment.id)
            #print(i)
            comment.upvote()
            #print(comment.id)
          if a20 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
            sleep(45)
            comment.reply(aa20)
            #sleep(s)
            #print(comment.id)
            #print(i)
            comment.upvote()
            #print(comment.id)
          if a21 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
            sleep(45)
            comment.reply(aa21)
            #sleep(s)
            #print(comment.id)
            #print(i)
            comment.upvote()
            #print(comment.id)
          if a22 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
            sleep(45)
            comment.reply(aa22)
            #sleep(s)
            #print(comment.id)
            #print(i)
            comment.upvote()
            #print(comment.id)
          if a23 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
            sleep(45)
            comment.reply(aa23)
            #sleep(s)
            #print(comment.id)
            #print(i)
            comment.upvote()
            #print(comment.id)
          if a24 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
            sleep(45)
            comment.reply(aa24)
            #sleep(s)
            #print(comment.id)
            #print(i)
            comment.upvote()
            #print(comment.id)
          if a25 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
            sleep(45)
            comment.reply(aa25)
            #sleep(s)
            #print(comment.id)
            #print(i)
            comment.upvote()
            #print(comment.id)
          if a26 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
            sleep(45)
            comment.reply(aa26)
            #sleep(s)
            #print(comment.id)
            #print(i)
            comment.upvote()
            #print(comment.id)
          if a27 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
            sleep(45)
            comment.reply(aa27)
            #sleep(s)
            #print(comment.id)
            #print(i)
            comment.upvote()
          if a28 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
            sleep(45)
            comment.reply(aa28)
            #sleep(s)
            #print(comment.id)
            #print(i)
            comment.upvote()
          if a29 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
            sleep(45)
            comment.reply(aa29)
            #sleep(s)
            #print(comment.id)
            #print(i)
            comment.upvote()
          if a30 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
            sleep(45)
            comment.reply(aa30)
            #sleep(s)
            #print(comment.id)
            #print(i)
            comment.upvote()
          if a31 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
            sleep(45)
            comment.reply(aa31)
            #sleep(s)
            #print(comment.id)
            #print(i)
            comment.upvote()
            #print(comment.id)
            #print(i)
            comment.upvote()
          if a32 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
            sleep(45)
            comment.reply(aa32)
            #sleep(s)
            #print(comment.id)
            #print(i)
            comment.upvote()
            #print(comment.id)
            #print(comment.id)
          if a33 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
            sleep(45)
            comment.reply(aa33)
            #sleep(s)
            #print(comment.id)
            #print(i)
            comment.upvote()
          if a34 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
            sleep(45)
            comment.reply(aa34)
          #   #sleep(s)
            #print(comment.id)
            #print(i)
            comment.upvote()
          if a35 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
            sleep(45)
            comment.reply(aa35)
          #   #sleep(s)
            #print(comment.id)
            #print(i)
            comment.upvote()
          if a36 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
            sleep(45)
            comment.reply(aa36)
          #   #sleep(s)
            #print(comment.id)
            #print(i)
            comment.upvote()
            comment.upvote()
          if a37 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
            sleep(45)
            comment.reply(aa37)
          #   #sleep(s)
            #print(comment.id)
            #print(i)
            comment.upvote()
          if a38 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
            sleep(45)
            comment.reply(aa38)
          #   #sleep(s)
            #print(comment.id)
            #print(i)
            comment.upvote()
          if a39 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
            sleep(45)
            comment.reply(aa39)
          #   #sleep(s)
            #print(comment.id)
            #print(i)
            comment.upvote()
          if a40 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
            sleep(45)
            comment.reply(aa40)
          #  #sleep(s)
            #print(comment.id)
            #print(i)
            comment.upvote()
          if a41 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
            sleep(45)
            comment.reply(aa41)
            #sleep(s)
            #print(comment.id)
            #print(i)
            comment.upvote()
          if a42 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
            sleep(45)
            comment.reply(aa42)
          #  #sleep(s)
            #print(comment.id)
            #print(i)
            comment.upvote()
          if a43 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
            sleep(45)
            comment.reply(aa43)
           #sleep(s)
            #print(comment.id)
            ##print(i)
            comment.upvote()
          if a44 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
            sleep(45)
            comment.reply(aa44)
           ##sleep(s)
           # #print(comment.id)
           # ##print(i)
            comment.upvote()
        #   #if a45 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
           #sleep(45)
        #     comment.reply(aa45)
           ##sleep(s)
           # #print(comment.id)
           # ##print(i)
        #     #comment.upvote()
        #   #if a46 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
           #sleep(45)
        #     comment.reply(aa46)
           ##sleep(s)
           # #print(comment.id)
           # ##print(i)
        #    # comment.upvote()
        #   #if a47 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
           #sleep(45)
        #     comment.reply(aa47)
           ##sleep(s)
           # #print(comment.id)
           # ##print(i)
           #comment.upvote()
        #   #if a48 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
           #sleep(45)
        #     comment.reply(aa48)
           ##sleep(s)
           # #print(comment.id)
           # ##print(i)
           #comment.upvote()
        #   #if a49 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
           #sleep(45)
        #     comment.reply(aa49)
           ##sleep(s)
           # #print(comment.id)
           # ##print(i)
        #    # comment.upvote()
        #   #if a50 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
           #sleep(45)
        #     comment.reply(aa50)
           ##sleep(s)
           # #print(comment.id)
           # ##print(i)
        #    # comment.upvote()
        #   # if a51 in comment.body and comment.id not in comments_replied_to and comment.submission not in comments_replied_to and comment.author != reddit.user.me() and comment.author != "AutoModerator" and comment.author != "QualityVote":
           # sleep(45)
        #     comment.reply(aa51)
           # #sleep(s)
        #     # #print(comment.id)
        #     # ##print(i)
        #     #comment.upvote()

          f = open("reply_comment.txt", "a")
          f.write(comment.id + " ")
          f.write(comment.submission)
          #if comment.submission + "  " in comments_replied_to:
          #    print("found text")
              #f.write(submission + " ")
  except Exception as e:
    print("bohot jayada hora hai")
    print(e)
    sleep(1000)
    pass
try:
  comment()
except Exception as e:
  print(e)
  sleep(1000)
  pass

