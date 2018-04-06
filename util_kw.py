lower_caste_keywords = ['dalit', 'untouchable', 'sc_st', 'obc', 'lower_caste', 'minorities', 'backward_class']
neutral_keywords = ['individual', 'man', 'woman', 'person', 'people', 'subject', 'object', 'human']
upper_caste_keywords = ['upper_caste', 'kshatriya', 'brahmin', 'government', 'democracy', 'election', 'college', 'education', 'scholar', 'merit', 'meritorous', 'international', 'rich']
negative_aspect = ['poor', 'violence', 'disease', 'unhealthy', 'incident', 'crime']
positive_aspect = ['empathy', 'care', 'companion', 'friend', 'healthy', 'prosperity']

def add_to_graph(word, assoclist, graph):
    graph.add_node(word)
    for wtuple in assoclist:
        kword, kweight = wtuple
        graph.add_node(kword)
        graph.add_edge(word, kword, weight=kweight)
        
def recurse_add_(word, wvmodel, graph, depth=1, topn=5):
    if depth==1:
        # call add_to_graph and return
        alist = wvmodel.most_similar(word, topn=topn)
        add_to_graph(word, alist, graph)
        return
    else:
        # generate wordlist, then call recurse_add_ with each word in wordlist, with depth-1
        alist = wvmodel.most_similar(word, topn=topn)
        for wtuple in alist:
            aword, _ = wtuple
            recurse_add_(aword, wvmodel, graph, depth=depth-1, topn=topn)