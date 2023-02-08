import os
import openai
import gradio as gr
from pyChatGPT import ChatGPT

session_token = "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..CfI-5f1eyeBoAGVF.IF4KP7Njh9MhZeU00KpAAWRlM0l6kiZAVKympM-q4Tdd_LQnL_3ASszUGmbG_qzmAQCwXdO70Rm6pDd7da-lHk9Qs0vfsL729pHUZZXGeDTUE4DXOj3VTRAockEEBiFdVyyE_y9_b-XJvCoixTuVd0e5hrBqRTAdqK3gt7kO1BLsaR6VE8SThf9vS2t5Tvo7JZCYZDx8aeQWadhmClagNWMVHekidlo_EfKB7obMTh4iZmVREJ5Kc9rhdMwl0ERBtKr53I-bD_Yx05nSYGpWm3IGM1c3GtB6VKzU9lk-5W9kApAJf-VzGVLZaat98NrH6gaQ70EVYQ_b6RKTo6LKpegtpbYQEkVKtRGEy1NKAAuQJA3r3rNUw_-RddZkmJSvfIfPErjVlHQ1rxGPGmFqQ2wfk9cFt5318xMfsgoK47OQjTQ32N_RGtrHwoclFw9-wg2RAaWRUtT49MBdSzNYsHyTtxJ6q5Nc2MFFw3KFwjGT91MWi5GT7A28fXhlnvQoEprrxG3oR1ozchiHQRheJauwjAhWR99aKa5hFF-2B3_lHff2csyz0fwhyzjNpDUoJ1lPd5T1bKCW5OI4O1anmknQOFRhkCiGDS_ZCSKMmpDSY7JY0ygXPk8MEvG8lE8Z9onoD0olQLebM--lBLT7nWkD288Y5SS4Dh9A7K3lF7ElAMbkkVng79SbvcXyprvmWc8wFpOBmb-JD2_4aREMDo8LimxIti4EuP9_7ieyn8WIOQIWCYDQjt_AzwN1G-vRYoqYlwWMxV2jlWOdEsJdY5yP2eOd0OVeuhkZH_ofbtLoqVc5ruRMgv1nc_FbXYT2LbDAmF7P1D4Krxp-MScIsLV7riZ_e1RTO3bNhSJo4o9dQwi_fR-WV2YGeOrTNZ5qupqkmg56bjiVWeUh1IIIRkS_QSyDBWzgt7j-dqxYQmpRd0LPbansm4ChxKW1wSH7zY-iWDIJhRwWP-FAd9Dps0S5OVgejGG6f4yBDf0-JWV1NB0jHHJ0247llqSCwc9KiPKrSrJQmQZl0SaiG36t1q-Kqe_LOei4FJDK6-Zw0ZQaaJ5ukDtciHpopaYC7d-3ynTj8GzOFrfLZHQW9rgbJ6wIHVLSyyiKhFk05YuYzd6bxQpgVPUjFljIwfpXyaI1hb_wRH8jGA8hdBo7cNjUbczb83IWqK7HpVROpoFbPKP4fMO9V6b5OCAH-8H8K-HMgERdRvMSvel_q6JQWmeCTaVOlPNpJvzYK0L2z_I4Ib8nw7VOKDB_uiD9yzZ5abULbH8XwLbAadTepA3WMUKrHe87gy6_Uri6ecuRkMZcUn3dLU3GnAONqK3UP5sL0iHjGsgIn2Wln3ufplQEdilS7M7oTHJ2_R9Q59kZHOkqc4VKtsFHxhIRS5iVWftonjQS5soViapsu-6kdAK7LA0z4_45k2CWW5R9mYCygRZ_OsSZaEZ_xAnx45cnqYYVHlnzBXwhlNUA6aqh9dqcoD4ru_j0hLZeJHMOj1rN_Z9-tadny3c5Rv4fSgc9SN_yReL32as-YMJQcJH3VaV0Q9MDAxgLX4fCkMojaGW79JTFindyTp0SbDI4WTmPKvOpl__L079t32fgwYkj9YfqYRl5OuBS0cR1ubVILOem-AlVmpIEkYs8xqwSDMikw8CTbsOZFcBEpfzhu8HHesWrESRSALlQNmVHfLM7RhWOsOH_bDlo2pcOdMRC-t8ZNDskP0Tq9mvg5bmkjLNkuBowLwWeEggQrGF6yhNsCNcgRCZ0D3uLXxgirpIu1KiNV_cgNHLjDGoBOFOB3x9J8J-_Q-uIf8LdT9lpvYECrI5M4iLNoGeLzK_V6QQvA1WZo1GJmz9PQ5OFShRfWRbJB8WubDB8b4XegSDbzbxow2NFUfj8njYLa9l7o5V8f7OsywQcX9sLu6l4OcpeqWi3xEQmjwlJnWe1TR6bGE6EzzIzU0LdE71zaTD3cPsupxNoB8fkD-tiWecLkr_0k_GrqhnXS3BRXsRWFGGzZtD4RZdgUEVjyNnk8nxiATh-2w3Z1OhfqfEpukKbgwEc0WLdtzz--lZx0v0Bw3hBbn-lexxynPzM2g_S9VKyGvMgCyxT6GXT4h5kQ7bxuYNYNsENNslQsOMITLopyEhrZtCjszdj3K0F_8x6ZyedNg1eLMD7RDn8eyBE0deEnpva6ml8Rf-Eq9JYAVSPhCz-DadzFzB5M6DwOEX83cpna1o5Ct5v19o7YrL9mOvbnNcHXr7xAfWbbIYAWzO_hhfLx30k-0gdejLp1ECf5qMI0yGu65ClH5sguD4VabDan_ObdaKpgk0_diEwXWIJSquFtkYmij8q42ILRpJqFQzY6FZCzah5oLL4tLDbWxzkO4ouHr4UyrbIbsezyXeKcSoA4Fv-69IFetBQwWF6uxjwR_veEcN4XBHMPfnkSZweDAKxcZvb5pY--01c2wKiH2wufc1ADMffEkDXEDSNt9uYGH12eFDqwT1YxByiu2Gzo3QcRu6oyOJ2NwPQsJai00jIYwMyhTobBkH-X-9e3p44hQ4p8imuWW8stHe6XmPvSTVZbvFaS4hss-kxTUNXMzX_RUzHpc4TmcBj4UfIbfd5RkrdScymaetdA2K2x9iJMCddq0lqXgUx942mPc-cJBlGk_6WGs-acC3a2_1kG_-rJelHEGP1UWmZBWvYyzIQEEAGwg.QUn-SLFkBLqWYeuq2txvYw"



start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: "

def openai_create(prompt):

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )

    return response.choices[0].text



def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history

def outputsGPT(input, history):
    resp = api1.send_message(input)
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    output = resp['message']
    history.append((input, output))
    print("Human: ", input)
    print("ChatGPT: ", output)
    return history, history


block = gr.Blocks()
api1 = ChatGPT(session_token) 

with block:
    try:
        chatbot = gr.Chatbot()
        message = gr.Textbox(placeholder=prompt)
        state = gr.State()
        submit = gr.Button("SEND")
        submit.click(outputsGPT, inputs=[message, state], outputs=[chatbot, state])
    except Exception as e:
        print("Error: ", e.message, e.args)

block.launch(debug = False, show_api=False)
