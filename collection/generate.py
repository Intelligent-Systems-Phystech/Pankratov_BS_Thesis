
from scipy import sparse
from scipy.stats import dirichlet
from scipy.stats import multinomial
from scipy.stats import zipf
import numpy as np

DOCS = 2000
WORDS = 10000
TOPICS = 100
WORDS_IN_DOC = 1000


def generate_phi(alpha, num_topics=TOPICS, num_words=WORDS):
    "alpha - параметр распределения Дирихле для генерации. 
    alphaphi = np.ones(num_words) * alpha
    phi = dirichlet.rvs(alphaphi, size = num_topics, random_state = 1).transpose() 
    return phi

def generate_theta(beta, num_docs=DOCS, num_topics=TOPICS):
    "beta - параметр распределения Дирихле для генерации.
    beta = np.ones(num_topics) * beta
    theta = dirichlet.rvs(beta, size = num_docs, random_state = 1).transpose()
    return theta
                          
def generate_doc(i, phi, theta, num_words_in_doc=WORDS_IN_DOC):
    "i - порядковый номер генерируемого документа. Не должен превышать число столбцов theta
    topicvec = multinomial.rvs(num_words_in_doc, theta[:,i], size = 1, random_state = 1)
    words_in_doc = np.zeros(len(phi))
    for j in range(len(topicvec[0])):
        words_in_doc = words_in_doc + multinomial.rvs(topicvec[0][j], phi[:,j], size = 1, random_state = 1)
    return words_in_doc[0]
    
def generate_collection(num_docs, phi, theta, num_words_in_doc=WORDS):
    collection = []
    for i in range(num_docs):
        collection.append(generate_doc(i, phi, theta, num_words_in_doc))
    return collection

def check_imbalance_degree(theta,phone_deg):
    "Выдает пару степеней несбалансированности сгенерированной Theta: для первого и второго смысла
    deg1 = np.max((np.sum(theta,axis = 1)))/np.min(np.sum(theta,axis = 1))
    deg2 = np.sum(np.abs((np.sum(theta,axis = 1) - (1 - phone_deg)*20)))
    return (deg1,deg2)
