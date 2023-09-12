import streamlit as st
from InputHandler import *
from APIHandler import *
from GraphHandler import *

st.set_page_config(layout="wide")
st.title("Knowledge Graph Generator")

inputHandler=InputHandler()
inputHandler.desc_input()
inputHandler.api_key_input()
submit=st.button("Make Knowledge Graph")

if submit:
	with st.spinner(text="In progress..."):
		if(inputHandler.api_key and inputHandler.desc):
			apiHandler=APIHandler(inputHandler.desc,inputHandler.api_key)
			apiHandler.get_response()
			apiHandler.clean_response()
			apiHandler.generate_updates()

			graphHandler=GraphHandler()
			graphHandler.updateGraph(apiHandler.updates)
			graphHandler.init_figure(30,30)
			graphHandler.init_networkx()
			graphHandler.init_netgraph()
			graphHandler.show_output()
			st.balloons()


