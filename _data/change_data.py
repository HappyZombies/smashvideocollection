# Author: Daniel R. (@theDEEJAY69)
# Code is being improved all the time, if you find a way to optimize it be sure to discuss!
# Current things that can be improved: loop so we can leave adding a new video, and directly go to a new category
#
# - This code was created so we could skip the copy and pasting of text. Now we just easily add it ! 
#
# You must have Python and the PyYaml extension installed
#
import yaml
new_video = """
    - title: <video_title>
      url: <video_url>    
      opponent: <opponent>    
"""
with open("characters.yml") as f:
    the_file = yaml.load(f)
    video_data = yaml.load(new_video)
    newvideo_data = video_data[0]
    character = raw_input("Enter Name for Character: ")
    character = character.title()
    try:
        error = the_file[character]
    except Exception, e:
        print "WARNING!!!: '"+ character +"' is not a name in the .yml file."
    video_category = raw_input("""
What category in videos would would you like to change for """+character+"""
- Guides
- Montages 
- Tournaments
(type name)
""")
    video_category = video_category.title()
    print "\nAdding new video to '"+video_category+"' category"
    video_title = raw_input("Enter Title for New Video: ")
    video_url = raw_input("Enter URL for New Video: ")
    video_opponent = raw_input("Enter opponent for Video: ")        
    newvideo_data['title'] = video_title
    newvideo_data['url'] = video_url
    newvideo_data['opponent'] = video_opponent
    video_request = the_file[character]["videos"][video_category]+video_data
    the_file[character]["videos"][video_category] = video_request
    print "Content in "+video_category+"\n\n", yaml.dump(video_request, default_flow_style=False)
    print "...."
with open("characters.yml", "w") as f:
    yaml.dump(the_file, f, default_flow_style=False)
print "Done."