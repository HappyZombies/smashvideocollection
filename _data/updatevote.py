# Author: Daniel R. (@theDEEJAY69)
# Code is being improved all the time, if you find a way to optimize it be sure to discuss!
#
# You must have Python and the PyYaml extension installed
# module `emaildata` is a module i created in order to contain the email and password. Use your own email and password if you want to test this out
#
#
# File will crash if not all 31 days are present
# File currently crashes because it only has 3 videos on it.
# Futher tesing is still required 
#
#
# The idea of this code is for it to run in the background. 
# Add 30 videos and 30 strawpoll links to vote.yml, and this file will automatically update the site with new page content
# It will also e-mail us the results of the poll. So we don't have to constantly go to the site...and view the results
#
#
# Again, for this automatic process to work you need to run the update.sh program AND this one.
import json, requests, yaml, time, emaildata, smtplib


def emailreport():
    login_email =  emaildata.email_address
    login_password = emaildata.email_password
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login(login_email, login_password)
    mail.sendmail(login_email,'smashvideocollection@hotmail.com', email_results)
    mail.close()

day_number = 0
now = time.strftime("%c")
todays_date = ("%s"  % now )
while True:
    with open("../files/vote.html", "w") as f:
        day_number += 1
        day = "day"+str(day_number)
        vote_content = ("""---
layout: default
character_name: Vote
permalink: /vote/
comments: true
---
<div class = "middle-wrapper">
    <h1>Today's video is for {{site.data.vote."""+day+""".character}}!</h2>
        <iframe width="600" height="390" src="{{site.data.vote."""+day+""".video}}" frameborder="0" allowfullscreen>Your browser does not support iFrame</iframe>
        &nbsp;
        <iframe src="{{site.data.vote."""+day+""".strawpoll}}" style="width: 600px; height: 390px; border: 0;">Loading poll...</iframe>
        <i>Last update on """+todays_date+"""</i>
    </div>
""")
        
        f.write(vote_content)
        f.close()
        if day == 'day31':
            break
    print "Done!"
    print "Waiting....will update page again in 24 hours"
    time.sleep(86400)
    #after 24 hours are over, retrieve results, e-mail it to me.
    #Set time.sleep for 24 hours = 86400 seconds 
    #Every 24 hours, python will change data in vote.html, thus automatically changing the data. 
    #We will use batch to automically git push origin gh-pages every 25 hours. Just to be safe 25 hours = 90000s
    print "Updating html page with new content..."
    with open("vote.yml") as vote_links:
        #Grab url from vote.yml and retrieve the number
            vote_data = yaml.load(vote_links)
            url_holder = vote_data[day]['strawpoll']
            video_link = vote_data[day]['video']
            vote_character = vote_data[day]['character']
            strawpoll_id = url_holder.replace("http://strawpoll.me/embed_1/", "")
            video_link = video_link.replace("embed/","watch?v=")
            url = "http://strawpoll.me/api/v2/polls/"+strawpoll_id
            #go to strawpoll and get data
            results = requests.get(url).json()
            totalvotes_yes = results['votes'][0]
            totalvotes_no = results['votes'][1]
            email_results = ("""Hey there! Here are the results for the video poll: This was for the  - """+ day
            +""" video\nThe total votes for `Yes` are: """ + str(totalvotes_yes)
            +"""\nThe total votes for `No` are: """ + str(totalvotes_no))+"""\nVideo link: """ + str(video_link)+"""\nCharacter is: """ + str(vote_character)
            print "Sending e-mail." 
            emailreport()
            #Here we will have code that sends an email to me
    
   
print "Waiting for next commands..."

