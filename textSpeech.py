from gtts import gTTS

article = """
Why we need to pass a function to setState﴾﴿?
The reason behind for this is that setState() is an asynchronous operation. React
batches state changes for performance reasons, so the state may not change
immediately after setState() is called. That means you should not rely on the
current state when calling setState() since you can't be sure what that state will
be. The solution is to pass a function to setState() , with the previous state as an
argument. By doing this you can avoid issues with the user getting the old state
value on access due to the asynchronous nature of setState() .
Let's say the initial count value is zero. After three consecutive increment
operations, the value is going to be incremented only by one
"""

language = 'en'
gttsT = gTTS(text=article, lang=language)
gttsT.save("wired_article.mp3")
print("Convert Successfully")