##
import streamlit as st
import pandas as pd


df = pd.read_csv('recommended.csv')

##

import ast

def parse_string_to_list(string):
    return ast.literal_eval(string)

df['recommended_articles'] = df['recommended_articles'].apply(parse_string_to_list)

##

def main():
    st.title("Article Recommendations")

    num_articles = len(df)
    articles_per_row = 4
    padding = 20
    image_width = 150
    image_height = 200

    for i in range(0, num_articles, articles_per_row):
        cols = st.columns(articles_per_row)
        for j in range(articles_per_row):
            if i + j < num_articles:
                with cols[j]:
                    image = df.iloc[i + j]['image_url']
                    title = df.iloc[i + j]['title_long']
                    st.image(image, width=image_width, use_column_width=False)
                    st.markdown(f"<p style='text-align:center'>{title}</p>", unsafe_allow_html=True)

                    if 'recommended_articles' in df.columns and isinstance(df.iloc[i + j]['recommended_articles'],
                                                                           list):
                        expander = st.expander("Recommended Articles")
                        with expander:
                            recommended_indices = df.iloc[i + j]['recommended_articles']
                            for idx in recommended_indices:
                                st.write(df.iloc[idx]['title_short'])


if __name__ == "__main__":
    main()
