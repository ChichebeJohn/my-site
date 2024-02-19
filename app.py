from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie



st.set_page_config(page_title="My Webpage", page_icon="👋", layout="wide")

def load_lottieurl(url):
  r=requests.get(url)
  if r.status_code != 200:
    return None
  return r.json()

def local_css(file_name):
  with open(file_name) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
local_css("style/style.css")

#---- load assets------
lottie_coding = "https://lottie.host/2b83c8cc-8e0d-488c-97b4-1ac783c89aef/Ck0aQJb92P.json"
img_contact_form = Image.open("images/logo.png")
img_lottie_animation = Image.open("images/virtualmarket!!.png")


# ------ Header Section --------
with st.container():
 st.subheader("Hi, I am John 👋" )
 st.title("A graphic designer from Nigeria")
 st.write("I am passionte about fiding ways to use python and VBA to be more efficient and effective in building webpages.")
 st.write("[Learn More >](https://pythonandvba.com)")

# ----- WHAT I DO ---------
with st.container():
  st.write("---")
  left_column, right_column = st.columns(2)
  with left_column:
    st.header("What I do")
    st.write("##")
    st.write(
        """
        on my facebook page you get to learn alot about graphics design using powerful tools like corel draw, adobe photoshop, paint etc:
        - are you looking for a competent hand to guide you in your graphics design journey?
        - are you struggling with repeatative design patterns?
        - want to learn more new things about graphics design?
        - are you working on a design and yourself thinking - "there've got to be a better way"
        - If this sounds intresting to your then follow our facebook channel!!
        """
    )
    st.write("[FaceBook Channel >](https://web.facebook.com/profile.php?id=100032823554889)")
    with right_column:
      st_lottie(lottie_coding, height=300, key="coding")
      
      
      #-------- projects ----------
  with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
          st.image(img_lottie_animation)
          
          
    with text_column:
            st.subheader("Integrate Lottie Animation Inside Your Streamlite App")
            st.write(
  """
  Learn to use lottie files in Streamlit!
  Animations make our web app more engainging and fun, and Lottie files are the easiest way to do it in this tutorial i will show you how.
  """
   )
    st.markdown("[watch video...](https://youtu.be/TXSOitGoINE)")
with st.container():
  image_column, text_column = st.columns((1, 2))
  with image_column:
    st.image(img_contact_form)
with text_column:
  st.subheader("how to add a contact form to your streamlit App")
  st.write(
     """
     erdtyfugihlkjhcjyrk
     r6er7iuhgzr567i8ohklbjhjrewzdfghjk/huytrae\dsghjbkuiytrcghkukytsrzfgxjkytuydtgjkluytsr
     yhtgfghjkdtxgbbukytrsgfxhjbbjkufyjghcbjjhfgxbvkgjfgdhfxbh
     """
  )
  st.markdown("[watch video....](https://youtu.be/FOULV9Xij_8)")
  
  #--------- Contact --------
with st.container():
  st.write("---")
  st.header("Get In Touch With Me!")
  st.write("##")
  
  contact_form = """
  <form action="https://formsubmit.co/chichebenmesoma@gmail.com" method="POST">
     <input type= "hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="your message here" required></textarea>
     <button type="submit">Send</button>
  </form>
  """
  left_column, right_column = st.columns(2)
  with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
  with right_column:
    st.empty()
    