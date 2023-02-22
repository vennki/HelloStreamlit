import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import altair as alt


st.write("Hello World!")

################################################################################################################

st.header('st.button')
st.markdown('---')

if st.button('Say Hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

################################################################################################################

st.header('st.write')
st.markdown('---')

# Example 1

st.write('Hello, *World!* :sunglasses:')

# Example 2

st.write(1234)

# Example 3

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

st.write(df)

# Example 4

st.write('Below is a DataFrame:', df, 'Above is a DataFrame')

# Example 5

df2 = pd.DataFrame(np.random.randn(200, 3),
                   columns=['a', 'b', 'c'])

st.write(df2)

c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.write(c)

################################################################################################################

st.header('st.markdown')
st.markdown('---')

# Example 1

st.markdown('Streamlit is **_really_ cool**.')
st.markdown(
    'This text is :red[colored red], and this is **:blue[colored]** and bold')
st.markdown(':green[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:')
st.markdown(
    'Emoji codes are found here: [Emoji Codes](https://share.streamlit.io/streamlit/emoji-shortcodes)')
st.markdown(
    'Supported LaTeX expressions: [LaTeX Expressions](https://katex.org/docs/supported.html)')


################################################################################################################

st.header('st.subheader')
st.markdown('---')

st.subheader('This is a subheader')
st.subheader(
    'A subheader with _italics_ :blue[colors] and emojis :sunglasses:')

################################################################################################################

st.header('st.caption')
st.markdown('---')

st.caption('This is a string that explains something above.')
st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')

################################################################################################################

st.header('st.text')
st.markdown('---')

st.text('This is some text.')

################################################################################################################

st.header('st.latex')
st.markdown('---')

st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

################################################################################################################

st.header('st.code')
st.markdown('---')

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')
