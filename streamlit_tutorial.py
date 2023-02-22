import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import altair as alt
from datetime import datetime, time
from vega_datasets import data


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

################################################################################################################

st.header('st.slider')
st.markdown('---')
st.write('The following data types are supported: int, float, date, time, and datetime.')

# Example 1

st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, ' years old')

# Example 2
st.subheader('Range Slider')
values = st.slider('Select a range of values', 0.0, 100.0, (25.0, 75.0))
st.write('Values: ', values)

# Example 3
st.subheader('Range Time Slider')

appointment = st.slider('Schedule your appointment:',
                        value=(time(11, 30), time(12, 45)))
st.write('You are scheduled for: ', appointment)

# Example 4
st.subheader('DateTime Slider')

start_time = st.slider('When do you start?', value=datetime(
    2023, 2, 22, 6, 30), format="MM/DD/YY - hh:mm")
st.write('Start time: ', start_time)

################################################################################################################

st.header('st.select_slider')
st.markdown('---')
st.write('''
This also allows you to render a range slider by passing a two-element tuple or list as the value.

The difference between st.select_slider and st.slider is that select_slider accepts any datatype and takes an iterable set of options, while slider only accepts numerical or date/time data and takes a range as input.''')

color = st.select_slider(
    'Select a color of the rainbow',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
st.write('My favorite color is', color)

start_color, end_color = st.select_slider(
    'Select a range of color wavelength',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
    value=('red', 'green'))
st.write('You selected wavelengths between', start_color, ' and ', end_color)

################################################################################################################

st.header('st.line_chart')
st.markdown('---')

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

################################################################################################################

st.header('st.altair_chart')
st.markdown('---')
st.write(
    'Examples of Altair charts: [Altair Gallery](https://altair-viz.github.io/gallery)')

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

c = alt.Chart(chart_data).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.altair_chart(c, use_container_width=True)

################################################################################################################

source = data.cars()

chart = alt.Chart(source).mark_circle().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
    tooltip=['Name', 'Origin', 'Horsepower', 'Miles_per_Gallon']
).interactive()

tab1, tab2 = st.tabs(['Streamlit Theme (Default)', 'Altair Native Theme'])

with tab1:
    st.altair_chart(chart, theme="streamlit", use_container_width=True)
with tab2:
    st.altair_chart(chart, theme=None, use_container_width=True)

################################################################################################################

source = data.seattle_weather()

scale = alt.Scale(
    domain=["sun", "fog", "drizzle", "rain", "snow"],
    range=["#e7ba52", "#a7a7a7", "#aec7e8", "#1f77b4", "#9467bd"],
)
color = alt.Color("weather:N", scale=scale)

# We create two selections:
# - a brush that is active on the top panel
# - a multi-click that is active on the bottom panel
brush = alt.selection_interval(encodings=["x"])
click = alt.selection_multi(encodings=["color"])

# Top panel is scatter plot of temperature vs time
points = (
    alt.Chart()
    .mark_point()
    .encode(
        alt.X("monthdate(date):T", title="Date"),
        alt.Y(
            "temp_max:Q",
            title="Maximum Daily Temperature (C)",
            scale=alt.Scale(domain=[-5, 40]),
        ),
        color=alt.condition(brush, color, alt.value("lightgray")),
        size=alt.Size("precipitation:Q", scale=alt.Scale(range=[5, 200])),
    )
    .properties(width=550, height=300)
    .add_selection(brush)
    .transform_filter(click)
)

# Bottom panel is a bar chart of weather type
bars = (
    alt.Chart()
    .mark_bar()
    .encode(
        x="count()",
        y="weather:N",
        color=alt.condition(click, color, alt.value("lightgray")),
    )
    .transform_filter(brush)
    .properties(
        width=550,
    )
    .add_selection(click)
)

chart = alt.vconcat(points, bars, data=source,
                    title="Seattle Weather: 2012-2015")

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Altair native theme"])

with tab1:
    st.altair_chart(chart, theme="streamlit", use_container_width=True)
with tab2:
    st.altair_chart(chart, theme=None, use_container_width=True)

st.markdown('---')
st.write('altair char with Annotations')

# We use @st.cache_data to keep the dataset in cache


@st.cache_data
def get_data():
    source = data.stocks()
    source = source[source.date.gt("2004-01-01")]
    return source


source = get_data()

# Define the base time-series chart.


def get_chart(data):
    hover = alt.selection_single(
        fields=["date"],
        nearest=True,
        on="mouseover",
        empty="none",
    )

    lines = (
        alt.Chart(data, title="Evolution of stock prices")
        .mark_line()
        .encode(
            x="date",
            y="price",
            color="symbol",
        )
    )

    # Draw points on the line, and highlight based on selection
    points = lines.transform_filter(hover).mark_circle(size=65)

    # Draw a rule at the location of the selection
    tooltips = (
        alt.Chart(data)
        .mark_rule()
        .encode(
            x="yearmonthdate(date)",
            y="price",
            opacity=alt.condition(hover, alt.value(0.3), alt.value(0)),
            tooltip=[
                alt.Tooltip("date", title="Date"),
                alt.Tooltip("price", title="Price (USD)"),
            ],
        )
        .add_selection(hover)
    )
    return (lines + points + tooltips).interactive()


chart = get_chart(source)

# Add annotations
ANNOTATIONS = [
    ("Mar 01, 2008", "Pretty good day for GOOG"),
    ("Dec 01, 2007", "Something's going wrong for GOOG & AAPL"),
    ("Nov 01, 2008", "Market starts again thanks to..."),
    ("Dec 01, 2009", "Small crash for GOOG after..."),
]
annotations_df = pd.DataFrame(ANNOTATIONS, columns=["date", "event"])
annotations_df.date = pd.to_datetime(annotations_df.date)
annotations_df["y"] = 10

annotation_layer = (
    alt.Chart(annotations_df)
    .mark_text(size=20, text="⬇", dx=-8, dy=-10, align="left")
    .encode(
        x="date:T",
        y=alt.Y("y:Q"),
        tooltip=["event"],
    )
    .interactive()
)

st.altair_chart(
    (chart + annotation_layer).interactive(),
    use_container_width=True
)
