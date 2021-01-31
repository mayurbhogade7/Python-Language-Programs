def sent(lists):
    for list in lists:
        print(f"sending {list}")
        n_messages.append(list)

messages = ['hi', 'how are you?', "what's up", 'I love you', 'I like you']
n_messages = []
sent(messages)
print(n_messages)