
# to creat api key >>>>>  https://platform.openai.com/account/api-keys
import os
import openai
os.system('pip install -qq openai')
while True:

    ask = input(">>> ")

    openai.api_key = " " #Enter your  API key

    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": f"{ask}"}])


    print(f"\n{completion.choices[0].message.content}")
    print("\n_______________________________\n")
    print("$ Do You Have a New Question Sir ?")
    print("_______________________________\n")
