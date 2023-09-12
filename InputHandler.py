import streamlit as st
class InputHandler():
	def desc_input(self):
		self.desc=st.text_input("Enter The description")
	def api_key_input(self):
		self.api_key=st.text_input("Enter your OpenAI API key")
		