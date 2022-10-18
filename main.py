import facebook_scraper
import pandas as pd


my_scraper = facebook_scraper._scraper
my_scraper.set_user_agent(
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" "AppleWebKit/537.36 (KHTML, like Gecko)""Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47"
)
df = pd.DataFrame(columns=['username', 'time', 'likes',
                  'comments', 'shares', 'reactions', 'post_text'])

posts = facebook_scraper.get_posts(
    group='327882939484536', cookies="./facebook_cookie.json")

for index, post in enumerate(posts):
    dataframe = post
    _df = pd.DataFrame.from_dict(dataframe, orient='index')
    _df = _df.transpose()
    df = df.append(_df)
    # 该部分功能仅供测试使用，爬5条就保存退出。
    if (index > 0 and index % 5 == 0):
        break

print('saving file')
df.to_csv('./facebook_posts.csv', index=False)
