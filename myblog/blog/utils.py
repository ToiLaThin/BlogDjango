import matplotlib.pyplot as plt
from io import BytesIO
import base64
from .models import Post, Category
from django.contrib.auth.models import User
from django.db.models import Count
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    img_png = buffer.getvalue()
    graph = base64.b64encode(img_png)
    graph = graph.decode('utf-8')

    buffer.close()
    return graph


def get_plot(x: str, hue: str, df: pd.DataFrame, xlabel: str, ylabel: str, title: str, y: str = None, cond: int = 1):
    if cond == 1:
        sub_df = df.groupby(x)[hue].value_counts().to_frame()
        sub_df.columns = ['count']
        y = 'count'
    elif cond == 2:
        sub_df = df.groupby([x, hue])[y].sum().to_frame()
    elif cond == 3:
        sub_df = df.groupby([x, hue])['Word-Count'].mean().to_frame()
        sub_df.columns = ['Avg-Word-Count']
        y = 'Avg-Word-Count'

    sub_df.reset_index(inplace=True)

    plt.switch_backend('AGG')
    plt.figure(figsize=(12, 8))
    sns.barplot(x, y, hue, sub_df)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(loc="upper left")
    plt.tight_layout()

    # sau khi plt.plot xong thì trong get_graph có plt.savefig(buffer)
    graph = get_graph()
    return graph


# chuyển các seriest thành 1 dataframe duy nhất
def pre_process(sr1: pd.Series, sr2: pd.Series, sr3: pd.Series, sr4: pd.Series = None, sr5: pd.Series = None):
    pd_dict = {
        'Title': sr1,
        'Body': sr2,
        'Category-Name': sr3,
        'Author': sr4,
        'Likes':  sr5,
    }
    df = pd.DataFrame(pd_dict)
    df.fillna('', inplace=True)
    sr = df['Body'].str.split(' ')
    sr.update([len(words_lst) for words_lst in sr.values])
    df['Word-Count'] = sr
    return df


def get_dataframe():
    post_titles = list(Post.objects.all().values_list('title', flat=True))
    post_titles = pd.Series(post_titles)

    post_bodies = list(Post.objects.all().values_list('body', flat=True))
    post_bodies = pd.Series(post_bodies)

    post_categories = list(
        Post.objects.all().values_list('category', flat=True))
    post_categories = pd.Series(post_categories)

    post_authors = list(Post.objects.all().select_related(
        'author').values_list('author_id', flat=True))
    post_authors = pd.Series(post_authors)

    # đếm số trường likes gắn với 1 bài post
    post_likes = Post.objects.all().annotate(like_count=Count('likes'))
    post_likes = pd.Series([post.like_count for post in post_likes])

    df = pre_process(sr1=post_titles, sr2=post_bodies,
                     sr3=post_categories, sr4=post_authors, sr5=post_likes)

    data_csv = df.to_csv('blog_data.csv', index=None, header=True)
    return df


def get_context_chart() -> dict:
    df = get_dataframe()
    chart1 = get_plot(x='Author', hue='Category-Name', df=df, xlabel='Author s id',
                      ylabel='Post s count', title='Number of Posts per user', cond=1)
    chart2 = get_plot(x='Author', y='Likes', hue='Category-Name', df=df, xlabel='Author s id',
                      ylabel='Likes per Category', title='Number of Likes per user', cond=2)
    chart3 = get_plot(x='Author', hue='Category-Name', df=df, xlabel='Author s id',
                      ylabel='Median words per Category of User', title='Media of Word per user', cond=3)
    posts_num = len(df)

    posts_author = df['Author']
    posts_author = posts_author.drop_duplicates().count()

    categories_num = df['Category-Name']
    categories_num = categories_num.drop_duplicates().count()

    revenue = df.get('Likes').sum() * 2
    context_dict = {
        'chart1': chart1,
        'chart2': chart2,
        'chart3': chart3,
        'posts_num': posts_num,
        'posts_author': posts_author,
        'categories_num': categories_num,
        'revenue': revenue,

    }
    return context_dict
