import requests
import json
import re
import time
import random

if __name__ == '__main__':
    
    key = input("\n\n請輸入地名與目標(旅遊&風景...) : ")
    IG_API = 'https://www.instagram.com/explore/tags/'+key+'/?__a=1'

    count = 0
    a = requests.get(IG_API).text
    b = json.loads(a)
    
    try:
        output = []

        for item in b['graphql']['hashtag']['edge_hashtag_to_top_posts']['edges']: #定位字典
        
            pic = item['node']['display_url'] #圖片
            href = item['node']['shortcode'] #連結
            content = item['node']['edge_media_to_caption']['edges'][0]['node']['text']



            '''print('===================\n這是第'+str(count)+'個hashtag\n')
            print(content[:50]+'...\n')
            print('https://www.instagram.com/p/'+href+'/\n===================')

            count += 1

            img_data = requests.get(pic).content
            

            print("Start downloading.")
            with open(str(count)+'.jpg', 'wb') as handler: #下載圖片到默認
                
                handler.write(img_data)
                handler.flush()
            handler.close()
            print("Done.")
            time.sleep(1)'''

            result = content[:50] +'https://www.instagram.com/p/' +href
            output.append(result)                            #將搜尋結果逐條加入陣列

        print(random.choice(output))

    except:
        pass
   