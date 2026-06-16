import plotly.express as px
import plotly.graph_objects as go


def bar_chart(df, x, y, title, color=None):
    return px.bar(df, x=x, y=y, color=color, title=title)


def line_chart(df, x, y, title, color=None):
    return px.line(df, x=x, y=y, color=color, markers=True, title=title)


def heatmap(df, x, y, z, title):
    pivot = df.pivot_table(index=y, columns=x, values=z, aggfunc="mean")
    return px.imshow(pivot, text_auto=True, aspect="auto", title=title)
