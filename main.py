from statistics import mode
import facebook_scraper
import pandas as pd


my_scraper = facebook_scraper._scraper
my_scraper.set_user_agent(
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" "AppleWebKit/537.36 (KHTML, like Gecko)""Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47"
)
df = pd.DataFrame(columns=['username', 'time', 'likes',
                  'comments', 'shares', 'reactions', 'post_text'])

posts = facebook_scraper.get_posts(
    group='689278925171103', cookies="./facebook_cookie.json")

for index, post in enumerate(posts):
    print(("+"*10) + str(index) + ("+"*10))
    dataframe = post
    _df = pd.DataFrame.from_dict(dataframe, orient='index')
    # print(_df.head())
    _df = _df.transpose()
    # print(_df.head())
    df = df.append(_df)
    # pd.concat([df, _df])
    print(df.head(3))
    # 每20条保存一次。
    if (index > 0 and index % 3 == 0):
        print('saving file')
        df.to_csv('./facebook_posts.csv', index=False, mode='a')
        df = pd.DataFrame(columns=['username', 'time', 'likes',
                  'comments', 'shares', 'reactions', 'post_text'])
        if(index == 2000):
            break


