'''
Problem Statement: The goal is to tokenize the following 5 sentences into words, excluding the stop words. Input:

sentences = ["a new world record was set", 
            "in the holy city of ayodhya",
            "on the eve of diwali on tuesday",
            "with over three lakh diya or earthen lamps",
            "lit up simultaneously on the banks of the sarayu river"] 
            stopwords = ['for', 'a', 'of', 'the', 'and', 'to', 'in','on','with','was']
'''
sentences = ["a new world record was set", 
            "in the holy city of ayodhya",
            "on the eve of diwali on tuesday",
            "with over three lakh diya or earthen lamps",
            "lit up simultaneously on the banks of the sarayu river"]
stopwords = ['for', 'a', 'of', 'the', 'and', 'to', 'in','on','with','was']
res=[]
for sentence in sentences:
    row_data=[]
    for word in sentence.split():
        if word not in stopwords:
            row_data.append(word)
    res.append(row_data)
print(res)

