import plotly.graph_objects as go
import streamlit as st

def speedometer(score):
    fig = go.Figure(go.Indicator(
        domain={'x': [0, 1], 'y': [0, 1]},
        value=score,
        mode="gauge+number+delta",
        delta={'reference': 1},
        gauge={'axis': {'range': [-1, 1]},
               'steps': [
                   {'range': [-1, -0.25], 'color': "red"},
                   {'range': [-0.25, 0.25], 'color': "white"}, {'range': [0.25, 1], 'color': "yellow"}],
               'threshold': {'line': {'color': "black", 'width': 4}, 'thickness': 0.75, 'value': 1}}))

    fig.update_layout(
        autosize=False,
        width=500,
        height=300,
        margin=dict(
            l=30,
            r=30,
            b=50,
            t=50,
            pad=0
        ),
        paper_bgcolor="white",
    )
    st.plotly_chart(fig, use_container_width=True)
    st.text("Red:Negative Sentiment,White:Neutral Sentiment,Yellow:Positive Sentiment ")
