from requests_html import HTMLSession
import pandas  as pd 
s = HTMLSession()
url = 'https://www.youtube.com/@GeeksforGeeksVideos/videos'

# create empty list
data = []

# sent the request to server
r = s.get(url)
# render the javascript page
r.html.render(sleep=3,timeout =2000 , keep_page=True,scrolldown=20)
container = r.html.find('ytd-rich-grid-row.style-scope.ytd-rich-grid-renderer')

# use for loop to scraping all data
for ele in container:
    vediotitle = ele.find('yt-formatted-string.style-scope.ytd-rich-grid-media',first = True).text 
    videourl ='https://www.youtube.com'+ ele.find('a#video-title-link',first=True).attrs['href']
    views = ele.find('#metadata-line > span:nth-child(3)',first = True).text.replace('views','')
    posted = ele.find('#metadata-line > span:nth-child(4)',first = True).text
    Videolength = ele.find('#text',first = True).text

    # append all data
    data.append([vediotitle,videourl,views,posted,Videolength])


# create pandas dataframe
df = pd.DataFrame(data,columns=['VideoTitle','Video Url','Views','Posted','Videolength'])
df.to_csv('yt.csv',index = False)
