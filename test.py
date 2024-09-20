import streamlit as st
import pandas as pd
import numpy as np
st.set_page_config(
    page_title="DrAni List",  # Set the title of the webpage
    page_icon="🖥️",                # Set the icon of the webpage (can be emoji or path to an image)
    layout="wide",                  # Set the layout (wide or centered)
)

if st.checkbox("Show"):
    st.title("DrAni List")
    st.header("Introduction")
    st.subheader("Why DrAni List?")
    st.text('A free website/tool to track your Animes, Series, Manga and Dramas in one website!')
    st.markdown('test')

st.image("https://github.com/Sys-stack/IP-Test/blob/test/japan-background-digital-art.jpg?raw=true")
st.markdown(
    """
    <div style="position: relative; text-align: center; color: white;">
        <h2 style="position: absolute; top: 20%; left: 50%; transform: translate(-50%, -50%);">
            omg yoo
        </h2>
    </div>
    """,
    unsafe_allow_html=True
)
import jinja2

#def command for one list in another
def sublistcheck(sub, master):
    for i in sub:
        if i not in master:
            y = False
            break
        else:
            y = True
    return y

#Creating the dataframe models

anidictmodel = {'S.no':[], 'Title':[],'Status':[],
                'Studio': [], 'Genre': [], 'Start-date': [], 
                'End-date': [], 'Source': [], 'Score': [], 
                'Tags': [], 'Season':[]}


#Actual list

all_ani_list = pd.read_csv('https://raw.githubusercontent.com/Sys-stack/IP-Test/test/anilist.csv', sep= '*')
#all_ani_list = pd.DataFrame(anidictmodel)
all_ani_list.set_index('S.no', inplace = True)
all_ani_list.style.set_properties(**{"font-size":"1.5rem",
                                  'color':'Blue',
                                  'width':'100px',
                                  'Background-color':'Black'})

#Main menu
st.table(pd.DataFrame([st.image("https://github.com/Sys-stack/IP-Test/blob/test/japan-background-digital-art.jpg?raw=true")])
st.text('''
      -------------------------------------------------------------------
                                        MENU
      -------------------------------------------------------------------
      1. Show List - (Filtered, Unfiltered)
      2. Errors
      3. Timeline
      4. Statistics
      5. Profile''')
cmd = st.radio('Choose: ', ("Show List", "Errors", 'Timeline', 'Statistics', 'Profile'))



#completed list
owari_list = pd.DataFrame(anidictmodel)
owari_list.set_index('S.no',inplace = True)
owari_list.style.set_properties(**{"font-size":"1.5rem",
                                  'color':'Blue',
                                  'width':'100px',
                                  'Background-color':'Black'})
i = 0
for [row,rowseries] in all_ani_list.iterrows():
    if all_ani_list['Status'][row] == 'Completed':
        i += 1
        owari_list.loc[i] = rowseries

#watching list
wat_list = pd.DataFrame(anidictmodel)
wat_list.set_index('S.no',inplace = True)
wat_list.style.set_properties(**{"font-size":"1.5rem",
                                  'color':'Blue',
                                  'width':'100px',
                                  'Background-color':'Black'})
i = 0
for [row,rowseries] in all_ani_list.iterrows():
    if all_ani_list['Status'][row] == 'Watching':
        i += 1
        wat_list.loc[i] = rowseries

#On-HOld list
oh_list = pd.DataFrame(anidictmodel)
oh_list.set_index('S.no',inplace = True)
oh_list.style.set_properties(**{"font-size":"1.5rem",
                                  'color':'Blue',
                                  'width':'100px',
                                  'Background-color':'Black'})
i = 0
for [row,rowseries] in all_ani_list.iterrows():
    if all_ani_list['Status'][row] == 'On-Hold':
        i += 1
        oh_list.loc[i] = rowseries

#Dropped list
drop_list = pd.DataFrame(anidictmodel)
drop_list.set_index('S.no',inplace = True)
drop_list.style.set_properties(**{"font-size":"1.5rem",
                                  'color':'Blue',
                                  'width':'100px',
                                  'Background-color':'Black'})
i = 0
for [row,rowseries] in all_ani_list.iterrows():
    if all_ani_list['Status'][row] == 'Dropped':
        i += 1
        drop_list.loc[i] = rowseries

#watching list
ptw_list = pd.DataFrame(anidictmodel)
ptw_list.set_index('S.no',inplace = True)
ptw_list.style.set_properties(**{"font-size":"1.5rem",
                                  'color':'Blue',
                                  'width':'100px',
                                  'Background-color':'Black'})
i = 0
for [row,rowseries] in all_ani_list.iterrows():
    if all_ani_list['Status'][row] == 'Plan to Watch':
        i += 1
        ptw_list.loc[i] = rowseries

#show lists
#unfiltered

if cmd == ('Show List' or '1'):
    st.text('''          1. All
          2. Currently Watching
          3. Completed
          4. On-hold
          5. Dropped
          6. Plan to Watch
          for filtering options, type \'filter\' as a prefix ''')
    key = st.text_input('Choose list: ')
    dick1 = {'All': all_ani_list,
            'Currently Watching': wat_list, 
            'Completed': owari_list, 
            'On-hold': oh_list, 
            'Dropped': drop_list, 
            'Plan to Watch': ptw_list}
    if key in dick1:
        st.table(dick1[key])

    #filtered
    if 'filter' in key:
        st.text('Ayaan: Hold my Keyboard!')
''' AYAAN'S JOB '''

#Error Checker
genre = ["Action", "Adventure", "Comedy",
         "Drama", "Fantasy", "Horror",
         "Mystery", "Psychological", "Romance",
         "Sci-Fi", "Slice of Life", "Sports",
         "Supernatural", "Historical",
         "Music", "Mecha", "Magic",
         "Military", "Superpower",
         "Demons", "Isekai", "Harem",
         "Yaoi", "Yuri", "Tragedy",
         "Parody", "Ecchi", "Seinen",
         "Shoujo", "Shounen", "Josei",
         "Gender Bender", "Martial Arts", "Space",
         "Game","School", "Vampire",
         "Samurai", "Aliens", "Dystopian",
         "Romantic Comedy", "Psychological Thriller",
         "Gore", "Dark Fantasy", "Action Comedy",
         "Historical Drama", "Superhero", "Post-Apocalyptic",
         "CGDCT"]

stxt = 'There are status errors in the following rows: '
gtxt = 'There are genre errors in the following rows: '
sarguement = 0
garguement = 0

if cmd == ('Errors' or '4'):
    for [row,rowseries] in all_ani_list.iterrows():
#Status column
        if all_ani_list['Status'][row] != ('Completed' or 'Plan to Watch' or
                                           'Dropped' or 'On-hold' or
                                           'Watching'):
            stxt += ('''
                    ''' + '(Status)' + str(row))
            sarguement = True

#Genre Column

        if sublistcheck(eval(all_ani_list['Genre'][row]),genre) == False:
            gtxt += ('''
                    ''' + '(Genre)' + str(row))
            garguement = True
if sarguement == True:
    st.text(stxt)
if garguement == True:
    st.text(gtxt)

