from flask import Flask, request, abort
import requests
import pandas as pd

app = Flask(__name__)
domain = "https://jsonplaceholder.typicode.com"

def download(endpoint):
    url = f"{domain}/{endpoint}"
    response = requests.get(url)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        abort(400, description=f"{endpoint.title()} endpoint is invalid")

@app.route("/top")
def process():
    df_comments = download("comments")
    df_posts = download("posts")
    
    df_comments_count = df_comments.groupby("postId")["id"].agg("count")
    df_comments_count = df_comments_count.rename('comments_count')
    
    df = df_posts.merge(df_comments_count, how="left", left_on="id", right_index=True)
    df = df.sort_values(by='comments_count', ascending=False)
    df = df[['id', 'title', 'body', 'comments_count']].rename(columns={
        'id': 'post_id',
        'title': 'post_title',
        'body': 'post_body',
        'comments_count': 'total_number_of_comments',
    })

    result = df.to_dict(orient='records')
    return result

@app.route("/search")
def search():
    params = request.args.to_dict()
    df_comments = download("comments")

    filters = []
    for key, value in params.items():
        if key in df_comments.columns:
            try:
                value = float(value)
            except:
                value = value
            if isinstance(value, float):
                filters.append(f"{key} == {value}")
            elif isinstance(value, str):
                filters.append(f"{key}.str.contains(@value)")

    if filters:
        query = " & ".join([q for q in filters])
        df = df_comments.query(query)
    else:
        df = df_comments

    result = df.to_dict(orient='records')
    return result

if __name__ == "__main__":
    app.run()
